import random
import json

teamNames = ["Nyan", "Yoshi", "Haruki", "Kenzo", "Momo", "Yuki",
            "Fuwafuwa", "Tadeo", "Yuuma", "Adzuki", "Taro", "Sota", "Fuku"]

i = 0

class Crib:
    pass

def fileRead():
    with open('testingFiles.txt') as myFile:
        text = myFile.read()
    result = text.split('$')
    return result

def register(uid):
    with open ("participants.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        if uid not in data.keys():
            data.update({uid: None})
            f.seek(0)
            f.truncate()
            json.dump(data, f)
            return True
        else:
            return False

def find_user(uid):
    with open("participants.json", "r") as f:
        data = json.load(f)
        if uid in data:
            return data[uid]
        else:
            return None

def load_guild(guildname):
    with open("cribs/" + guildname.lower() + ".json", "r") as f:
        lst = json.load(f).values()
        data = Crib(*lst)
        return data

def upload_guild(guild):
    with open("cribs/" + guild.name.lower() + ".json", "r+") as f:
        data = guild.__dict__
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent = 4)

def set_guild(uid, cribname):
    with open("participants.json", "r+") as f:
        data = json.load(f)
        if cribname:
            data[uid] = cribname.lower()
        else:
            data[uid] = None
        f.seek(0)
        f.truncate()
        json.dump(data, f)

def join(uid, guildname):
    try:
        guild = load_guild(guildname)
        if not guild:
            return False
        memb = guild.new_member(uid)
        if memb:
            set_guild(uid, guildname)
            upload_guild(guild)
        return True, memb
    except Exception as e:
        print(str(e) + " while joining guild")
        return False, True

def randomTeamName():
    name = random.choice(teamNames)
    teamNames.remove(name)
    return name