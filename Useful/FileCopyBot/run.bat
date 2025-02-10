@echo off

REM Move to the directory of this batch file
cd /d "%~dp0"

REM Run the Python script
python copyBot.py

REM Keep the window open so you can see any output or errors
pause
