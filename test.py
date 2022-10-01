import discord
from discord.ext import commands
from functions import *
from classes import Mission

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith('$test'):
    #     id = message.author.id
    #     await message.channel.send("Ovidijus mldc o tu eik nx " + "<@" + str(id) + ">")
        # await message.channel.send("eik nx " + "<@" + str(id) + ">")
        # X = fileRead()
        # for i in range (len(X)):
        #     print(X[i])
        #     # if X[i] == '1':
                

             
client.run('MTAyNDkyMTUxMDYxNzU0NjgxMg.GYJoDb.LwaUCFzSgXa6QWJsnMh0c9DrbhZfv8ikioXfkY')
bot.run('MTAyNDkyMTUxMDYxNzU0NjgxMg.GYJoDb.LwaUCFzSgXa6QWJsnMh0c9DrbhZfv8ikioXfkY')