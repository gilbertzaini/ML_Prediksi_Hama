@echo off
setlocal enabledelayedexpansion

set "DIR=%~dp0"
cd /d "%DIR%"

call venv\Scripts\activate
python main.py

exit /b 0
