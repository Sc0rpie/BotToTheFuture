import json
import random
from datetime import datetime

import discord

import functions

# Task List
EASY_TASKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]
MEDIUM_TASKS = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
HARD_TASKS = [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]
last_update = "00:00"

# Crib List (gets chosen randomly and deleted from list when used until next bot startup)
teamNames = ["Nyan", "Yoshi", "Haruki", "Kenzo", "Momo", "Yuki",
            "Fuwafuwa", "Tadeo", "Yuuma", "Adzuki", "Taro", "Sota", "Fuku",
            "Akemi", "Akiko", "Akira", "Aiko", "Airi", "Asami", "Asuka", "Ayame",
            "Ayano", "Ceiko", "Dai", "Chika", "Chiyo", "Chiyoko", "Emi", "Emiko", "Eri", "Etsuko",
            "Fumiko", "Hana", "Hanako", "Haru", "Haruko", "Haruna", "Hideko", "Hikari", "Hina", "Hisako", "Hiro",
            "Hiroko", "Hiromi", "Daiki", "Daisuke", "Hoshi", "Hoshiko",
            "Hotaru", "Izumi", "Kamiko", "Katsumi", "Kazuki", "Eiji",
            "Keiko", "Kiko", "Kimi", "Fumio", "Kiyomi", "Kumiko",
            "Kyo", "Kyoko", "Madoka", "Mai", "Maki", "Maiko", "Makoto",
            "Mami", "Mana", "Manami", "Mao", "Masa", "Ryoichi", "Mariko", "Mayumi", "Midori", "Mi", "Michi", 
            "Miku", "Mio", "Miwa", "Miyako", "Moriko", "Nana", "Nao", "Noriko", "Ren", "Rina", "Rika", "Ryoko",
            "Sachiro", "Saki", "Sakura", "Saki", "Satoko", "Satomi", "Shinji", "Shiori", "Shizuka", "Sora", "Sora",
            "Sora", "Sumiko", "Takara", "Tamiko", "Tekuro", "Tashiko", "Umeko", "Yasu", "Yako", "Yoshie",
            "Yua", "Yuina", "Yuka", "Yukari", "Yuri", "Yuuno", "Sora", "Sasumo", "Yuji", "Carla", "Artemis", "Chi", "Korin",
            "Molly", "Luna", "Kuro", "Lin", "Yubaba", "Zeniba", "Aogaeru", "Kashira", "Shikigami", "Kasuga"]

# Crib class (data that is going to be saved in a json file)
class Crib:
    def __init__(self, uid, channelid=None, name="none", start=str(datetime.now()), points=0, currentEasyTask=1, currentMediumTask=62, currentHardTask=110, easyAmt=0, mediumAmt=0, hardAmt=0, completedTasks=[], end=str(datetime.now())):
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

    # Checks if the crib is full
    def new_member(self, uid):
        if len(self.members) < 6:                       # Limit was set to 6
            self.members.append(uid)
            return True
        else:
            return False

    # Adds points to the crib json file
    def add_points(self, points):
        self.points += int(points)
        with open("cribList.json", "r+") as f:
            data = json.load(f)
            data[self.name] += points
            f.seek(0)
            f.truncate()
            json.dump(data, f)
            return True

    # Next task function (gets called when a task is completed). Checks task id to see which is the next one
    # and updates the json file. If all tasks are completed, current task is set to -1
    def give_next(self, diff):
        if diff == 1:                                               # Easy
            self.completedTasks.append(self.currentEasyTask)
            self.easyAmt += 1
            if self.easyAmt < 61:
                if self.currentEasyTask == 61:
                    self.currentEasyTask = 1
                else:
                    self.currentEasyTask += 1
            else:
                self.currentEasyTask = -1
            
        if diff == 2:                                               # Medium
            self.completedTasks.append(self.currentMediumTask)
            self.mediumAmt += 1
            if self.mediumAmt < 48:
                if self.currentMediumTask == 109:
                    self.currentMediumTask = 62
                else:
                    self.currentMediumTask += 1
            else:
                self.currentMediumTask = -1

        if diff == 3:                                               # Hard
            self.completedTasks.append(self.currentHardTask)
            self.hardAmt += 1
            if self.hardAmt < 23:
                if self.currentHardTask == 132:
                    self.currentHardTask = 110
                else:
                    self.currentHardTask += 1
            else:
                self.currentHardTask = -1

    # Skip task function (gets called when a task is skipped). Checks task id to see which is the next one
    def skip(self, diff):
        # Not exactly sure how this boolean works because I didn't comment it but it works so I'm not touching it
        # The following function is for skipping id's. completeZero was added to fix a bug where the bot would skip
        # more id's than it should have (wasFound is also used for that)
        # Code is the same for all difficulties (easy, medium, hard). Only difference is the task id's
        completeZero = False
        if diff == 1:
            if self.easyAmt < 61:
                if len(self.completedTasks) == 0:
                    if self.currentEasyTask == 61:
                        self.currentEasyTask = 1
                        completeZero = True
                    else:
                        self.currentEasyTask += 1

                if completeZero == False:
                    if self.currentEasyTask == 61:
                        self.currentEasyTask = 1
                    else:
                        self.currentEasyTask += 1
                for i in range(1,61,1):
                    wasFound = False
                    
                    
                    for k in range(len(self.completedTasks)):
                        if wasFound == False and self.currentEasyTask == self.completedTasks[k]:
                            wasFound = True
                            break
                    
                    if wasFound == True:
                        if self.currentEasyTask == 61:
                            self.currentEasyTask = 1
                        else:
                            self.currentEasyTask += 1
                    else:
                        break
                    
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
        
        # This checks medium difficulty tasks
        if diff == 2:
            if self.mediumAmt < 48:
                if self.currentMediumTask == 109:
                    self.currentMediumTask = 62
                else:
                    self.currentMediumTask += 1
                for i in range(1,48,1):
                    wasFound = False
                    if len(self.completedTasks) == 0:
                        if self.currentMediumTask == 109:
                            self.currentMediumTask = 62
                            break
                        else:
                            self.currentMediumTask += 1
                            break

                    for k in range(len(self.completedTasks)):
                        if wasFound == False and self.currentMediumTask == self.completedTasks[k]:
                            wasFound = True
                            break
                    
                    if wasFound == True:
                        if self.currentMediumTask == 109:
                            self.currentMediumTask = 62
                        else:
                            self.currentMediumTask += 1
                    else:
                        break
        
        # This checks hard difficulty tasks
        if diff == 3:
            if self.hardAmt < 23:
                if self.currentHardTask == 132:
                    self.currentHardTask = 110
                else:
                    self.currentHardTask += 1
                for i in range(1,23,1):
                    wasFound = False
                    if len(self.completedTasks) == 0:
                        if self.currentHardTask == 132:
                            self.currentHardTask = 110
                            break
                        else:
                            self.currentHardTask += 1
                            break

                    for k in range(len(self.completedTasks)):
                        if wasFound == False and self.currentHardTask == self.completedTasks[k]:
                            wasFound = True
                            break
                    
                    if wasFound == True:
                        if self.currentHardTask == 132:
                            self.currentHardTask = 110
                        else:
                            self.currentHardTask += 1
                    else:
                        break

    # This was made for the leaderboard command. It returns a list of all the tasks that have been completed
    # Don't think it was used anywhere except the admin channel
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

    # This functions ends the game. It saves the time the game ended and returns True
    def end_game(self):
        self.end = str(datetime.now())
        return True

# This function registers participants into a json file
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

# Gets a random team name from a list declared at the top of the file
def randomTeamName():
    name = random.choice(teamNames)
    teamNames.remove(name)
    return name

# This is used to find participants in the json file (get their information)
def find_user(uid):
    with open("participants.json", "r") as f:
        data = json.load(f)
        if uid in data:
            return data[uid]
        else:
            return None

# Searches for a channel in the json file
def find_cribname_by_channelid(cid):
    with open("cribChannels.json", "r") as f:
        data = json.load(f)
        if cid in data:
            return data[cid]
        else:
            return None

# This function is used to get the team name of a participant
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

# Randomizes the starting task for each difficulty
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
        # HARD_TASKS.remove(start)
        return start

# This function is used to create a new team
async def create_guild(kitten, uid, channelid):
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

# This function is used to load a team from the json file
def load_guild(guildname):
    with open("cribs/" + guildname.lower() + ".json", "r") as f:
        lst = json.load(f).values()
        data = Crib(*lst)
        return data

# This function is used to upload a team to the json file
def upload_guild(guild):
    with open("cribs/" + guild.name.lower() + ".json", "r+") as f:
        data = guild.__dict__
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)

# Join function
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

# This function is used to update the leaderboard
# Just json shinanigans
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

# Finish game for a crib. Goes unused
def end_game(cid):
    kitten = functions.find_covenname_by_channelid(cid)
    crib = functions.load_guild(kitten)
    result = crib.end_game()
    if result:
        functions.upload_guild(crib)
        return "You have sucessefuly completed the game"
    print(":)")

