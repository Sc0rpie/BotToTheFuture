from glob import glob
from http import client
from logging import RootLogger
from re import A
from venv import create
import discord
from discord.utils import *
from discord.ext import commands
import random
from functions import *

description = '''A special bot made for a special event called "CatToTheFuture"'''

a = 0
teamNum = 1

intents = discord.Intents.default() # Intent - ability of a bot to do something (example: message intent for messaging and etc.)
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents) # Bot commands start with a prefix (here it's $)

async def channelCreate(): # For code to look cleaner (not implemented yet)
    pass


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------'*10)

@bot.command()
@commands.cooldown(1, 10800, commands.BucketType.user)
async def start(ctx): # Let the chaos begin. ($start command for members to join a team)
    global a # Team members
    global teamNum # Team number

    if ctx.channel.id != 1026528350891679754: # Check if text channel is #bot. If not, error is thrown
        await ctx.send("PaChDoN huuh??")
        with open('huuh.png', 'rb') as fp:
            await ctx.send(file=discord.File(fp, 'huuh.png'))       
        return
    elif a == 0:
        guild = ctx.guild
        user = ctx.message.author
        teamName = randomTeamName()
        await guild.create_role(name = str(teamName))
        global role
        role = discord.utils.get(user.guild.roles, name = str(teamName))
        overwrites = discord.PermissionOverwrite()
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel = False),
            role: discord.PermissionOverwrite(view_channel = True)
        }

        await guild.create_text_channel(str(teamName), overwrites = overwrites)
        a += 1
        await ctx.message.delete() # Delete message to have a clean main channel
    elif a == 2: 
        guild = ctx.guild
        user = ctx.message.author
        teamName = randomTeamName()
        role = discord.utils.get(user.guild.roles, name = str(teamName))
        overwrites = discord.PermissionOverwrite()
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel = False),
            role: discord.PermissionOverwrite(view_channel = True)
        }

        await guild.create_text_channel(str(teamName), overwrites = overwrites)
        a = 1
        await ctx.message.delete() # Delete message to have a clean main channel
    else:
        user = ctx.message.author
        a += 1
        await ctx.message.delete() # Delete message to have a clean main channel
    await user.add_roles(role)



@bot.command()
# @commands.cooldown(1, 10800, commands.BucketType.user)
async def test(ctx): # Team text channel and role creation test (each time $test is run, new role and channel is created)
    global a # Team members
    global teamNum # Team number

    if a == 0:
        guild = ctx.guild
        global user
        user = ctx.message.author
        teamName = randomTeamName()
        print(teamName)
        await guild.create_role(name = str(teamName))
        role = discord.utils.get(user.guild.roles, name = str(teamName))
        overwrites = discord.PermissionOverwrite()
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel = False),
            role: discord.PermissionOverwrite(view_channel = True)
        }
        await guild.create_text_channel(str(teamName), overwrites = overwrites)
    await user.add_roles(role)

@start.error
async def helloworld_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        #await ctx.send(f'Command "start" is no longer available for you')
        await ctx.send("PaChDoN huuh??")
        with open('huuh.png', 'rb') as fp:
            await ctx.send(file=discord.File(fp, 'huuh.png'))



bot.run('MTAyNDkyMTUxMDYxNzU0NjgxMg.GYJoDb.LwaUCFzSgXa6QWJsnMh0c9DrbhZfv8ikioXfkY')