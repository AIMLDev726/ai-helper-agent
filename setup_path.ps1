# AI Helper Agent - PATH Setup Script
# This script adds Python Scripts directory to PATH for direct command access

Write-Host "AI Helper Agent - PATH Setup" -ForegroundColor Cyan
Write-Host "=================================================="

$pythonScriptsPath = "C:\Users\$env:USERNAME\AppData\Roaming\Python\Python312\Scripts"

# Check if the directory exists
if (Test-Path $pythonScriptsPath) {
    Write-Host "Python Scripts directory found: $pythonScriptsPath" -ForegroundColor Green
    
    # Check if it's already in PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
    
    if ($currentPath -like "*$pythonScriptsPath*") {
        Write-Host "Directory already in PATH" -ForegroundColor Green
    } else {
        Write-Host "Adding to user PATH..." -ForegroundColor Yellow
        
        try {
            # Add to user PATH (permanent)
            $newPath = "$currentPath;$pythonScriptsPath"
            [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
            
            Write-Host "Successfully added to PATH!" -ForegroundColor Green
            Write-Host "You may need to restart your terminal/IDE for changes to take effect" -ForegroundColor Blue
        } catch {
            Write-Host "Failed to update PATH: $($_.Exception.Message)" -ForegroundColor Red
            Write-Host "You can manually add this to your PATH: $pythonScriptsPath" -ForegroundColor Yellow
        }
    }
    
    # Test if commands work
    Write-Host ""
    Write-Host "Testing console commands..." -ForegroundColor Cyan
    
    $commands = @("ai-helper", "ai-helper-agent", "ai_helper_agent")
    
    foreach ($cmd in $commands) {
        $fullPath = Join-Path $pythonScriptsPath "$cmd.exe"
        if (Test-Path $fullPath) {
            Write-Host "$cmd.exe - Available" -ForegroundColor Green
        } else {
            Write-Host "$cmd.exe - Not found" -ForegroundColor Red
        }
    }
    
    Write-Host ""
    Write-Host "Available Commands After Setup:" -ForegroundColor Cyan
    Write-Host "   ai-helper --help          # Show help"
    Write-Host "   ai-helper --version       # Show version"
    Write-Host "   ai-helper                 # Start interactive session"
    Write-Host "   ai-helper-agent           # Alternative command"
    Write-Host "   ai_helper_agent           # Alternative command"
    
    Write-Host ""
    Write-Host "Usage Example:" -ForegroundColor Cyan
    Write-Host "   ai-helper"
    Write-Host "   Enter your Groq API key: [your_key_here]"
    Write-Host "   AI Helper Agent v1.0.0 - Interactive Session"
    Write-Host "   Workspace: $PWD"
    Write-Host "   You: help me analyze my code"
    
} else {
    Write-Host "Python Scripts directory not found: $pythonScriptsPath" -ForegroundColor Red
    Write-Host "Make sure Python and ai-helper-agent are installed" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Setup complete!" -ForegroundColor Green
