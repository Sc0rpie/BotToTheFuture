# This example requires the 'members' and 'message_content' privileged intents to function.

from glob import glob
from http import client
from re import A
from venv import create
import discord
from discord.utils import *
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

a = 0
teamNum = 1

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------'*10)

@bot.command()
@commands.cooldown(1, 10800, commands.BucketType.user)
async def start(ctx):
    global a
    global teamNum
    #role = discord.utils.get(ctx.guild.roles, name="Admin")

    if ctx.channel.id != 1026012141867769876:
        await ctx.send("PaChDoN huuh??")
        with open('huuh.png', 'rb') as fp:
            await ctx.send(file=discord.File(fp, 'huuh.png'))       
        return
    elif a == 0:
        guild = ctx.guild
        user = ctx.message.author
        #team_role = get(guild.roles, name="cumpiss" + str(teamNum))
        channel = await guild.create_text_channel("cumpiss " + str(teamNum))
        await channel.set_permissions(ctx.guild.default_role, view_channel=False)
        await guild.create_role(name="cumpiss " + str(teamNum)) #padaro roles
        role = discord.utils.get(user.guild.roles, name = "cumpiss " + str(teamNum))
        a += 1
    elif a == 2:
        teamNum += 1
        guild = ctx.guild
        channel = await guild.create_text_channel("cumpiss " + str(teamNum))
        await channel.set_permissions(ctx.guild.default_role, view_channel=False)
        await guild.create_role(name="cumpiss " + str(teamNum)) 
        user = ctx.message.author
        role = discord.utils.get(user.guild.roles, name = "cumpiss " + str(teamNum))
        a = 1
    else:
        user = ctx.message.author
        role = discord.utils.get(user.guild.roles, name = "cumpiss " + str(teamNum))
        a += 1
    await user.add_roles(role)
  
@start.error
async def helloworld_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        #await ctx.send(f'Command "start" is no longer available for you')
        await ctx.send("PaChDoN huuh??")
        with open('huuh.png', 'rb') as fp:
            await ctx.send(file=discord.File(fp, 'huuh.png'))



bot.run('MTAyNDkyMTUxMDYxNzU0NjgxMg.GYJoDb.LwaUCFzSgXa6QWJsnMh0c9DrbhZfv8ikioXfkY')