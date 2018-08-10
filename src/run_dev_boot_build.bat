@echo off
echo Starting Build "../build/" runtime
cmd /V /C "set PYTHONSTARTUP=../build/bios_runtime/startup&& ..\build\bios_runtime\vol_runtime.exe -qSsuOO"
@echo on

