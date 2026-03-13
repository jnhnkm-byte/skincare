@echo off
chcp 65001 >nul 2>&1
title JH Smart Skincare Recommender

echo ==================================================
echo   JH Smart Skincare Recommender
echo   Kumoh National Institute of Technology
echo ==================================================
echo.

set PYTHON_CMD=
where python3 >nul 2>&1 && set PYTHON_CMD=python3
if "%PYTHON_CMD%"=="" where python >nul 2>&1 && set PYTHON_CMD=python
if "%PYTHON_CMD%"=="" (
    echo [ERROR] Python not found. Please install Python 3.9+
    pause
    exit /b 1
)

echo [INFO] Using: %PYTHON_CMD%
%PYTHON_CMD% --version
echo.

echo [INFO] Installing dependencies...
%PYTHON_CMD% -m pip install --upgrade pip >nul 2>&1
%PYTHON_CMD% -m pip install -r "%~dp0requirements.txt" --quiet 2>nul
echo [OK] Dependencies installed.
echo.

echo [INFO] Starting app... Browser will open automatically.
%PYTHON_CMD% -m streamlit run "%~dp0app.py" --server.headless true --browser.gatherUsageStats false

pause
