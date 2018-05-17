@ECHO OFF
REM Rhino 5
IF EXIST "C:\Program Files\Rhinoceros 5 (64-bit)\System\Rhino.exe" (
echo Starting Rhinoceros 5 to generate armacode documentation
echo Please switch to Rhino application for any prompts ...
"C:\Program Files\Rhinoceros 5 (64-bit)\System\Rhino.exe" /nosplash /runscript="!-_RunPythonScript ""%~dp0docGenerator.py"" -_Exit"
goto exit
)

REM Rhino 6

IF EXIST "C:\Program Files\Rhino 6\System\Rhino.exe" (
echo Starting Rhinoceros 6 to generate armacode documentation
echo Please switch to Rhino application for any prompts ...
"C:\Program Files\Rhino 6\System\Rhino.exe" /nosplash /runscript="!-_RunPythonScript ""%~dp0docGenerator.py"" -_Exit"
goto exit
)


:exit
