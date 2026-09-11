# 创建 Windows 任务计划程序 - 每日自动运行论文追踪
# 运行方式：在 PowerShell 中以管理员身份执行此脚本

$TaskName = "论文追踪-每日运行"
$ScriptPath = "D:\claude\hcmingGo\hcmingGo\04_Projects\城市低空资源研究\_tools\run_paper_tracker.bat"
$WorkingDir = "D:\claude\hcmingGo\hcmingGo\04_Projects\城市低空资源研究\_tools"

# 创建任务操作
$Action = New-ScheduledTaskAction -Execute $ScriptPath -WorkingDirectory $WorkingDir

# 创建触发器（每天上午 9:00）
$Trigger = New-ScheduledTaskTrigger -Daily -At 9:00AM

# 创建任务设置
$Settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1)

# 注册任务
Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Description "自动追踪 UAM 相关最新论文，每日上午 9:00 运行" `
    -Force

Write-Host "✅ 任务计划已创建：$TaskName" -ForegroundColor Green
Write-Host "   运行时间：每天上午 9:00" -ForegroundColor Cyan
Write-Host "   查看任务：taskschd.msc" -ForegroundColor Yellow
