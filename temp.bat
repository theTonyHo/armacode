@echo off
echo ----------------------------------------------------------------------------
echo Automatically add all files, commit and publish to remote repository
echo ----------------------------------------------------------------------------

setLocal EnableDelayedExpansion

REM Version file path
set VFILE=".\VERSION.txt"
set /p currentVersion= <%VFILE%

echo %currentVersion%

for /f "tokens=1" %%a in ("%currentVersion%") do set verPrimary=%%a
for /f "tokens=3" %%a in ("%currentVersion%") do set verBuild=%%a

set pushMessage="Auto publish %currentVersion%"

git tag -a "%verPrimary%" -m "Version %verPrimary%"
git push --tags
git add --all
git commit -m %pushMessage%
git push origin master
pause