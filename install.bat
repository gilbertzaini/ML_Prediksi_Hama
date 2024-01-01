@echo off
python -m venv venv & ".\venv\Scripts\activate" & pip install -r requirements.txt & python -x "main.py" & "deactivate"