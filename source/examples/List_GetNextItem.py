"""
Example:
    How to advance to the next item in a list by providing a direction.
    The logic here applies to most scriptincg languages. However, ` % totalCount` is unneccessary in Python as it accept index greater than the length of the list.
"""

dataList = ['a','b','c','d','e']
totalCount = len(dataList)

print dataList
for curIndex in range(totalCount):
    
    print "Current Item: ", dataList[curIndex]
    
    nextIndex = (curIndex + 1) % totalCount
    print "Advance to the next item:", dataList[nextIndex]
    
    nextIndex = (curIndex - 1) % totalCount
    print "Advance to the prev item:", dataList[nextIndex]
    print ""

