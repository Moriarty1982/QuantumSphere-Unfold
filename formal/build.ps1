# Baut formal/ in einem Spiegelordner außerhalb von OneDrive.
#
# Mathlib braucht unter .lake/ rund 5 GB. Im OneDrive-Ordner würde das hochgeladen; ein
# Verzeichnislink hilft nicht, OneDrive verfolgt ihn (getestet 2026-10-22). Deshalb wird
# der Quelltext in den Zielordner gespiegelt (ohne .lake/), dort gebaut, und ein geändertes
# lake-manifest.json wird zurückkopiert.
#
#   .\build.ps1                    # lake build
#   .\build.ps1 exe cache get      # beliebige lake-Argumente
#
# Zielordner: $env:QS_FORMAL_BUILD_DIR, sonst %USERPROFILE%\.qs-formal-build. Nicht
# %LOCALAPPDATA%: aus einer paketierten App (etwa der Claude-Desktop-App) heraus wird das auf
# einen app-eigenen Ordner umgeleitet, und eine normale Shell fände den Build dort nicht.

$BuildDir = if ($env:QS_FORMAL_BUILD_DIR) { $env:QS_FORMAL_BUILD_DIR } else { "$env:USERPROFILE\.qs-formal-build" }
if (-not [System.IO.Path]::IsPathRooted($BuildDir)) { throw "Zielordner muss absolut sein: $BuildDir" }

$src = $PSScriptRoot
[string[]] $lakeArgs = if ($args.Count -gt 0) { $args } else { "build" }
$env:PATH = "$env:USERPROFILE\.elan\bin;$env:PATH"

robocopy $src $BuildDir /MIR /XD .lake /XF build.ps1 /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy fehlgeschlagen ($LASTEXITCODE)" }

Push-Location $BuildDir
try {
    & lake @lakeArgs
    $rc = $LASTEXITCODE
} finally {
    Pop-Location
}

$m = Join-Path $BuildDir "lake-manifest.json"
if ((Test-Path $m) -and ((Get-FileHash $m).Hash -ne (Get-FileHash (Join-Path $src "lake-manifest.json")).Hash)) {
    Copy-Item $m (Join-Path $src "lake-manifest.json")
    Write-Host "lake-manifest.json aktualisiert"
}
exit $rc
