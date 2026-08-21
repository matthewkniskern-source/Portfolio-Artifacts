<#
.SYNOPSIS
    Identifies suspicious failed-to-successful authentication patterns.

.DESCRIPTION
    Find-SuspiciousLogons.ps1 reviews normalized authentication data and
    identifies accounts that experience repeated failed logons followed by
    a successful authentication from the same source within a configurable
    time window.

    The script is intended to surface investigation candidates. It does not
    classify the activity as malicious.

.PARAMETER Path
    Path to the authentication-events CSV file.

.PARAMETER FailureThreshold
    Minimum number of failed logons required before a pattern is flagged.

.PARAMETER WindowMinutes
    Maximum number of minutes allowed between the first failed logon and
    the successful authentication.

.PARAMETER OutputPath
    Optional path for exporting flagged patterns as CSV.

.EXAMPLE
    .\Find-SuspiciousLogons.ps1 `
        -Path "..\02 evidence\authentication-events.csv" `
        -FailureThreshold 5 `
        -WindowMinutes 5

    Reviews the case-study authentication dataset and identifies repeated
    failures followed by a successful authentication within five minutes.

.NOTES
    Designed as a defensive SOC case-study utility.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidateScript({ Test-Path $_ })]
    [string]$Path,

    [Parameter()]
    [ValidateRange(1,100)]
    [int]$FailureThreshold = 5,

    [Parameter()]
    [ValidateRange(1,1440)]
    [int]$WindowMinutes = 5,

    [Parameter()]
    [string]$OutputPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Convert-ToDateTime {
    param(
        [Parameter(Mandatory)]
        [string]$Value
    )

    return [datetime]::Parse($Value)
}

Write-Host ""
Write-Host "Suspicious Logon Review"
Write-Host "-----------------------"
Write-Host "Input:             $Path"
Write-Host "Failure threshold: $FailureThreshold"
Write-Host "Window:            $WindowMinutes minute(s)"
Write-Host ""

$Events = Import-Csv -Path $Path |
    ForEach-Object {
        [PSCustomObject]@{
            Timestamp     = Convert-ToDateTime $_.Timestamp
            EventID       = [int]$_.EventID
            Account       = $_.Account
            SourceAsset   = $_.SourceAsset
            SourceIP      = $_.SourceIP
            TargetAsset   = $_.TargetAsset
            LogonType     = $_.LogonType
            Status        = $_.Status
            FailureReason = $_.FailureReason
            Notes         = $_.Notes
        }
    } |
    Sort-Object Timestamp

$Groups = $Events |
    Group-Object Account, SourceAsset

$Findings = foreach ($Group in $Groups) {

    $GroupEvents = $Group.Group |
        Sort-Object Timestamp

    $Failures = $GroupEvents |
        Where-Object { $_.EventID -eq 4625 }

    foreach ($Failure in $Failures) {

        $WindowEnd = $Failure.Timestamp.AddMinutes($WindowMinutes)

        $WindowFailures = $GroupEvents |
            Where-Object {
                $_.EventID -eq 4625 -and
                $_.Timestamp -ge $Failure.Timestamp -and
                $_.Timestamp -le $WindowEnd
            }

        if ($WindowFailures.Count -lt $FailureThreshold) {
            continue
        }

        $LastFailure = $WindowFailures[-1]

        $Success = $GroupEvents |
            Where-Object {
                $_.EventID -eq 4624 -and
                $_.Timestamp -gt $LastFailure.Timestamp -and
                $_.Timestamp -le $WindowEnd
            } |
            Select-Object -First 1

        if ($null -eq $Success) {
            continue
        }

        $FirstFailure = $WindowFailures[0]
        $Duration = $Success.Timestamp - $FirstFailure.Timestamp

        [PSCustomObject]@{
            Account          = $FirstFailure.Account
            SourceAsset      = $FirstFailure.SourceAsset
            SourceIP         = $FirstFailure.SourceIP
            FailureCount     = $WindowFailures.Count
            FirstFailure     = $FirstFailure.Timestamp
            LastFailure      = $LastFailure.Timestamp
            SuccessfulLogon  = $Success.Timestamp
            ElapsedSeconds   = [math]::Round($Duration.TotalSeconds, 0)
            LogonType        = $Success.LogonType
            TargetAsset      = $Success.TargetAsset
            Pattern          = "Repeated failures followed by success"
        }

        break
    }
}

$Findings = @($Findings)

if ($Findings.Count -eq 0) {
    Write-Host "[-] No matching authentication patterns found."
    return
}

Write-Host "[+] $($Findings.Count) candidate pattern(s) identified."
Write-Host ""

$Findings |
    Sort-Object FirstFailure |
    Format-Table `
        Account,
        SourceAsset,
        FailureCount,
        FirstFailure,
        SuccessfulLogon,
        ElapsedSeconds `
        -AutoSize

if ($OutputPath) {

    $Directory = Split-Path -Parent $OutputPath

    if ($Directory -and -not (Test-Path $Directory)) {
        New-Item -Path $Directory -ItemType Directory -Force | Out-Null
    }

    $Findings |
        Export-Csv `
            -Path $OutputPath `
            -NoTypeInformation `
            -Encoding UTF8

    Write-Host ""
    Write-Host "[+] Findings exported to $OutputPath"
}
