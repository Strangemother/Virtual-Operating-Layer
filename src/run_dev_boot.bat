@echo off
echo Starting Build "../build/" runtime
cmd /V /C "set PYTHONSTARTUP=startup.tpy&& python -qSsuOOI"
@echo on

