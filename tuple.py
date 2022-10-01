from functions import fileRead
from classes import *
import random
# Mission = recordtype("Mission", "missionName diff")

# missionArray = [0]*100
# missionDesc = ["null"]
# missionDiff = [0]

# X = fileRead()
# i = 0


# while i < len(X)-1:
#     missionDesc.append(X[i].strip('\n'))
#     diff = X[i+1]
#     missionDiff.append(diff)
#     i+=2

# print(missionDesc)
# print(missionDiff)

MaxN = 20
MaxT = 10
Missions = [Mission() for i in range(MaxN)]
i = 0
X = fileRead()
for seg in Missions:
    seg.desc = X[i]
    seg.diff = X[i+1]
    i += 2
    
Teams = [Team() for i in range(MaxT)]
y = 0
for seg in Teams:
    seg.easyMissions = random.sample(range(10), 5)
    seg.mediumMissions = random.sample(range(10), 5)
    seg.hardMissions = random.sample(range(10), 5)


print(Teams[0].easyMissions)
print(Teams[0].mediumMissions)
print(Teams[0].hardMissions)