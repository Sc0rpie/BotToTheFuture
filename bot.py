# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.utils import *
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def start(ctx):
    # guild = ctx.guild
    # await guild.create_role(name="cumpiss")
    user = ctx.message.author
    role = discord.utils.get(user.guild.roles, name="cumpiss")
    await user.add_roles(role)

@bot.command()
async def createCumpiss(ctx):
    guild = ctx.guild
    await guild.create_role(name="cumpiss")

bot.run('MTAyNDkyMTUxMDYxNzU0NjgxMg.GYJoDb.LwaUCFzSgXa6QWJsnMh0c9DrbhZfv8ikioXfkY')