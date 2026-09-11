@echo off
chcp 65001 >nul
REM 论文追踪系统 - 每日运行脚本
REM 最后更新：2026-09-11

cd /d "%~dp0"
echo ============================================================
echo 📚 论文追踪系统 - 每日运行
echo ============================================================
echo.

python paper_tracker.py

if %errorlevel% equ 0 (
    echo.
    echo ✅ 追踪完成！请查看 00_Inbox/待处理/ 下的日报文件
) else (
    echo.
    echo ❌ 运行失败！请检查错误信息
)

echo.
pause
