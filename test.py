import discord
import time
from functions import *
from classes import Mission

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        X = fileRead()
        for i in range (len(X)):
            print(X[i])
            if X[i] == '1':
                
                await message.channel.send(X[i])
             
client.run('MTAyNDkyMTUxMDYxNzU0NjgxMg.GYJoDb.LwaUCFzSgXa6QWJsnMh0c9DrbhZfv8ikioXfkY')