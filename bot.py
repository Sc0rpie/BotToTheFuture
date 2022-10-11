from glob import glob
from http import client
from logging import RootLogger
from re import A
from venv import create
# import discord
# from discord.utils import *
# from discord.ext import commands
import random
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

start = False
# Predefined channel ID's
REGISTER_CHANNEL = 1026562999508545558
ADMIN_CHANNEL = 1028015282553360455
CRIB_CHANNEL = 1028015345291771934
HELP_CHANNEL = 1028015404032987216
# Main server admin
me = 168687487743557632

# Role ID's
PARTICIPANT_ID = 1028015588301344940
HELPER_ID = 1028015634837143623
BOT_ID = 1026563432054530173

command_list = ["points", "easy", "medium", "hard", "end", "help", "lead", "skipeasy", "skipmedium", "skiphard", "done1", "done2", "done3"]
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Pachdon bot v0.1 up and running')
    print('------'*10)

@bot.event
async def on_message(ctx: discord.Message):
    if not ctx.author.bot:
        global start
        author = ctx.author
        content = ctx.content.lower()
        channel = ctx.channel
        print(author.name + " " + content)
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
                await channel.send("You have completed all of your hard tasks!")

        elif command == "medium" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))
            if crib.currentMediumTask != -1:
                result = tasks.get_task(crib.currentMediumTask)
                await channel.send(embed = result)
            else:
                await channel.send("You have completed all of your hard tasks!")

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
            if crib.easyAmt == 61:
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
            if crib.hardAmt == 21:
                await channel.send("Objective can not be skipped. This is the last one")
            else:
                result = tasks.skip_task(str(channel.id), 3)
                if result:
                    await channel.send(result)

        elif command == "done1" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                role = get(ctx.guild.roles, name=ctx.channel.name)
                if ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 1)
                else:
                    result = tasks.org_give_points(str(author.id), str(channel.id), False, 1)
                if result:
                    await channel.send(result)
                    crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                    if crib.easyAmt != 3:
                        result = tasks.get_task(crib.currentEasyTask)
                        await channel.send(embed=result)

        elif command == "done2" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                role = get(ctx.guild.roles, name=ctx.channel.name)
                if ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 2)
                else:
                    result = tasks.org_give_points(str(author.id), str(channel.id), False, 2)
                if result:
                    await channel.send(result)
                    crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                    if crib.mediumAmt != 3:
                        result = tasks.get_task(crib.currentMediumTask)
                        await channel.send(embed=result)

        elif command == "done3" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                role = get(ctx.guild.roles, name=ctx.channel.name)
                if ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 3)
                else:
                    result = tasks.org_give_points(str(author.id), str(channel.id), False, 3)
                if result:
                    await channel.send(result)
                    crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                    if crib.hardAmt != 3:
                        result = tasks.get_task(crib.currentHardTask)
                        await channel.send(embed=result)

        elif command == "end":
            if author.id == me:
                result = functions.end_game(str(channel.id))
                if result:
                    await channel.send(result)
            else:
                sub_channel = get(ctx.guild.channels, id=HELP_CHANNEL)
                await sub_channel.send("<@" + str(me) + "> o kitten want to end the game - <#" + str(channel.id) + ">")


async def create_guild(ctx, crib):
    guild = ctx.guild
    member = ctx.author
    kittenrole = await guild.create_role(name=crib.lower(), colour = discord.Colour(0xff00ff))  
    helper = get(ctx.guild.roles, id=HELPER_ID)
    await member.add_roles(kittenrole)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages = False),
        kittenrole: discord.PermissionOverwrite(read_messages=True),
        helper: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(crib, overwrites=overwrites)
    functions.create_guild(crib, str(member.id), channel.id)
    return True


# @bot.command()
# @commands.cooldown(1, 0.5, commands.BucketType.channel)
# async def start(ctx):  # Let the chaos begin. ($start command for members to join a team)
#     global a  # Team members
#     # global teamNum  # Team number

#     guild = ctx.guild
#     user = ctx.message.author

#     playingRole = discord.utils.get(user.guild.roles, name='Playing')
#     if playingRole in user.roles:
#         await ctx.message.delete()
#         return
#     else:
#         await user.add_roles(playingRole)
#         if ctx.channel.id != 1026528350891679754:  # Check if text channel is #bot. If not, error is thrown
#             await ctx.send("PaChDoN huuh??")
#             with open('huuh.png', 'rb') as fp:
#                 await ctx.send(file=discord.File(fp, 'huuh.png'))
#             return
#         elif a == 0:
#             a += 1
#             global teamName
#             teamName = randomTeamName()
#             await guild.create_role(name=str(teamName))
#             global role
#             role = discord.utils.get(user.guild.roles, name=str(teamName))
#             overwrites = discord.PermissionOverwrite()
#             overwrites = {
#                 guild.default_role: discord.PermissionOverwrite(view_channel=False),
#                 role: discord.PermissionOverwrite(view_channel=True)
#             }

#             await guild.create_text_channel(str(teamName), overwrites=overwrites)
#             print("User: " + user.name)
#             print("Role name: " + role.name)
#             print(" ")
#         elif a == 2:
#             a = 1
#             guild = ctx.guild
#             user = ctx.message.author
#             teamName = randomTeamName()
#             await guild.create_role(name=str(teamName))
#             role = discord.utils.get(user.guild.roles, name=str(teamName))
#             overwrites = discord.PermissionOverwrite()
#             overwrites = {
#                 guild.default_role: discord.PermissionOverwrite(view_channel=False),
#                 role: discord.PermissionOverwrite(view_channel=True)
#             }

#             await guild.create_text_channel(str(teamName), overwrites=overwrites)
#             await ctx.message.delete()  # Delete message to have a clean main channel
#             print("User: " + user.name)
#             print("Role name: " + role.name)
#             print(" ")
#         else:
#             a += 1
#             user = ctx.message.author
#             # role = discord.utils.get(user.guild.roles, name = str(teamName))
#             await ctx.message.delete()  # Delete message to have a clean main channel
#             print("User: " + user.name)
#             print("Role name: " + role.name)
#             print(" ")
#         await user.add_roles(role)
#         await ctx.message.delete()  # Delete message to have a clean main channel


# @bot.command()
# # @commands.cooldown(1, 10800, commands.BucketType.user)
# async def test(ctx):  # Team text channel and role creation test (each time $test is run, new role and channel is created)
#     global a  # Team members
#     global teamNum  # Team number

#     if a == 0:
#         guild = ctx.guild
#         global user
#         user = ctx.message.author
#         teamName = randomTeamName()
#         print(teamName)
#         await guild.create_role(name=str(teamName))
#         role = discord.utils.get(user.guild.roles, name=str(teamName))
#         overwrites = discord.PermissionOverwrite()
#         overwrites = {
#             guild.default_role: discord.PermissionOverwrite(view_channel=False),
#             role: discord.PermissionOverwrite(view_channel=True)
#         }
#         await guild.create_text_channel(str(teamName), overwrites=overwrites)
#     await user.add_roles(role)


# @start.error
# async def helloworld_error(ctx, error):
#     if isinstance(error, commands.CommandOnCooldown):
#         await ctx.send(f'Command "start" is no longer available for you')
#         # await ctx.send("PaChDoN huuh??")
#         # with open('huuh.png', 'rb') as fp:
#         #     await ctx.send(file=discord.File(fp, 'huuh.png'))


bot.run(TOKEN)
