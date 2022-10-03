import random

teamNames = ["Nyan", "Yoshi", "Haruki", "Kenzo", "Momo", "Yuki",
            "Fuwafuwa", "Tadeo", "Yuuma", "Adzuki", "Taro", "Sota", "Fuku"]

i = 0

def fileRead():
    with open('testingFiles.txt') as myFile:
        text = myFile.read()
    result = text.split('$')
    return result

def randomTeamName():
    # global i
    # name = teamNames[i]
    # i += 1
    name = random.choice(teamNames)
    teamNames.remove(name)
    return name