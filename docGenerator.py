import sys
sys.path.insert(0, "C:\\Python27\\lib\\site-packages")

import sphinxcontrib.napoleon
import inspect
import math
import armacode
import os
import ast

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
    config = sphinxcontrib.napoleon.Config(napoleon_use_param=True, napoleon_use_rtype=True)
    restDocString = sphinxcontrib.napoleon.GoogleDocstring(docstring, config)
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

def DescribeObject(_objectName, _object):
    
    if inspect.isbuiltin(_object) or inspect.isfunction(_object) or inspect.ismethod(_object):
        message = DescribeMethod(_object)
        return message
    else:
        #Property
        return None

def ProcessMethods(dataDict, writeToDirectory=None, sortMembers=True, indexFile=False, useCustomNames=False):
    
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
    
    moduleDirectory = moduleToDocument.__path__
    #docDirectory = moduleDirectory[0] + "\\source" + "\\" + moduleName
    
    # Documentation director for all generated docs.
    docDirectory = "source" + "\\" + moduleName
    
    # Reference directory for methods to include in index but not to list out.
    refDirectory = docDirectory + "\\" + "reference"
    
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
        ProcessMethods(allData["methods"], docDirectory)
        ProcessMethods(additionalMethods, refDirectory, useCustomNames=True)
        print "Document generated for armacode Methods"

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
    versionFilePath = "VERSION.txt"
    
    with open(versionFilePath, 'w') as f:
        f.write(armacode.__Version__)
        f.write("\n")
        f.write(armacode.__ReleaseDate__)
    
    print "Version File Generated"

if __name__ == "__main__":
    #main()
    GenerateDocsetFeed()
    GenerateVersionFile()
    