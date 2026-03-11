@echo off
echo.
echo   Building Buckshot Tracker for Windows...
echo.

pyinstaller ^
  --onefile ^
  --name server ^
  --add-data "buckshot-tracker.html;." ^
  --icon icon.ico ^
  server.py

if not exist "..\windows-app" mkdir "..\windows-app"
copy dist\server.exe ..\windows-app\server.exe

rmdir /s /q build
rmdir /s /q dist
rmdir /s /q __pycache__
del server.spec

echo.
echo   Done! Binary: ..\windows-app\server.exe
echo.