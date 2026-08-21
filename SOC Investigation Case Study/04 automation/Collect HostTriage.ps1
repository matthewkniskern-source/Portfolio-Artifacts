<#
.SYNOPSIS
    Collects a focused Windows host-triage package for SOC investigation.

.DESCRIPTION
    Collect-HostTriage.ps1 gathers host identity, active user sessions,
    Windows Security events, running processes, and active TCP connections.

    The script is intended for first-pass defensive investigation and
    preserves results as structured CSV and text files for later review.

.PARAMETER StartTime
    Beginning of the investigation window.

.PARAMETER EndTime
    End of the investigation window.

.PARAMETER OutputPath
    Directory where collected evidence will be written.

.EXAMPLE
    .\Collect-HostTriage.ps1 `
        -StartTime "2026-08-17 06:45:00" `
        -EndTime "2026-08-17 07:05:00" `
        -OutputPath ".\triage-output"

.NOTES
    Designed as a defensive SOC case-study utility.
    Administrative privileges may be required for complete Security log access.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [datetime]$StartTime,

    [Parameter(Mandatory)]
    [datetime]$EndTime,

    [Parameter()]
    [string]$OutputPath = ".\triage-output"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ($EndTime -le $StartTime) {
    throw "EndTime must be later than StartTime."
}

$OutputPath = [System.IO.Path]::GetFullPath($OutputPath)

if (-not (Test-Path $OutputPath)) {
    New-Item -Path $OutputPath -ItemType Directory -Force | Out-Null
}

$CollectionTime = Get-Date
$Hostname       = $env:COMPUTERNAME

Write-Host ""
Write-Host "Windows Host Triage"
Write-Host "-------------------"
Write-Host "Host:        $Hostname"
Write-Host "Start:       $StartTime"
Write-Host "End:         $EndTime"
Write-Host "Output:      $OutputPath"
Write-Host ""

function Export-Collection {
    param(
        [Parameter(Mandatory)]
        [string]$Name,

        [Parameter(Mandatory)]
        [scriptblock]$Command
    )

    $Path = Join-Path $OutputPath "$Name.csv"

    try {
        $Results = & $Command

        if ($null -ne $Results) {
            $Results |
                Export-Csv -Path $Path -NoTypeInformation -Encoding UTF8

            Write-Host "[+] $Name"
        }
        else {
            Write-Host "[-] $Name - no results"
        }
    }
    catch {
        Write-Warning "$Name collection failed: $($_.Exception.Message)"
    }
}

#
# Host Identity
#

Export-Collection -Name "host-information" -Command {

    $OS = Get-CimInstance Win32_OperatingSystem
    $Computer = Get-CimInstance Win32_ComputerSystem

    [PSCustomObject]@{
        CollectionTime = $CollectionTime
        Hostname       = $Hostname
        Domain         = $Computer.Domain
        Manufacturer   = $Computer.Manufacturer
        Model          = $Computer.Model
        OS             = $OS.Caption
        OSVersion      = $OS.Version
        LastBootTime   = $OS.LastBootUpTime
        CurrentUser    = $Computer.UserName
    }
}

#
# Logged-On Users
#

Export-Collection -Name "logged-on-users" -Command {

    Get-CimInstance Win32_LoggedOnUser |
        ForEach-Object {

            [PSCustomObject]@{
                Antecedent = $_.Antecedent
                Dependent  = $_.Dependent
            }
        }
}

#
# Network Configuration
#

Export-Collection -Name "network-configuration" -Command {

    Get-NetIPConfiguration |
        ForEach-Object {

            [PSCustomObject]@{
                InterfaceAlias = $_.InterfaceAlias
                InterfaceIndex = $_.InterfaceIndex
                IPv4Address    = ($_.IPv4Address.IPAddress -join ';')
                IPv6Address    = ($_.IPv6Address.IPAddress -join ';')
                IPv4Gateway    = ($_.IPv4DefaultGateway.NextHop -join ';')
                DNSServers     = ($_.DNSServer.ServerAddresses -join ';')
            }
        }
}

#
# Running Processes
#

Export-Collection -Name "running-processes" -Command {

    Get-CimInstance Win32_Process |
        Select-Object `
            ProcessId,
            ParentProcessId,
            Name,
            ExecutablePath,
            CommandLine
}

#
# Active TCP Connections
#

Export-Collection -Name "tcp-connections" -Command {

    Get-NetTCPConnection |
        Where-Object {
            $_.State -in 'Established','Listen','SynSent'
        } |
        ForEach-Object {

            $Process = Get-Process `
                -Id $_.OwningProcess `
                -ErrorAction SilentlyContinue

            [PSCustomObject]@{
                LocalAddress  = $_.LocalAddress
                LocalPort     = $_.LocalPort
                RemoteAddress = $_.RemoteAddress
                RemotePort    = $_.RemotePort
                State         = $_.State
                PID           = $_.OwningProcess
                ProcessName   = $Process.ProcessName
            }
        }
}

#
# Authentication Events
#

Export-Collection -Name "authentication-events" -Command {

    Get-WinEvent -FilterHashtable @{
        LogName   = 'Security'
        Id        = 4624,4625
        StartTime = $StartTime
        EndTime   = $EndTime
    } |
        Select-Object `
            TimeCreated,
            Id,
            MachineName,
            ProviderName,
            RecordId,
            Message
}

#
# Process Creation Events
#

Export-Collection -Name "process-events" -Command {

    Get-WinEvent -FilterHashtable @{
        LogName   = 'Security'
        Id        = 4688
        StartTime = $StartTime
        EndTime   = $EndTime
    } |
        Select-Object `
            TimeCreated,
            Id,
            MachineName,
            ProviderName,
            RecordId,
            Message
}

#
# Security Event Timeline
#

Export-Collection -Name "security-timeline" -Command {

    Get-WinEvent -FilterHashtable @{
        LogName   = 'Security'
        Id        = 4624,4625,4688
        StartTime = $StartTime
        EndTime   = $EndTime
    } |
        Sort-Object TimeCreated |
        Select-Object `
            TimeCreated,
            Id,
            MachineName,
            RecordId
}

#
# Neighbor Table
#

Export-Collection -Name "network-neighbors" -Command {

    Get-NetNeighbor |
        Where-Object {
            $_.State -ne 'Unreachable'
        } |
        Select-Object `
            InterfaceAlias,
            IPAddress,
            LinkLayerAddress,
            State
}

#
# Collection Manifest
#

$Manifest = @"
SOC Host Triage Collection

Host:              $Hostname
Collection Time:   $CollectionTime
Investigation From: $StartTime
Investigation To:   $EndTime

Collected Data:
- Host information
- Logged-on users
- Network configuration
- Running processes
- Active TCP connections
- Windows Event 4624
- Windows Event 4625
- Windows Event 4688
- Combined security timeline
- Network neighbor table

Output Directory:
$OutputPath
"@

$Manifest |
    Set-Content `
        -Path (Join-Path $OutputPath "collection-manifest.txt") `
        -Encoding UTF8

Write-Host ""
Write-Host "[+] Collection complete."
Write-Host "[+] Evidence written to $OutputPath"
Write-Host ""
