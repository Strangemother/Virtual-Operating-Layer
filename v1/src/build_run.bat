@echo off
python build-scripts/build.py
echo Starting Build "../build/" runtime
cmd /V /C "cd C:\Users\jay\Documents\projects\desktop\build && boot.exe"
@echo on


