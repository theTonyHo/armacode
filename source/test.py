import armacode

with open ("..\\VERSION.txt", "r") as myfile:
    data = []
    data.append(myfile.readline().strip("\n"))
    release = data[0]
    version = str.split(data[0])[0]