import functions

import os
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import tasks

description = '''A special bot made for a special event called "CatToTheFuture"'''

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Intent - ability of a bot to do something (example: message intent for messaging and etc.)
intents = discord.Intents.all()

# Bot commands start with a prefix (here it's nothing)
bot = commands.Bot(command_prefix='',
                   description=description, intents=intents)

start = True
# Predefined channel ID's
REGISTER_CHANNEL = 1026562999508545558
ADMIN_CHANNEL = 1028015282553360455
CRIB_CHANNEL = 1028015345291771934
HELP_CHANNEL = 1028015404032987216
INFO_CHANNEL = 1030179986264559717
ADMININFO_CHANNEL = 1030118347955765378
# Main server admin
me = 168687487743557632

# Role ID's
ADMIN_ID = 1029148212923215912
PARTICIPANT_ID = 1028015588301344940
HELPER_ID = 1028015634837143623
BOT_ID = 1026563432054530173

command_list = ["points", "easy", "medium", "hard", "end", "help", "lead", "skipeasy", "skipmedium", "skiphard", "done1", "done2", "done3"]
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Pachdon bot v1.0 up and running')
    print('------'*10)

@bot.event
async def on_message(ctx: discord.Message):
    if not ctx.author.bot:
        global start
        author = ctx.author
        content = ctx.content.lower()
        channel = ctx.channel
        print(channel.name + " " + author.name + " " + content)
        data = content.split(" ")
        command = data[0]
        data = data[1:]
        data = ' '.join(data)

        if channel.id == REGISTER_CHANNEL:
            if functions.register(str(author.id)):
                role = get(ctx.guild.roles, id=PARTICIPANT_ID)
                await author.add_roles(role)
            await ctx.delete()

        elif channel.id == ADMIN_CHANNEL and command == "start":
            start = True
            print("Event has started")
            await channel.send("Nu chio pojehali chebra\nTikiuosi botas gyvens. Amen.")

        elif channel.id == CRIB_CHANNEL and command == "create":
            if not functions.find_user(str(author.id)):
                name = functions.randomTeamName()
                if await create_guild(ctx, str(name)):
                    await channel.send("Welcome to the crib dawg, the name of your kitten is: " + str(name))
                else:
                    await channel.send("Something is not right fella")
            else:
                await channel.send("I think that you already have a kitten, one kitten for one group :)")
            # else:
                 #no message here?
        elif channel.id == CRIB_CHANNEL and command == "join":
            if data:
                if not functions.find_user(str(author.id)):
                    result, memb = functions.join(str(author.id), data)
                    if result and memb:
                        role = get(ctx.guild.roles, name=data.lower())
                        if role:
                            await author.add_roles(role)
                            await channel.send("You have successfully joined: " + str(data))
                    elif result:
                        await channel.send("It seems like the crib is full")
                else:
                    await channel.send("You already have a kitten. You shall not pass!")
            else:
                await channel.send("Frend I think you forgot to enter the name of ze kitten...\n *whispers* it goes like this: \"join <kitten name>\"")
        
        elif not start and command in command_list:
            await channel.send("Dede Avidij dar neleido pradet")

        elif channel.id == HELP_CHANNEL and command == "points":
            try:
                if data:
                    guildname = " ".join(content.split(" ")[1:-1])
                    points = int(content.split(" ")[-1])
                    coven = functions.load_guild(guildname.lower())
                    coven.add_points(points)
                    functions.upload_guild(coven)
            except Exception as e:
                print("main" + str(e))
                await channel.send("points <coven> <number>")

        elif command == "help":
            sub_channel = get(ctx.guild.channels, id=HELP_CHANNEL)
            await sub_channel.send("<@" + str(me) + "> help at <#" + str(channel.id) + ">")

        elif command == "easy" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))
            if crib.currentEasyTask != -1:
                result = tasks.get_task(crib.currentEasyTask)
                await channel.send(embed = result)
            else:
                await channel.send("You have completed all of your easy tasks!")

        elif command == "medium" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))
            if crib.currentMediumTask != -1:
                result = tasks.get_task(crib.currentMediumTask)
                await channel.send(embed = result)
            else:
                await channel.send("You have completed all of your medium tasks!")

        elif command == "hard" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))
            if crib.currentHardTask != -1:
                result = tasks.get_task(crib.currentHardTask)
                await channel.send(embed = result)
            
            else:
                await channel.send("You have completed all of your hard tasks!")

        elif command == "lead":
            if channel.id == ADMIN_CHANNEL:
                result = functions.update_leaderboard()
                if result:
                    await channel.send(result)
            else:
                kittenname = functions.find_user(str(author.id))
                crib = functions.load_guild(kittenname)
                await channel.send(embed=crib.lead())

        elif command == "skipeasy" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))
            if crib.easyAmt == 60:
                await channel.send("Objective can not be skipped. This is the last one")
            else:
                result = tasks.skip_task(str(channel.id), 1)
                if result:
                    await channel.send(result)
        
        elif command == "skipmedium" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))
            if crib.mediumAmt == 47:
                await channel.send("Objective can not be skipped. This is the last one")
            else:
                result = tasks.skip_task(str(channel.id), 2)
                if result:
                    await channel.send(result)
        
        elif command == "skiphard" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))
            if crib.hardAmt == 22:
                await channel.send("Objective can not be skipped. This is the last one")
            else:
                result = tasks.skip_task(str(channel.id), 3)
                if result:
                    await channel.send(result)

        elif command == "done1" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                role = get(ctx.guild.roles, id=ADMIN_ID)
                if role in ctx.author.roles or ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 1)
                    if result:
                        await channel.send(embed=result)
                        crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                        if crib.easyAmt != 61:
                            nextTask = discord.Embed(title="Your next task is:")
                            await channel.send(embed=nextTask)
                            result = tasks.get_task(crib.currentEasyTask)
                            await channel.send(embed=result)
                else:
                    await channel.send("Pachdon comrade, but you're not able to use this command")# result = tasks.org_give_points(str(author.id), str(channel.id), False, 1)
                
                    # if crib.easyAmt != 61:
                    #     result = tasks.get_task(crib.currentEasyTask)
                    #     await channel.send(embed=result)

        elif command == "done2" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                # role = get(ctx.guild.roles, name=ctx.channel.name)
                role = get(ctx.guild.roles, id=ADMIN_ID)
                if role in ctx.author.roles or ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 2)
                    if result:
                        await channel.send(embed=result)
                        crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                        if crib.mediumAmt != 48:
                            nextTask = discord.Embed(title="Your next task is:")
                            await channel.send(embed=nextTask)
                            result = tasks.get_task(crib.currentMediumTask)
                            await channel.send(embed=result)
                else:
                    await channel.send("Pachdon comrade, but you're not able to use this command")
                    # if crib.mediumAmt != 48:
                    #     result = tasks.get_task(crib.currentMediumTask)
                    #     await channel.send(embed=result)

        elif command == "done3" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                # role = get(ctx.guild.roles, name=ctx.channel.name)
                role = get(ctx.guild.roles, id=ADMIN_ID)
                if role in ctx.author.roles or ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 3)
                    if result:
                        await channel.send(embed=result)
                        crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                        if crib.hardAmt != 23:
                            nextTask = discord.Embed(title="Your next task is:")
                            await channel.send(embed=nextTask)
                            result = tasks.get_task(crib.currentHardTask)
                            await channel.send(embed=result)
                else:
                    await channel.send("Pachdon comrade, but you're not able to use this command")
                    # if crib.hardAmt != 23:
                    #     result = tasks.get_task(crib.currentHardTask)
                    #     await channel.send(embed=result)

        elif command == "end":
            if author.id == me:
                result = functions.end_game(str(channel.id))
                if result:
                    await channel.send(result)
            else:
                sub_channel = get(ctx.guild.channels, id=HELP_CHANNEL)
                await sub_channel.send("<@" + str(me) + "> o kitten want to end the game - <#" + str(channel.id) + ">")
        
        elif command == "info" and channel.id == INFO_CHANNEL:
            await ctx.delete()
            commandInfo = discord.Embed(title="help", description=":flag_lt:Iškviečia organizatorių\n:flag_gb:Calls the organizer")
            await channel.send(embed=commandInfo)
            commandInfo = discord.Embed(title="create", description=":flag_lt:Sukuria komandą su atsitiktiniu pavadinimu (1 žmogus gali sukurti 1 komandą)\n:flag_gb:Creates a team with a random name (1 team per person)")
            await channel.send(embed=commandInfo)
            commandInfo = discord.Embed(title="join <team name>", description=":flag_lt:Leidžia prisijungti prie jau sukurtos komandos (iki 6 žmonių komandoje)\n:flag_gb:Allows to join an existing team (max 6 people per team)")
            await channel.send(embed=commandInfo)
            commandInfo = discord.Embed(title="easy", description=":flag_lt:Parodo lengvą užduotį\n:flag_gb:Shows an easy difficulty mission")
            await channel.send(embed=commandInfo)
            commandInfo = discord.Embed(title="medium", description=":flag_lt:Parodo vidutinio sunkumo užduotį\n:flag_gb:Shows a medium difficulty mission")
            await channel.send(embed=commandInfo)
            commandInfo = discord.Embed(title="hard", description=":flag_lt:Parodo sunkią užduotį\n:flag_gb:Shows a hard difficulty mission")
            await channel.send(embed=commandInfo)
            commandInfo = discord.Embed(title="skipeasy", description=":flag_lt:Praleidžia lengvą užduotį (vėliau galima prie jos grįžti)\n:flag_gb:Skips an easy mission")
            await channel.send(embed=commandInfo)
            commandInfo = discord.Embed(title="skipmedium", description=":flag_lt:Praleidžia vidutinę užduotį (vėliau galima prie jos grįžti)\n:flag_gb:Skips a medium mission")
            await channel.send(embed=commandInfo)
            commandInfo = discord.Embed(title="skiphard", description=":flag_lt:Praleidžia sunkią užduotį (vėliau galima prie jos grįžti)\n:flag_gb:Skips a hard mission")
            await channel.send(embed=commandInfo)
        # elif command == "admininfo" and channel.id == ADMININFO_CHANNEL:
        #     await ctx.delete()
        #     commandInfo = discord.Embed(title="COMMAND LIST")
        #     await channel.send(embed=commandInfo)
        #     commandInfo = discord.Embed(title="done1", description=":flag_lt:Užbaigia easy užd.")
        #     await channel.send(embed=commandInfo)
        #     commandInfo = discord.Embed(title="done2", description=":flag_lt:Užbaigia medium užd.")
        #     await channel.send(embed=commandInfo)
        #     commandInfo = discord.Embed(title="done3", description=":flag_lt:Užbaigia hard užd.")
        #     await channel.send(embed=commandInfo)


async def create_guild(ctx, crib):
    guild = ctx.guild
    member = ctx.author
    kittenrole = await guild.create_role(name=crib.lower(), colour = discord.Colour.random(), hoist = True)
    # kittenrole.hoist = True  
    # helper = get(ctx.guild.roles, id=HELPER_ID)
    await member.add_roles(kittenrole)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages = False),
        kittenrole: discord.PermissionOverwrite(read_messages=True)
        # helper: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(crib, overwrites=overwrites)
    await functions.create_guild(crib, str(member.id), channel.id)
    return True

bot.run(TOKEN)
