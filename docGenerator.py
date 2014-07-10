import sys
sys.path.insert(0, "C:\\Python27\\lib\\site-packages")

import sphinxcontrib.napoleon
import inspect
import math
import armacode
import os

def DocStringFromGoogle(docstring):
    config = sphinxcontrib.napoleon.Config(napoleon_use_param=True, napoleon_use_rtype=True)
    restDocString = sphinxcontrib.napoleon.GoogleDocstring(docstring, config)
    return restDocString

def MemberDoc(_object):
    memberName = _object.__name__
    docString = inspect.getdoc(_object) 
    if not docString:
        docString = "Undocumented"
    docString = inspect.cleandoc(docString)
    restDocString = DocStringFromGoogle(docString)
    
    return restDocString

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

def DescribeMethod(_object):
    global colonSpacing
    # Get Values
    memberName = _object.__name__
    
    docString = inspect.getdoc(_object) 
    if not docString:
        docString = "Undocumented"
    
    docString = inspect.cleandoc(docString)
    
    indentedDocString = StringIndent(docString, 4)
    functionSyntax = inspect.formatargspec(*inspect.getargspec(_object))
    functionSyntax = StringIndent(memberName+functionSyntax, 4)
    # Create dictionary of values
    fieldValues = {}
    fieldValues["memberName"] = memberName
    underLine = "-" * len(memberName)
    fieldValues["underLine"] = underLine
    fieldValues["functionSyntax"] = functionSyntax
    fieldValues["docString"] = docString
    fieldValues["indentedDocString"] = indentedDocString
    
    # Create message format template
    message = []
    message.append(" ")
    message.append("{memberName}")
    message.append("{underLine}")
    message.append(" ")
    message.append("{functionSyntax}")
    message.append(" ")
    message.append("{docString}")
    message = str.join("\n", message)
    
    # Evaluate the message with corresponding fields
    message = message.format(**fieldValues)
    
    return message

def DescribeObject(_objectName, _object):
    
    if inspect.isbuiltin(_object) or inspect.isfunction(_object) or inspect.ismethod(_object):
        message = DescribeMethod(_object)
        return message
    else:
        #Property
        return None

def ProcessMembers(dataDict, writeToDirectory=None, sortMembers=True, indexFile=False):
    
    memberData = dataDict
    allMemberNames = dataDict.keys()
    if sortMembers:
        allMemberNames.sort()
    allStrings = []
    
    for memberName in allMemberNames:
        member = memberData[memberName]
        
        resultString = DescribeMember(member)
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


def DescribeMember(member):
    memberName = member.__name__
    
    restDocstring = MemberDoc(member)
    message = []
    message.append(memberName)
    message.append("-" * len(memberName))
    message.append(restDocstring)
    resultMessage = str.join("\n", message)
    return resultMessage

def InspectObject(_object=None):
    # Set defaul spacing
    global colonSpacing
    
    classes = {}
    imports = {}
    modules = {}
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
                methods[memberName] = member
            else:
                properties[memberName] = member
        except:
            protected[memberName] = member
        
        if memberName:
            # Automatically adjust spacing based on the required characters
            if len(memberName) > colonSpacing:
                colonSpacing = len(memberName)
    
    allData = {}
    allData["modules"] = modules
    allData["methods"] = methods
    allData["properties"] = properties
    allData["protected"] = protected
    
    return allData
colonSpacing = 10

def main():
    moduleToDocument = armacode
    moduleName = moduleToDocument.__name__
    sortMembers = True
    
    moduleDirectory = moduleToDocument.__path__
    #docDirectory = moduleDirectory[0] + "\\source" + "\\" + moduleName
    docDirectory = "source" + "\\" + moduleName
    
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
    
    # Methods
    proceed = True
    if proceed:
        ProcessMembers(allData["methods"], docDirectory)


if __name__ == "__main__":
    main()