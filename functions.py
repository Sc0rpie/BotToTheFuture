def fileRead():
    with open('testingFiles.txt') as myFile:
        text = myFile.read()
    result = text.split('$')
    return result

def startRoles():
    pass