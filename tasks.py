import discord
import json
import functions


class Task:
    lead: object

    def __init__(self, id, name, diff, person, task, reward):
        self.id = id
        self.name = name
        self.diff = diff
        self.person = person
        self.task = task
        self.reward = reward


task_dict = {
    Task(1, "Mission objective: Vytenis", "1", 0,
         "Komandos atstovas turi paglostyti Vytenio galvą", 1),
    Task(2, "Mission objective: Vytenis", "1", 0,
         "Mystery box?????", 1),
    Task(3, "Mission objective: Gabrielė D.", "1", 0,
         "Dviejų lyčių atstovai apsikeičia rūbais", 1),
    Task(4, "Mission objective: Vytenis", "2", 0,
         "Parodykit Vyteniui įdomų daiktą", 3),
    Task(5, "Mission objective: Vytenis", "2", 0,
         "Laimeti stalo futbolo žaidimą prieš Vytenį", 3),
    Task(6, "Mission objective: Vytenis", "2", 0,
         "Komandiškai išbūti kėdute 2 minutes", 3),
    Task(7, "Mission objective: Vytenis", "3", 0,
         "Nugalėk Vytenį Tetris žaidime", 5),
    Task(8, "Mission objective: Gabrielė D.", "3", 0,
         "Suvalgyti 4 gaidelius per minutę neužsigeriant", 5),
    Task(9, "Mission objective: Gabrielė D.", "3", 0,
         "Išsiaiškinkit mystery kodą", 5),
}

org_dict = {
    "1":
        {
            "tid": 267341036039176193,
            "name": "The High Priestess",
            "points": 30
        },
    "2":
        {
            "tid": 267341036039176193,
            "name": "The Chariot",
            "points": 10
        },
    "3":
        {
            "tid": 267341036039176193,
            "name": "The Star",
            "points": 30
        },
    "4":
        {
            "tid": 168687487743557632,
            "name": "The Emperor",
            "points": 20
        },
    "5":
        {
            "tid": 168687487743557632,
            "name": "Pentacles",
            "points": 30
        },
    "6":
        {
            "tid": 168687487743557632,
            "name": "The Empress",
            "points": 40
        },
    "7":
        {
            "tid": 168687487743557632,
            "name": "The Sun",
            "points": 20
        },
    "8":
        {
            "tid": 168687487743557632,
            "name": "The Fool",
            "points": 30
        },
    "9":
        {
            "tid": 168687487743557632,
            "name": "Wheel Of Fortune",
            "points": 20
        },
    "10":
        {
            "id": 168687487743557632,
            "name": "Justice",
            "points": 30
        },
    "11":
        {
            "id": 168687487743557632,
            "name": "Wands",
            "points": 10
        },
    "12":
        {
            "id": 168687487743557632,
            "name": "The Devil",
            "points": 10
        },
    "13":
        {
            "id": 168687487743557632,
            "name": "The Lovers",
            "points": 0
        },
    "14":
        {
            "id": 168687487743557632,
            "name": "The Tower",
            "points": 20
        },
    "15":
        {
            "id": 168687487743557632,
            "name": "Swords",
            "points": 20
        },
    "16":
        {
            "id": 168687487743557632,
            "name": "The Hierophant",
            "points": 10
        },
    "17":
        {
            "id": 168687487743557632,
            "name": "Temperance",
            "points": 30
        },
    "18":
        {
            "id": 168687487743557632,
            "name": "Judgement",
            "points": 0
        },
    "19":
        {
            "id": 168687487743557632,
            "name": "The Magician",
            "points": 20
        },
    "20":
        {"id": 168687487743557632,
            "name": "Cups",
            "points": 20
         },
    "21":
        {
            "id": 168687487743557632,
            "name": "The Hermit",
            "points": 30
        },
    "22":
        {
            "id": 168687487743557632,
            "name": "The Moon",
            "points": 20
        },
    "23":
        {
            "id": 168687487743557632,
            "name": "The World",
            "points": 0
        },
    "24":
        {
            "id": 168687487743557632,
            "name": "Strength",
            "points": 40
        }
}


# def check_answer(uid, answer):
#     kitten = functions.find_user(uid)
#     crib = functions.load_guild(kitten)
#     with open("tasks.json", "r") as t:
#         data = json.load(t)
#         if answer in data.keys():
#             task = Task(*data[answer].values())
#             if crib.currentTask == task.id:
#                 result = crib.add_points(task.reward)
#                 crib.give_next()
#                 functions.upload_guild(crib)
#                 if len(crib.completedTasks) >= 24:
#                     return "You have completed " + str(task.name) + "\nReward of " + str(task.reward) + " points has been given \n"
#                 if result:
#                     return "You have completed " + str(task.name) + "\nReward of " + str(task.reward) + " points has been given \nYour next task is"
#             else:
#                 return "This is not the correct answer"
#         else:
#             return "This is not the correct answer"

def skip_task(cid, diff):
    with open("cribChannels.json", "r") as f:
        data = json.load(f)
        if cid in data.keys():
            kitten = data[cid]
            crib = functions.load_guild(kitten)
            if diff == 1:
                crib.skip(1)
                functions.upload_guild(crib)
                return "Easy objective has been sucessfully skipped"
            elif diff == 2:
                crib.skip(2)
                functions.upload_guild(crib)
                return "Medium objective has been sucessfully skipped"
            elif diff == 3:
                crib.skip(3)
                functions.upload_guild(crib)
                return "Hard objective has been sucessfully skipped"

def org_give_points(uid, cid, Admin, diff):
    with open("cribChannels.json", "r") as f:
        data = json.load(f)
        if cid in data.keys():
            kitten = data[cid]
            crib = functions.load_guild(kitten)
            if diff == 1:
                tid, name, points = org_dict[str(crib.currentEasyTask)].values()
                if Admin == 1:
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(1)
                        functions.upload_guild(crib)
                        if crib.currentEasyTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all easy tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                elif str(uid) == str(tid):
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(1)
                        functions.upload_guild(crib)
                        if crib.currentEasyTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all easy tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                else:
                    return "Pachdon comrade, but you're not able to use this command"
            if diff == 2:
                tid, name, points = org_dict[str(crib.currentMediumTask)].values()
                if Admin == 1:
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(2)
                        functions.upload_guild(crib)
                        if crib.currentMediumTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all medium tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                elif str(uid) == str(tid):
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(2)
                        functions.upload_guild(crib)
                        if crib.currentMediumTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all medium tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                else:
                    return "Pachdon comrade, but you're not able to use this command"
            if diff == 3:
                tid, name, points = org_dict[str(crib.currentHardTask)].values()
                if Admin == 1:
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(3)
                        functions.upload_guild(crib)
                        if crib.currentHardTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all hard tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                elif str(uid) == str(tid):
                    result = crib.add_points(points)
                if result:
                    crib.give_next(3)
                    functions.upload_guild(crib)
                    if crib.currentHardTask == -1:
                        return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all hard tasks!"
                    else:
                        return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYour next task is"
                return "Add Points"
            else:
                return "Pachdon comrade, but you're not able to use this command"
        else:
            print("something is wrong :)")


def get_task(currenttask):
    for t in task_dict:
        if t.id == currenttask:
            embed = discord.Embed(title=t.name, description=t.task)
            return embed
