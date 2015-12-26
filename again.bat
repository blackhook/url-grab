@echo off
set filename=%Date:~0,4%%Date:~5,2%%Date:~8,2%-%time:~0,2%-%time:~3,2%-%time:~6,2%
copy ok\fulldomain.txt bak\%filename%_fulldomain.txt
copy ok\fullpath.txt bak\%filename%_fullpath.txt
move /y ok\fulldomain.txt in.txt 
del /q ok\fullpath.txt
python url.py
pause