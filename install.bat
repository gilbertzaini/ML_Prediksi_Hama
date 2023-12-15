@echo off
setlocal enabledelayedexpansion

set "DIR=%~dp0"
cd /d "%DIR%"

python -m venv venv
call venv\Scripts\activate
pip install -r .\requirements.txt
python main.py

exit /b 0
