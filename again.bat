@echo off
set filename=%Date:~0,4%%Date:~5,2%%Date:~8,2%-%time:~0,2%-%time:~3,2%-%time:~6,2%
copy in.txt bak\%filename%.txt
move /y ok\ok.txt in.txt 
python url.py
pause