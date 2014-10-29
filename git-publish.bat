@echo off
echo ----------------------------------------------------------------------------
echo Automatically add all files, commit and publish to remote repository
echo ----------------------------------------------------------------------------

setLocal EnableDelayedExpansion

REM Check if there is any staged changes
for /f %%i in ('git diff --name-only --cached') do set changedFiles=%%i

REM If nothing changed abort
if "%changedFiles%" == "" goto end

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
    echo git tag -a "%verPrimary%" -m "Version %verPrimary%"
)

git add --all
git commit -m %pushMessage%
git push origin master
git push --tags

:end
pause