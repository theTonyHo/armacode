@Echo OFF

del "%~dp0docset\armacodeDocset.tgz"

"C:\Program Files\7-Zip\7z.exe" a -y -ttar -so -r "%~dp0docset\armacodeDocset.tar" "%~dp0docset\armacode.docset"| "C:\Program Files\7-Zip\7z.exe" u -si "%~dp0docset\armacodeDocset.tgz"

pause