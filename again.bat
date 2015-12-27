@echo off
set filename=%Date:~0,4%%Date:~5,2%%Date:~8,2%-%time:~0,2%-%time:~3,2%-%time:~6,2%
@echo off
copy ok\fulldomain.txt bak\%filename%_fulldomain.txt >nul 2>nul
@echo off
copy ok\fullpath.txt bak\%filename%_fullpath.txt >nul 2>nul
@echo off
move /y ok\fulldomain.txt in.txt  >nul 2>nul
del /q ok\fullpath.txt >nul 2>nul
python url.py
pause