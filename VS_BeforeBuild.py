"""
This routine is executed on Before Build every time user build a Visual Studio project.

TODO:
    CHM web template with logo.
    Custom Icon Strip for CHM Files.

Author: Tony Ho @ AR-MA 2018
"""

from subprocess import call
import os
import fnmatch


def Run():
    GenerateDocsInRhino()
    GenerateHTMLHelp()
    ChangeCHMIconToBooks()
    GenerateHTMLHelpCHM()
    return True

docDirectory = os.path.dirname(__file__)

def GenerateDocsInRhino():
    print "Generating documentation via Rhino"
    print "---------------------------------------"
    # How to compile a chm file in Python?
    # ---------------------------------
    command = os.path.join(docDirectory, "generateDocsInRhino.bat")
    # print command
    rc = call(command, cwd=docDirectory)

def GenerateHTMLHelp():
    print "Building HTML Help package"
    print "---------------------------------------"
    # How to compile a chm file in Python?
    # ---------------------------------
    command = os.path.join(docDirectory, "make-htmlhelp.bat")
    # print command
    rc = call(command, cwd=docDirectory)

def GenerateHTMLHelpCHM():
    print "Compiling CHM file from HTML Help package"
    print "---------------------------------------"
    # How to compile a chm file in Python?
    # ---------------------------------
    command = os.path.join(docDirectory, "make-htmlhelpCHM.bat")
    # print command
    rc = call(command, cwd=docDirectory)

def ChangeCHMIconToBooks():
    """Change CHM icon to book icon.
    Read HHC file and delete the line <param name="ImageType" value="Folder">
    """
    filename = os.path.join(docDirectory, "build\\htmlhelp\\armacode.hhc")

    #Open Read the file, remove all lines starting with _static
    with open(filename, "r+") as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            rc = fnmatch.fnmatch(line, "*<param name=\"ImageType\" value=\"Folder\">")
            if rc:
                lines[i] = ""

        newContent = "".join(lines) #all lines already have return characters
        f.seek(0)
        f.write(newContent)
    return rc

if __name__ == "__main__":
    pass