"""
Generate Documentation for armacode to ReadTheDocs.
Since this requires Rhino libraries, sphinx can not parse the module. This is a work around to export all documentation to .rst files.

Dependencies:
    - Python27. Remember to set PATH Environment System variables
    - pip
    - Sphinx
    - Sphinxcontrib.napoleon
    - pockets

"""

import sys
sys.path.insert(0, "C:\\Python27\\lib\\site-packages")

import sphinxcontrib.napoleon as sphinxNP
import inspect
import math
import armacode
import os
import ast
import shutil

#import sphinx.ext.napoleon #This does not work in IronPython ?

def StringToFile(string, fileName):
    
    dirName = os.path.dirname(fileName)
    
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    
    f = open(fileName,'w')
    f.write(string) # python will convert \n to os.linesep
    f.close() # you can omit in most cases as the destructor will call if
    return fileName

def StringIndent(multilineString, indent=4, delimiter="\n"):
    indentString = ""
    if isinstance(indent, int):
        indentString = " " * indent
    elif isinstance(indent, str):
        indentString = indent
    
    resultStrings = []
    strLines = multilineString.split(delimiter)
    
    if len(strLines) == 1:
        resultStrings = "{}{}".format(indentString, strLines[0])
    if len(strLines) > 1:
        for item in strLines:
            resultStrings.append("{}{}".format(indentString, item))
        resultStrings = str.join(delimiter, resultStrings)
    return resultStrings

def DocStringFromGoogle(docstring):
    config = sphinxNP.Config(napoleon_use_param=True, napoleon_use_rtype=True)
    restDocString = sphinxNP.GoogleDocstring(docstring, config)
    return restDocString

def FileDoc(filename):
    """
    Return the restructuredText docstring in a python file
    """
    file_contents = None
    with open(filename) as f:
        file_contents = f.read()
        
    
    try:
        mod = ast.parse(file_contents)
        
    except:
        return
    
    docString = ast.get_docstring(mod)
    if docString:
        docString = inspect.cleandoc(docString)
        restDocString = DocStringFromGoogle(docString)
        return restDocString

def MethodSyntax(_object):
    """
    Return the call syntax for a method member.
    """
    memberName = _object.__name__
    functionSyntax = inspect.formatargspec(*inspect.getargspec(_object))
    resultString = functionSyntax
    return resultString
    
def MethodDoc(_object):
    """
    Return the restructuredText docstring for a method member.
    """
    memberName = _object.__name__
    docString = inspect.getdoc(_object) 
    if not docString:
        docString = "Undocumented"
    docString = inspect.cleandoc(docString)
    restDocString = DocStringFromGoogle(docString)
    
    return restDocString

def DescribeMethod(_object, customName=None):
    """
    Return the string describing the method.
    """
    # Get Values
    memberName = _object.__name__
    if customName:
        memberName = customName
    methodSyntax = MethodSyntax(_object)
    
    if methodSyntax:
        methodSyntax = "\n.. py:Function:: {}{}\n\n".format(memberName, methodSyntax)
    
    restDocstring = MethodDoc(_object)
    
    message = []
    message.append(memberName)
    message.append("-" * len(memberName))
    message.append(methodSyntax)
    message.append(restDocstring)
    
    resultMessage = str.join("\n", message)
    
    return resultMessage

def DescribeTool(filename, customName=None):
    """
    Return the string describing the method.
    """
    # Get Values
    
    fpath, fname = os.path.split(filename)
    memberName = fname[:-3]
    
    restDocstring = FileDoc(filename)
    
    message = []
    
    # Indexing
    message.append(".. index:: {} (Tool)\n".format(memberName))
    # Reference Label
    message.append(".. _tools.{}:\n".format(str.lower(memberName)))
    
    if not restDocstring:
        restDocstring = "Undocumented."
    
    message.append(memberName)
    message.append("-" * len(memberName))
    
    message.append(restDocstring)
    
    resultMessage = str.join("\n", message)
    
    return resultMessage

def DescribeCommand(filename, customName=None):
    """
    Return the string describing the method.
    """
    # Get Values
    
    fpath, fname = os.path.split(filename)
    memberName = fname[:-7]
    
    restDocstring = FileDoc(filename)
    
    message = []
    
    # Indexing
    message.append(".. index:: {} (Command)\n".format(memberName))
    # Reference label
    message.append(".. _{}_cmd:\n".format(str.lower(memberName)))
    
    if not restDocstring:
        restDocstring = "Undocumented."
    
    message.append(memberName)
    message.append("-" * len(memberName))
    message.append(restDocstring)
    
    resultMessage = str.join("\n", message)
    
    return resultMessage

def DescribeGHUserObject(member, customName=None):
    """
    Return the string describing the GH User Object.
    """
    # Get Values
    
    fpath, fname = os.path.split(filename)
    memberName = fname[:-7]
    
    restDocstring = FileDoc(filename)
    
    message = []
    
    # Indexing
    message.append(".. index:: {} (GH)\n".format(memberName))
    # Reference label
    message.append(".. _{}_gh:\n".format(str.lower(memberName)))
    
    if not restDocstring:
        restDocstring = "Undocumented."
    
    message.append(memberName)
    message.append("-" * len(memberName))
    message.append(restDocstring)
    
    resultMessage = str.join("\n", message)
    
    return resultMessage

def DescribeObject(_objectName, _object):
    
    if inspect.isbuiltin(_object) or inspect.isfunction(_object) or inspect.ismethod(_object):
        message = DescribeMethod(_object)
        return message
    else:
        #Property
        return None

def ProcessMethods(dataDict, writeToDirectory=None, sortMembers=True, indexFile=False, useCustomNames=False):
    
    if writeToDirectory:
        shutil.rmtree(writeToDirectory)
        
    memberData = dataDict
    allMemberNames = dataDict.keys()
    if sortMembers:
        allMemberNames.sort()
    allStrings = []
    
    for memberName in allMemberNames:
        member = memberData[memberName]
        if useCustomNames:
            useCustomNames = memberName
        resultString = DescribeMethod(member, useCustomNames)
        
        if writeToDirectory:
            if isinstance(writeToDirectory, str):
                fileName = "{}\\{}.rst".format(writeToDirectory, memberName)
            else:
                fileName = "{}.rst".format(memberName)
            rc = StringToFile(resultString, fileName)
            
    if writeToDirectory and indexFile:
        
        indexFilename = "{}\\index.rst".format(writeToDirectory)
        indexContent = CombineFiles(allMemberNames)
        rc = StringToFile(indexContent, indexFilename)
    print "Processed {} Methods !".format(len(allMemberNames))

def ProcessCommands(dirPath, writeToDirectory=None, sortMembers=True, indexFile=False, useCustomNames=False):
    
    if writeToDirectory:
        shutil.rmtree(writeToDirectory)
    #Get filenames of all tools.
    fileList = []
    for (dirpath, dirname, filenames) in os.walk(dirPath):
        for fname in filenames:
            if fname.endswith("_cmd.py") and not fname.startswith("_"):
                fPath = dirpath+"\\"+fname
                fileList.append(fPath)
    if sortMembers:
        fileList.sort()
    for item in fileList:
        resultString = DescribeCommand(item)
        fpath, fname = os.path.split(item)
        memberName = fname[:-7]
        
        if writeToDirectory:
            if isinstance(writeToDirectory, str):
                fileName = "{}\\{}.rst".format(writeToDirectory, memberName)
            else:
                fileName = "{}.rst".format(memberName)
            rc = StringToFile(resultString, fileName)
            
    if writeToDirectory and indexFile:
        
        indexFilename = "{}\\index.rst".format(writeToDirectory)
        indexContent = CombineFiles(allMemberNames)
        rc = StringToFile(indexContent, indexFilename)
    print "Processed {} Commands !".format(len(fileList))

def ProcessTools(dirPath, writeToDirectory=None, sortMembers=True, indexFile=False, useCustomNames=False):
    
    if writeToDirectory:
        shutil.rmtree(writeToDirectory)
    #Get filenames of all tools.
    fileList = []
    for (dirpath, dirname, filenames) in os.walk(dirPath):
        for fname in filenames:
            if fname.endswith(".py") and not fname.startswith("_"):
                fPath = dirpath+"\\"+fname
                fileList.append(fPath)
    if sortMembers:
        fileList.sort()
    for item in fileList:
        resultString = DescribeTool(item)
        fpath, fname = os.path.split(item)
        memberName, ext = os.path.splitext(fname)
        
        if writeToDirectory:
            
            if isinstance(writeToDirectory, str):
                fileName = "{}\\{}.rst".format(writeToDirectory, memberName)
            else:
                fileName = "{}.rst".format(memberName)
            rc = StringToFile(resultString, fileName)
            
    if writeToDirectory and indexFile:
        
        indexFilename = "{}\\index.rst".format(writeToDirectory)
        indexContent = CombineFiles(allMemberNames)
        rc = StringToFile(indexContent, indexFilename)
    print "Processed {} Tools !".format(len(fileList))

def ProcessGHUserObjects(category="AR-MA", writeToDirectory=None, sortMembers=True, indexFile=False, useCustomNames=False):
    
    import Grasshopper
    
    objs = list(Grasshopper.GH_InstanceServer.ComponentServer.ObjectProxies)
    
    if sortMembers:
        objs.sort(key=lambda obj: obj.Desc.Name)
    
    obj = objs[0]
    
    allMemberNames = []
    
    iconDirectory = writeToDirectory + "\\icon"
    
    if writeToDirectory:
        shutil.rmtree(writeToDirectory)
    if not os.path.isdir(iconDirectory):
        os.mkdir(iconDirectory)
    for obj in objs:
        catName = obj.Desc.Category
        if not category in catName:
            continue
        
        memberName = obj.Desc.Name
        subCatName = obj.Desc.SubCategory
        description = obj.Desc.InstanceDescription
        
        fileName = memberName
        #fileName = str.replace(memberName, "[OBSOLETE]", "_OBSOLETE")
        
        fileName = str.replace(fileName, "|", "-")
        fileName = str.replace(fileName, "/", "-")
        fileName = str.replace(fileName, ":", "-")
        fileName = str.replace(fileName, "*", "-")
        
        fileName = fileName.replace(" ", "_")
        
        iconFileName = "{}.png".format(fileName)
        iconFilePath = "{}\\icon\\{}".format(writeToDirectory, iconFileName)
        docString = description
        if not docString:
            docString = "Undocumented"
        docString = inspect.cleandoc(docString)
        restDocString = DocStringFromGoogle(docString)
        
        message = []
        # Indexing
        message.append(".. index:: {} (GH)\n".format(memberName))
        # Reference label
        message.append(".. _{}_gh:\n".format(str.lower(memberName)))
        
        if not restDocString:
            restDocString = "Undocumented."
        
        heading = memberName + " |icon| "
        message.append(memberName + " |icon| ")
        message.append("-" * len(heading))
        message.append("")
        message.append(restDocString)
        
        message.append("\n.. |icon| image:: icon/{}".format(iconFileName))
        resultString = str.join("\n", message)
        
        if writeToDirectory:
            try:
                obj.Icon.Save(iconFilePath)
            except:
                print "ERROR: {} could not be extracted".format(iconFilePath)
                
            if isinstance(writeToDirectory, str):
                fileName = "{}\\{}.rst".format(writeToDirectory, fileName)
            else:
                fileName = "{}.rst".format(memberName)
            rc = StringToFile(resultString, fileName)
            
        allMemberNames.append(memberName)
        
    if writeToDirectory and indexFile:
        
        indexFilename = "{}\\index.rst".format(writeToDirectory)
        indexContent = CombineFiles(allMemberNames)
        rc = StringToFile(indexContent, indexFilename)
    print "Processed {} GH User Objects !".format(len(allMemberNames))
        

def Toctree(includePaths, maxdepth=2):
    
    toctreeString = []
    toctreeString.append("")
    toctreeString.append(".. toctree::")
    toctreeString.append("   :maxdepth: {}".format(maxdepth))
    
    #toctreeString.append("   :numbered:")
    #toctreeString.append("   :titlesonly:")
    #toctreeString.append("   :glob:")
    #toctreeString.append("   :hidden:")
    
    toctreeString.append(" ")
    
    for item in includePaths:
        toctreeString.append("   {}.rst".format(item))
    resultString = str.join("\n", toctreeString)
    return resultString

def CombineFiles(includePaths):
    content = []
    for item in includePaths:
        content.append(".. include:: {}.rst".format(item))
        #content.append("   :end-before: :param")
    resultString = str.join("\n", content)
    return resultString


def InspectObject(_object=None, ):
    # Set defaul spacing
    global colonSpacing
    
    classes = {}
    imports = {}
    modules = {}
    specialModules = {}
    methods = {}
    properties = {}
    protected = {}
    
    memberData = inspect.getmembers(_object)
    
    for memberName, member in memberData:
        #print "{:>30}, {}".format(memberName,type(member))
        try:
            if inspect.isclass(member):
                classes[memberName] = member
            if inspect.ismodule(member):
                modules[memberName] = member
            elif inspect.isbuiltin(member) or inspect.isfunction(member) or inspect.ismethod(member):
                if memberName.startswith("_"):
                    specialModules[memberName] = member
                else:
                    methods[memberName] = member
            else:
                properties[memberName] = member
        except:
            protected[memberName] = member
        
    
    allData = {}
    allData["modules"] = modules
    allData["methods"] = methods
    allData["specials"] = specialModules
    allData["properties"] = properties
    allData["protected"] = protected
    
    return allData

def main():
    moduleToDocument = armacode
    moduleName = moduleToDocument.__name__
    sortMembers = True
    
    moduleDirectory = moduleToDocument.__path__[0]
    #docDirectory = moduleDirectory[0] + "\\source" + "\\" + moduleName
    
    docDirectory = os.path.dirname(__file__)
    print docDirectory
    # Documentation director for all generated docs.
    moduleDocDirectory = "source" + "\\" + moduleName
    methodDocDirectory = moduleDocDirectory + "\\libraries"
    # Reference directory for methods to include in index but not to list out.
    refDirectory = moduleDocDirectory + "\\" + "reference"
    
    # Commands
    commandPath = moduleDirectory + "\\plug-in\\AR-MA {4dbb1598-76ef-4560-8b04-fd01de706e43}\\dev"
    commandDocDirectory = "source" + "\\armacode\\plug-ins\\commands"
    
    # Tools
    toolPath = moduleDirectory + "\\tools"
    toolDocDirectory = "source" + "\\armacode\\tools"
    
    # Grasshopper UserObjects
    ghDocDirectory = "source" + "\\armacode\\ghuserobjects"
    
    includeModules = ["classes", ""]
    
    # Go through module
    # Ger list of methods, modules, properties
    # ##Methods
    # for each member of methods
    # Get docstring for each member
    # Convert to reSText
    # Save as a .rst file with the hierarchy as name
    # armacode/AddLayer.rst
    
    allData = InspectObject(armacode)
    
    #Additional methods to include in index
    additionalMethods = {   "armacode.config.SetOption" : armacode.config.SetOption,
                            "armacode.config.GetOption" : armacode.config.GetOption,
                            "armacode.config.Save" : armacode.config.Save
                        }
    
    def get_class_that_defined_method(meth):
        for cls in inspect.getmro(meth.im_class):
            if meth.__name__ in cls.__dict__: 
                return cls
        return None
    
    # Methods
    proceed = True
    if proceed:
        
        
        ProcessMethods(allData["methods"], methodDocDirectory)
        ProcessMethods(additionalMethods, refDirectory, useCustomNames=True)
        
        ProcessCommands(commandPath, commandDocDirectory)
        ProcessTools(toolPath, toolDocDirectory)
        ProcessGHUserObjects("AR-MA", ghDocDirectory)
        GenerateDocsetFeed()
        GenerateVersionFile()
        print "Document generated for armacode"
    

def GenerateDocsetFeed():
    feedFilePath = "feed\\armacode.xml"
    feedTemplate = ["<entry>",
                    "    <version>{versionNumber}</version>",
                    "    <url>https://github.com/theTonyHo/armacode/raw/master/docset/armacode.tgz</url>",
                    "</entry>"]
    feedTemplate = str.join("\n", feedTemplate)
    feedContent = feedTemplate.format(versionNumber=armacode.__Version__)
    
    with open(feedFilePath, 'w') as f:
        f.write(feedContent)
    print "Docset Feed Generated"

def GenerateVersionFile():
    versionFilePath = os.getcwd()+"\\VERSION"
    
    with open(versionFilePath, 'w') as f:
        f.write(armacode.__Version__)
        f.write("\n")
        f.write(armacode.__ReleaseDate__)
    
    print "Version File Generated"



if __name__ == "__main__":
    main()