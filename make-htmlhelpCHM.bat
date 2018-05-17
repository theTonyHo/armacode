@echo off

REM REFERENCE: https://stackoverflow.com/questions/39150947/htmlhelp-compiler-works-perfectly-from-command-line-but-not-run-from-a-script-or

set hhpFile="%~dp0build\htmlhelp\armacode.hhp"

echo '//--- HH Compiler start --------------------------------------
if exist "C:\Program Files (x86)\HTML Help Workshop\hhc.exe" (
"C:\Program Files (x86)\HTML Help Workshop\hhc.exe" %hhpFile%
) else (
    echo "Unable to find hhc.exe. Please install HTML Help Workshop. https://www.microsoft.com/en-au/download/details.aspx?id=21138"
)

echo '//--- HH Compiler end   --------------------------------------
echo '//--- errorlevel -------------------------------------------
echo %errorlevel%
echo '//------------------------------------------------------------

if not %errorlevel% equ 1 (
exit /b 1 
)