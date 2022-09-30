def fileRead():
    with open('testingFiles.txt') as myFile:
        text = myFile.read()
    result = text.split('$')
    return result
    # for i in range(len(result)):
    #     print(result[i])
