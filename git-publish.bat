@echo off
echo ----------------------------------------------------------------------------
echo Automatically add all files, commit and publish to remote repository
echo ----------------------------------------------------------------------------

setLocal EnableDelayedExpansion

REM Check if there is any unstaged
for /f %%i in ('git status --porcelain 2^>/dev/null^| egrep "^??" ^| wc -l') do set changedFiles=%%i

REM If nothing changed abort
if "%changedFiles%" == 0 goto end

REM Set location of Version file.
set VFILE=".\VERSION.txt"
set /p currentVersion= <%VFILE%

echo %currentVersion%

for /f "tokens=1" %%a in ("%currentVersion%") do set verPrimary=%%a
for /f "tokens=3" %%a in ("%currentVersion%") do set verBuild=%%a

set pushMessage="Auto publish %currentVersion%"

REM Check if tag exist for current version
set addTag=1
for /f %%i in ('git tag') do (

    if "%verPrimary%" == "%%i" (
        set addTag=0
    )
)

REM Add tag if not already

if %addTag%==1 (
    echo 
    echo Version incremented, adding new tag
    echo -----------------------------------
    echo 
    echo git tag -a "%verPrimary%" -m "Version %verPrimary%"
)

echo git add --all
echo git commit -m %pushMessage%
echo git push origin master
echo git push --tags

:end
pause