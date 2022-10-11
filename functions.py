import json
import random
from datetime import datetime

import discord

import functions

EASY_TASKS = [1, 2, 3]
MEDIUM_TASKS = [4, 5, 6]
HARD_TASKS = [7, 8, 9]
last_update = "00:00"

teamNames = ["Nyan", "Yoshi", "Haruki", "Kenzo", "Momo", "Yuki",
            "Fuwafuwa", "Tadeo", "Yuuma", "Adzuki", "Taro", "Sota", "Fuku"]

class Crib:
    def __init__(self, uid, channelid=None, name="none", start=str(datetime.now()), points=0, currentEasyTask=1, currentMediumTask=4, currentHardTask=7, easyAmt=0, mediumAmt=4, hardAmt=7, completedTasks=[], end=str(datetime.now())):
        self.members = uid
        self.channelid = channelid
        self.name = name
        self.start = start
        self.points = points
        self.currentEasyTask = currentEasyTask
        self.currentMediumTask = currentMediumTask
        self.currentHardTask = currentHardTask
        self.easyAmt = easyAmt
        self.mediumAmt = mediumAmt
        self.hardAmt = hardAmt
        self.completedTasks = completedTasks
        self.end = end

    def __repr__(self):
        string = "**_" + self.name + "_**\n"
        for member in self.members:
            string += "<@" + str(member) + ">\n"
        string += "Total crib Points: " + str(self.points)
        string += "\n Mischieves managed: " + str(len(self.completedTasks))
        return string

    def new_member(self, uid):
        if len(self.members) <= 6:
            self.members.append(uid)
            return True
        else:
            return False

    def add_points(self, points):
        self.points += points
        with open("cribList.json", "r+") as f:
            data = json.load(f)
            data[self.name] += points
            f.seek(0)
            f.truncate()
            json.dump(data, f)
            return True

    def give_next(self, diff):
        if diff == 1:
            self.completedTasks.append(self.currentEasyTask)
            self.easyAmt += 1
            if self.easyAmt < 3:
                if self.currentEasyTask == 3:
                    self.currentEasyTask = 1
                else:
                    self.currentEasyTask += 1
            else:
                self.currentEasyTask = -1
            
        if diff == 2:
            self.completedTasks.append(self.currentMediumTask)
            self.mediumAmt += 1
            if self.mediumAmt < 3:
                if self.currentMediumTask == 6:
                    self.currentMediumTask = 4
                else:
                    self.currentMediumTask += 1
            else:
                self.currentMediumTask = -1
        if diff == 3:
            self.completedTasks.append(self.currentHardTask)
            self.hardAmt += 1
            if self.hardAmt < 3:
                if self.currentHardTask == 9:
                    self.currentHardTask = 7
                else:
                    self.currentHardTask += 1
            else:
                self.currentHardTask = -1

    def skip(self, diff):
        if diff == 1:
            if self.easyAmt < 3:
                if self.currentEasyTask == 3:
                    self.currentEasyTask = 1
                else:
                    self.currentEasyTask += 1
                for i in range(1,3,1):
                    wasFound = False
                    if len(self.completedTasks) == 0:
                        if self.currentEasyTask == 3:
                            self.currentEasyTask = 1
                            break
                        else:
                            self.currentEasyTask += 1
                            break

                    for k in range(len(self.completedTasks)):
                        if wasFound == False and self.currentEasyTask == self.completedTasks[k]:
                            wasFound = True
                            break
                    
                    if wasFound == True:
                        if self.currentEasyTask == 3:
                            self.currentEasyTask = 1
                        else:
                            self.currentEasyTask += 1
                    
                    # else:
                    #     if self.currentEasyTask == 3:
                    #         self.currentEasyTask = 1
                    #     else:
                    #         self.currentEasyTask += 1
                # if isFound == False:
                #     if self.currentEasyTask == 3:
                #         self.currentEasyTask = 1
                #     else:
                #         self.currentEasyTask += 1
        if diff == 2:
            if self.mediumAmt < 3:
                if self.currentMediumTask == 6:
                    self.currentMediumTask = 4
                else:
                    self.currentMediumTask += 1
                for i in range(1,3,1):
                    wasFound = False
                    if len(self.completedTasks) == 0:
                        if self.currentMediumTask == 6:
                            self.currentMediumTask = 4
                            break
                        else:
                            self.currentMediumTask += 1
                            break

                    for k in range(len(self.completedTasks)):
                        if wasFound == False and self.currentMediumTask == self.completedTasks[k]:
                            wasFound = True
                            break
                    
                    if wasFound == True:
                        if self.currentMediumTask == 6:
                            self.currentMediumTask = 4
                        else:
                            self.currentMediumTask += 1
                    
        if diff == 3:
            if self.hardAmt < 3:
                if self.currentHardTask == 9:
                    self.currentHardTask = 7
                else:
                    self.currentHardTask += 1
                for i in range(1,3,1):
                    wasFound = False
                    if len(self.completedTasks) == 0:
                        if self.currentHardTask == 9:
                            self.currentHardTask = 7
                            break
                        else:
                            self.currentHardTask += 1
                            break

                    for k in range(len(self.completedTasks)):
                        if wasFound == False and self.currentHardTask == self.completedTasks[k]:
                            wasFound = True
                            break
                    
                    if wasFound == True:
                        if self.currentHardTask == 9:
                            self.currentHardTask = 7
                        else:
                            self.currentHardTask += 1

    def lead(self):
        try:
            with open("leaderboard.json", "r") as f:
                data = json.load(f)[self.name.lower()]
                embed = discord.Embed(title="Latest leaderboards:")
                for i in range(1, len(data)):
                    embed.add_field(name=data[-i][0], value="Points collected: " + str(data[-i][1]), inline=False)
                embed.set_footer(text="Last update "+last_update)
                return embed
        except Exception as e:
            print("functions" + str(e))
            return discord.Embed(title="Leaderboard is not prepared yet. Try again later", description="We update leaderboards every 30 minutes")

    def end_game(self):
        self.end = str(datetime.now())
        return True


def register(uid):
    with open("participants.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        if uid not in data.keys():
            data.update({uid: None})
            f.seek(0)
            f.truncate()
            json.dump(data, f)
            return True
        else:
            return False

def randomTeamName():
    name = random.choice(teamNames)
    teamNames.remove(name)
    return name

def find_user(uid):
    with open("participants.json", "r") as f:
        data = json.load(f)
        if uid in data:
            return data[uid]
        else:
            return None


def find_cribname_by_channelid(cid):
    with open("cribChannels.json", "r") as f:
        data = json.load(f)
        if cid in data:
            return data[cid]
        else:
            return None


def set_guild(uid, kitten):
    with open("participants.json", "r+") as f:
        data = json.load(f)
        if kitten:
            data[uid] = kitten.lower()
        else:
            data[uid] = None
        f.seek(0)
        f.truncate()
        json.dump(data, f)


def choosestart(diff):
    if diff == 1:
        start = random.choice(EASY_TASKS)
        EASY_TASKS.remove(start)
        return start
    elif diff == 2:
        start = random.choice(MEDIUM_TASKS)
        MEDIUM_TASKS.remove(start)
        return start
    else:
        start = random.choice(HARD_TASKS)
        HARD_TASKS.remove(start)
        return start


def create_guild(kitten, uid, channelid):
    with open("cribList.json", "r+") as covens:
        data = json.load(covens)
        if kitten not in data.keys():
            with open("cribs/" + kitten.lower() + ".json", "w+") as crib:
                json.dump(Crib(name=kitten, uid=[uid], channelid=channelid, currentEasyTask=choosestart(1), easyAmt=0, mediumAmt=0, hardAmt=0, currentMediumTask=choosestart(2), currentHardTask=choosestart(3)).__dict__, crib, indent=4)
            data.update({kitten: 0})
            covens.seek(0)
            covens.truncate()
            json.dump(data, covens, indent=4)
            set_guild(uid, kitten.lower())
            with open("cribChannels.json", "r+") as f:
                data2 = json.load(f)
                data2.update({channelid: kitten})
                f.seek(0)
                f.truncate()
                json.dump(data2, f, indent=4)
            return True
        else:
            return False


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
        json.dump(data, f, indent=4)


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


def update_leaderboard():
    with open("cribList.json", "r") as f:
        data = json.load(f)
    sorted_data = sorted(data.items(), key=lambda x: x[1])
    with open("leaderboard.json", "w") as ff:
        new_data = {}
        end = len(sorted_data)
        for i in range(0, end):
            listas = []
            if i >= 2:
                listas.append(sorted_data[i - 2])
            if i >= 1:
                listas.append(sorted_data[i - 1])
            listas.append(sorted_data[i])
            if i < end - 1:
                listas.append(sorted_data[i + 1])
            if i < end - 2:
                listas.append(sorted_data[i + 2])
            new_data[sorted_data[i][0]] = listas
        json.dump(new_data, ff, indent=4)

    now = datetime.now()
    global last_update
    last_update = now.strftime("%H:%M")
    result = ""
    for i in range(1, end):
        result += "No." + str(i) + " " + sorted_data[len(sorted_data) - i][0] + " " + str(
            sorted_data[len(sorted_data) - i][1]) + "\n"
    return result


def end_game(cid):
    kitten = functions.find_covenname_by_channelid(cid)
    crib = functions.load_guild(kitten)
    result = crib.end_game()
    if result:
        functions.upload_guild(crib)
        return "You have sucessefuly completed the game"
    print(":)")

