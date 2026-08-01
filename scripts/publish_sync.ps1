# Rebuild GitHub Pages docs/ from data/sync and push to origin when needed.
# Safe to run from Task Scheduler after research jobs finish (debounced via flag).
#
# Usage:
#   .\scripts\publish_sync.ps1
#   .\scripts\publish_sync.ps1 -Force
#   .\scripts\publish_sync.ps1 -DryRun
#
# Install schedule:
#   .\scripts\install_publish_sync.ps1

param(
  [switch]$Force,
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$LogDir = Join-Path $Root "data"
if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir | Out-Null }
$Log = Join-Path $LogDir "publish_sync.log"
$Flag = Join-Path $LogDir "publish_requested"

function Write-PubLog([string]$msg) {
  $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $msg"
  Add-Content -Path $Log -Value $line
  Write-Host $line
}

function Test-GitAvailable {
  try { git --version | Out-Null; return $true } catch { return $false }
}

if (-not (Test-GitAvailable)) {
  Write-PubLog "ERROR: git not found on PATH"
  exit 1
}

# Only publish when a research export requested it, or -Force, or sync/docs already dirty.
$flagExists = Test-Path $Flag
git status --porcelain -- "data/sync" "docs" | Out-Null
$dirtySync = @(git status --porcelain -- "data/sync" "docs")
$hasDirty = $dirtySync.Count -gt 0

if (-not $Force -and -not $flagExists -and -not $hasDirty) {
  Write-PubLog "Nothing to publish (no flag, clean tree)"
  exit 0
}

Write-PubLog "Publish start (force=$Force flag=$flagExists dirty=$hasDirty)"

# Prefer main for Pages source
$branch = (git rev-parse --abbrev-ref HEAD).Trim()
if ($branch -eq "HEAD") {
  Write-PubLog "ERROR: detached HEAD — abort"
  exit 1
}

# Pull latest so we don't fight overnight cloud commits
try {
  git fetch origin 2>&1 | ForEach-Object { Write-PubLog "fetch: $_" }
  $upstream = "origin/$branch"
  $hasUpstream = git rev-parse --verify $upstream 2>$null
  if ($LASTEXITCODE -eq 0) {
    git pull --rebase --autostash origin $branch 2>&1 | ForEach-Object { Write-PubLog "pull: $_" }
    if ($LASTEXITCODE -ne 0) {
      Write-PubLog "ERROR: git pull --rebase failed"
      exit 1
    }
  }
} catch {
  Write-PubLog "WARN: pull failed: $_"
}

# Rebuild styled Pages site from sync packs
$py = $null
foreach ($c in @("py -3.11", "py -3", "python", "python3")) {
  try {
    $null = Invoke-Expression "$c -c `"import sys; print(sys.executable)`"" 2>$null
    if ($LASTEXITCODE -eq 0) { $py = $c; break }
  } catch { }
}
if (-not $py) {
  # Fall back to venv if present
  $venvPy = Join-Path $Root ".venv\Scripts\python.exe"
  if (Test-Path $venvPy) { $py = "`"$venvPy`"" }
}
if (-not $py) {
  Write-PubLog "ERROR: Python not found"
  exit 1
}

Write-PubLog "Building docs/ with $py"
$buildOut = Invoke-Expression "$py scripts\build_pages_site.py 2>&1"
$buildOut | ForEach-Object { Write-PubLog "build: $_" }
if ($LASTEXITCODE -ne 0) {
  Write-PubLog "ERROR: build_pages_site.py failed"
  exit 1
}

git add -- "data/sync" "docs"
$status = @(git status --porcelain -- "data/sync" "docs")
if ($status.Count -eq 0) {
  if (Test-Path $Flag) { Remove-Item $Flag -Force -ErrorAction SilentlyContinue }
  Write-PubLog "No file changes after build — cleared flag"
  exit 0
}

$summary = ($status | Select-Object -First 8) -join "; "
$msg = "Auto-publish research sync + Pages ($($status.Count) paths)"
Write-PubLog "Commit: $msg :: $summary"

if ($DryRun) {
  Write-PubLog "DryRun — skipping commit/push"
  git reset HEAD -- "data/sync" "docs" 2>$null | Out-Null
  exit 0
}

git -c user.useConfigOnly=true commit -m $msg 2>&1 | ForEach-Object { Write-PubLog "commit: $_" }
if ($LASTEXITCODE -ne 0) {
  # Retry with a local identity if repo has no user config (common on fresh clones)
  git -c user.name="Equity Research Agent" -c user.email="equity-research-agent@local" commit -m $msg 2>&1 |
    ForEach-Object { Write-PubLog "commit: $_" }
  if ($LASTEXITCODE -ne 0) {
    Write-PubLog "ERROR: commit failed"
    exit 1
  }
}

git push origin "HEAD:$branch" 2>&1 | ForEach-Object { Write-PubLog "push: $_" }
if ($LASTEXITCODE -ne 0) {
  Write-PubLog "ERROR: git push failed — check credentials (gh auth login / credential manager)"
  exit 1
}

if (Test-Path $Flag) { Remove-Item $Flag -Force -ErrorAction SilentlyContinue }
Write-PubLog "Publish OK → origin/$branch"
exit 0
