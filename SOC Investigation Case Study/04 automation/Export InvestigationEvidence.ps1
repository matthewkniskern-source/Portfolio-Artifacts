<#
.SYNOPSIS
    Packages investigation evidence into a case-specific directory.

.DESCRIPTION
    Export-InvestigationEvidence.ps1 validates selected evidence files,
    copies them into an incident-specific export directory, calculates
    SHA-256 hashes, and writes a manifest describing the exported evidence.

    The script supports basic evidence integrity and case organization.
    It is not intended to replace formal forensic chain-of-custody procedures.

.PARAMETER CaseId
    Incident or case identifier used to name the export directory.

.PARAMETER EvidencePath
    Directory containing the source evidence files.

.PARAMETER OutputRoot
    Root directory where the case evidence package will be created.

.PARAMETER Include
    Optional list of file names to include from the evidence directory.

.EXAMPLE
    .\Export-InvestigationEvidence.ps1 `
        -CaseId "SOC-2026-0817-0042" `
        -EvidencePath "..\02 evidence" `
        -OutputRoot ".\exports"

    Creates an incident-specific evidence package containing the default
    case-study evidence files and a SHA-256 manifest.

.NOTES
    Designed as a defensive SOC case-study utility.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$CaseId,

    [Parameter(Mandatory)]
    [ValidateScript({ Test-Path $_ -PathType Container })]
    [string]$EvidencePath,

    [Parameter()]
    [string]$OutputRoot = ".\exports",

    [Parameter()]
    [string[]]$Include = @(
        "authentication-events.csv",
        "process-events.csv",
        "network-connections.csv",
        "evidence-notes.md"
    )
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$EvidencePath = [System.IO.Path]::GetFullPath($EvidencePath)
$OutputRoot   = [System.IO.Path]::GetFullPath($OutputRoot)

$ExportPath = Join-Path $OutputRoot $CaseId

if (-not (Test-Path $OutputRoot)) {
    New-Item -Path $OutputRoot -ItemType Directory -Force | Out-Null
}

if (Test-Path $ExportPath) {
    throw "Export directory already exists: $ExportPath"
}

New-Item -Path $ExportPath -ItemType Directory -Force | Out-Null

Write-Host ""
Write-Host "Investigation Evidence Export"
Write-Host "-----------------------------"
Write-Host "Case ID:      $CaseId"
Write-Host "Source:       $EvidencePath"
Write-Host "Destination:  $ExportPath"
Write-Host ""

$ManifestEntries = foreach ($FileName in $Include) {

    $SourceFile = Join-Path $EvidencePath $FileName

    if (-not (Test-Path $SourceFile -PathType Leaf)) {
        Write-Warning "Evidence file not found: $FileName"
        continue
    }

    $DestinationFile = Join-Path $ExportPath $FileName

    Copy-Item `
        -Path $SourceFile `
        -Destination $DestinationFile

    $Hash = Get-FileHash `
        -Path $DestinationFile `
        -Algorithm SHA256

    $Item = Get-Item $DestinationFile

    Write-Host "[+] Exported $FileName"

    [PSCustomObject]@{
        CaseId        = $CaseId
        FileName      = $Item.Name
        SizeBytes     = $Item.Length
        LastWriteTime = $Item.LastWriteTime
        SHA256        = $Hash.Hash
    }
}

$ManifestEntries = @($ManifestEntries)

if ($ManifestEntries.Count -eq 0) {
    Remove-Item -Path $ExportPath -Recurse -Force
    throw "No evidence files were exported."
}

$ManifestCsv = Join-Path $ExportPath "evidence-manifest.csv"

$ManifestEntries |
    Sort-Object FileName |
    Export-Csv `
        -Path $ManifestCsv `
        -NoTypeInformation `
        -Encoding UTF8

$ExportTime = Get-Date

$Summary = @"
Investigation Evidence Package

Case ID:        $CaseId
Export Time:    $ExportTime
Source Path:    $EvidencePath
Export Path:    $ExportPath
Hash Algorithm: SHA-256

Files Exported: $($ManifestEntries.Count)

Purpose:
This package contains normalized case-study evidence associated with the
SOC investigation. SHA-256 hashes are provided to support basic integrity
verification of the exported files.

Limitations:
This export demonstrates evidence organization and integrity checking.
It does not represent a formal forensic acquisition or complete legal
chain-of-custody process.
"@

$Summary |
    Set-Content `
        -Path (Join-Path $ExportPath "evidence-package-summary.txt") `
        -Encoding UTF8

Write-Host ""
Write-Host "[+] Evidence package complete."
Write-Host "[+] Files exported: $($ManifestEntries.Count)"
Write-Host "[+] Manifest: $ManifestCsv"
Write-Host ""
