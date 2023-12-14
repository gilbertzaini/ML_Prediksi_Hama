@echo off

:: Get the directory of the script
set "DIR=%~dp0"

:: Change to the script directory
cd /d "%DIR%"

:: Activate virtual environment
call venv\Scripts\activate

:: Run the Python script
python main.py

:: Deactivate virtual environment (optional)
deactivate
