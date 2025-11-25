# Push repository to remote GitHub repository
# Usage: Run this script from the repository root in PowerShell

param(
    [string]$RemoteUrl = 'https://github.com/manisha1600/Testproject.git',
    [string]$Branch = 'main'
)

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git is not installed or not in PATH. Install Git first: https://git-scm.com/download/win or use winget/choco."
    exit 1
}

# Initialize repo if needed
if (-not (Test-Path .git)) {
    git init
    git checkout -b $Branch
}

# Stage and commit
git add -A
$commitMsg = "Add initial project files, docs, tests, and CI"
# Only commit if there are staged changes
$porcelain = git status --porcelain 2>&1
if ($porcelain -ne "") {
    git commit -m $commitMsg
} else {
    Write-Host "No changes to commit."
}

# Add/update origin
if ((git remote) -contains 'origin') {
    git remote set-url origin $RemoteUrl
    Write-Host "Updated 'origin' to $RemoteUrl"
} else {
    git remote add origin $RemoteUrl
    Write-Host "Added 'origin' -> $RemoteUrl"
}

# Push
Write-Host "Pushing branch '$Branch' to origin..."
try {
    git push -u origin $Branch
} catch {
    Write-Error "Push failed. Ensure you have permission and authentication set up."
    exit 2
}

Write-Host 'Push completed.'
