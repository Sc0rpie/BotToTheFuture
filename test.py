import discord

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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
client.run('MTAyNDkyMTUxMDYxNzU0NjgxMg.GYBBRW.6NYRenmTFtoZEd8ZdbAmSUmLbf_L0J6AsAWLNI')