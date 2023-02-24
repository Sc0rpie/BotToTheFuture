# Pachdon bot v1.0
# Made for CatToTheFuture event of Vilnius University Mathematics and Informatics Faculty
# This is the main file of the bot. Startup should be done here.
# Make sure to add a .env file in the root of this project with the following content: TOKEN=<your bot token> (without <>)
# Missions were hard coded into the code, good idea to use json files for that in the future (wasn't implemented due to time constraints)


import functions

import os
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import tasks

description = '''A special bot made for a special event called "CatToTheFuture"'''

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")
# Intent - ability of a bot to do something (example: message intent for messaging and etc.)
intents = discord.Intents.all()

# Bot commands start with a prefix (here it's nothing)
bot = commands.Bot(command_prefix='',
                   description=description, intents=intents)

# Global variables
start = True                            # Boolean variable for checking if the event has started. Can be used by 
                                        # admins to start the event (set to False if you want to use it)

# Predefined channel ID's (Change to your own channel id's if you want to use this bot)
REGISTER_CHANNEL = 1026562999508545558
ADMIN_CHANNEL = 1028015282553360455
CRIB_CHANNEL = 1028015345291771934
HELP_CHANNEL = 1028015404032987216
INFO_CHANNEL = 1030179986264559717
ADMININFO_CHANNEL = 1030118347955765378
# Main server admin id
me = 168687487743557632

# Role ID's (for checking and adding roles to users)
ADMIN_ID = 1029148212923215912
PARTICIPANT_ID = 1028015588301344940
HELPER_ID = 1028015634837143623
BOT_ID = 1026563432054530173

# List of available commands (dunno if this is needed xd)
command_list = ["points", "easy", "medium", "hard", "end", "help", "lead", "skipeasy", "skipmedium", "skiphard", "done1", "done2", "done3"]

# Start up message
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Pachdon bot v1.0 up and running')
    print('------'*10)

# Checking input messages
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

        # Register channel
        if channel.id == REGISTER_CHANNEL:
            if functions.register(str(author.id)):
                role = get(ctx.guild.roles, id=PARTICIPANT_ID)      # Registers player as a participant
                await author.add_roles(role)
            await ctx.delete()                                      # Deletes message


        # Admin channel
        elif channel.id == ADMIN_CHANNEL and command == "start":    # Checks if admin channel and if message is "start"
            start = True                                            # Sets start to True and allows commands to be used            
            print("Event has started")
            await channel.send("Nu chio pojehali chebra\nTikiuosi botas gyvens. Amen.") 

        # Crib channel
        elif channel.id == CRIB_CHANNEL and command == "create":    # Checks if crib channel and if message is "create"
            if not functions.find_user(str(author.id)):             # Checks if user already has a crib
                name = functions.randomTeamName()                   # Generates random name for the crib
                if await create_guild(ctx, str(name)):              # Creates a new crib
                    await channel.send("Welcome to the crib dawg, the name of your kitten is: " + str(name))
                else:
                    await channel.send("Something is not right fella")
            else:
                await channel.send("I think that you already have a kitten, one kitten for one group :)")
            # else:
                 #no message here?

        # Crib channel
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

        # Help channel
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

        # Global command HELP. Sends message to help channel if user types "help" in any channel
        elif command == "help":
            sub_channel = get(ctx.guild.channels, id=HELP_CHANNEL)
            await sub_channel.send("<@" + str(me) + "> help at <#" + str(channel.id) + ">") # Sends message to help channel with info about the user and the channel

        # Global command EASY. Checks if channel is not register or crib channel and if user has a crib
        elif command == "easy" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))    # Loads crib of the user
            if crib.currentEasyTask != -1:                                      # Checks if user has any easy tasks left
                result = tasks.get_task(crib.currentEasyTask)                   # Gets task from tasks.py
                await channel.send(embed = result)                              # Sends task to the channel
            else:
                await channel.send("You have completed all of your easy tasks!")    # Sends message if user has no easy tasks left

        # Global command MEDIUM. Checks if channel is not register or crib channel and if user has a crib
        elif command == "medium" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))    # Loads crib of the user
            if crib.currentMediumTask != -1:                                    # Checks if user has any medium tasks left
                result = tasks.get_task(crib.currentMediumTask)                 # Gets task from tasks.py
                await channel.send(embed = result)                              # Sends task to the channel
            else:
                await channel.send("You have completed all of your medium tasks!")  # Sends message if user has no medium tasks left

        # Global command HARD. Checks if channel is not register or crib channel and if user has a crib
        elif command == "hard" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))    # Loads crib of the user
            if crib.currentHardTask != -1:                                      # Checks if user has any hard tasks left
                result = tasks.get_task(crib.currentHardTask)                   # Gets task from tasks.py
                await channel.send(embed = result)                              # Sends task to the channel
            else:
                await channel.send("You have completed all of your hard tasks!")    # Sends message if user has no hard tasks left

        # Global command LEADERBOARD. Checks if channel is admin channel
        # Updates the leaderboard and sends it to the channel
        elif command == "lead":
            if channel.id == ADMIN_CHANNEL:
                result = functions.update_leaderboard()
                if result:
                    await channel.send(result)
            else:                                                   # Haven't used it, maybe works maybe not ¯\_(ツ)_/¯
                kittenname = functions.find_user(str(author.id))
                crib = functions.load_guild(kittenname)
                await channel.send(embed=crib.lead())

        # Global command SKIPEASY. Checks if channel is not register or crib channel and if user has a crib
        elif command == "skipeasy" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))    # Loads crib of the user
            if crib.easyAmt == 60:                                              # Checks if it's the last task
                await channel.send("Objective can not be skipped. This is the last one")
            else:
                result = tasks.skip_task(str(channel.id), 1)                    # Skips task
                if result:
                    await channel.send(result)                                  # Sends message if task was skipped
        
        # Global command SKIPMEDIUM. Checks if channel is not register or crib channel and if user has a crib
        elif command == "skipmedium" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))    # Loads crib of the user
            if crib.mediumAmt == 47:                                            # Checks if it's the last task
                await channel.send("Objective can not be skipped. This is the last one")
            else:
                result = tasks.skip_task(str(channel.id), 2)                    # Skips task
                if result:
                    await channel.send(result)                                  # Sends message if task was skipped
        
        # Global command SKIPHARD. Checks if channel is not register or crib channel and if user has a crib
        elif command == "skiphard" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            crib = functions.load_guild(functions.find_user(str(author.id)))    # Loads crib of the user
            if crib.hardAmt == 22:                                              # Checks if it's the last task
                await channel.send("Objective can not be skipped. This is the last one")
            else:
                result = tasks.skip_task(str(channel.id), 3)                    # Skips task
                if result:
                    await channel.send(result)                                  # Sends message if task was skipped

        # Global command DONE1. Checks if channel is not register or crib channel and if user has a crib
        # Used by admins to give points to users if task was done
        elif command == "done1" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                role = get(ctx.guild.roles, id=ADMIN_ID)                        # Gets admin role
                if role in ctx.author.roles or ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 1)    # Gives points to user
                    if result:
                        await channel.send(embed=result)                        # Sends message if task was done
                        crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                        if crib.easyAmt != 61:                                  # Checks if it's the last task, otherwise sends next task    
                            nextTask = discord.Embed(title="Your next task is:")
                            await channel.send(embed=nextTask)
                            result = tasks.get_task(crib.currentEasyTask)
                            await channel.send(embed=result)
                else:
                    await channel.send("Pachdon comrade, but you're not able to use this command")# result = tasks.org_give_points(str(author.id), str(channel.id), False, 1)
                
                    # if crib.easyAmt != 61:
                    #     result = tasks.get_task(crib.currentEasyTask)
                    #     await channel.send(embed=result)

        # Global command DONE2. Checks if channel is not register or crib channel and if user has a crib
        # Used by admins to give points to users if task was done
        elif command == "done2" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                # role = get(ctx.guild.roles, name=ctx.channel.name)
                role = get(ctx.guild.roles, id=ADMIN_ID)                        # Gets admin role
                if role in ctx.author.roles or ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 2)   # Gives points to user
                    if result:
                        await channel.send(embed=result)                        # Sends message if task was done
                        crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                        if crib.mediumAmt != 48:                                # Checks if it's the last task, otherwise sends next task
                            nextTask = discord.Embed(title="Your next task is:")
                            await channel.send(embed=nextTask)
                            result = tasks.get_task(crib.currentMediumTask)
                            await channel.send(embed=result)
                else:                                                           # Sends message if user is not admin
                    await channel.send("Pachdon comrade, but you're not able to use this command")
                    # if crib.mediumAmt != 48:
                    #     result = tasks.get_task(crib.currentMediumTask)
                    #     await channel.send(embed=result)

        # Global command DONE3. Checks if channel is not register or crib channel and if user has a crib
        # Used by admins to give points to users if task was done
        elif command == "done3" and channel.id != REGISTER_CHANNEL and channel.id != CRIB_CHANNEL:
            # if data == '1':
                # role = get(ctx.guild.roles, name=ctx.channel.name)
                role = get(ctx.guild.roles, id=ADMIN_ID)                            # Gets role of the admin
                if role in ctx.author.roles or ctx.author.id == me:
                    result = tasks.org_give_points(str(author.id), str(channel.id), True, 3)    # Gives points to user
                    if result:
                        await channel.send(embed=result)                            # Sends message if points were given
                        crib = functions.load_guild(functions.find_cribname_by_channelid(str(channel.id)))
                        if crib.hardAmt != 23:                                      # Checks if it's the last task, otherwise sends next task        
                            nextTask = discord.Embed(title="Your next task is:")
                            await channel.send(embed=nextTask)
                            result = tasks.get_task(crib.currentHardTask)
                            await channel.send(embed=result)
                else:
                    await channel.send("Pachdon comrade, but you're not able to use this command")
                    # if crib.hardAmt != 23:
                    #     result = tasks.get_task(crib.currentHardTask)
                    #     await channel.send(embed=result)

        #Global command END. Used for ending the game - Admin only
        elif command == "end":
            if author.id == me:                                                 # Checks if user is the bot owner
                result = functions.end_game(str(channel.id))                    # Ends the game
                if result:
                    await channel.send(result)                                  # Sends message if game was ended
            else:
                sub_channel = get(ctx.guild.channels, id=HELP_CHANNEL)          # Sends message to help channel if user is not the bot owner
                await sub_channel.send("<@" + str(me) + "> o kitten want to end the game - <#" + str(channel.id) + ">")
        
        # Global command INFO. This command is used to send info about other commands into the info channel.
        # Info channel should be read-only so only admins can use it
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

# This command is used to create a team with a random name
async def create_guild(ctx, crib):
    guild = ctx.guild
    member = ctx.author
    kittenrole = await guild.create_role(name=crib.lower(), colour = discord.Colour.random(), hoist = True)
    # kittenrole.hoist = True  
    # helper = get(ctx.guild.roles, id=HELPER_ID)
    await member.add_roles(kittenrole)                                      # Add role to the user
    overwrites = {                                                          # Set permissions for the channel
        guild.default_role: discord.PermissionOverwrite(read_messages = False),
        kittenrole: discord.PermissionOverwrite(read_messages=True)
        # helper: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(crib, overwrites=overwrites)  # Create a channel
    await functions.create_guild(crib, str(member.id), channel.id)          # Create a guild in the database
    return True

bot.run(TOKEN)                                                             # Run the bot with the token provided in .env file
