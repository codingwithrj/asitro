# This file is the main, start point (Where i run the bot)


from Utilities.Ults.Ult import token
from Utilities.Log.Log import *
import os
import psutil
import discord
from discord.ext import commands
import discord
from dotenv import load_dotenv

# my imports

load_dotenv()

#Loading in DotEnv

Log = Logger("client")

# Starting the logger

Token = token

# Getting discord bot token from the Ult file

intents = discord.Intents.all()
client = commands.AutoShardedBot(
    shard_count=1, help_command=None, intents=intents)

# discord bot client settings, setting up sharded, etc


@client.event
async def on_ready():
    await Log.info(f"{client.user} is online.")

# My online event (Runs when every i start the bot)


for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"Cogs.{filename[:-3]}")
for filename in os.listdir("./Cogs/Money"):
    if filename.endswith(".py"):
        client.load_extension(f"Cogs.Money.{filename[:-3]}")

# Loads all the files in the Cogs folder that contain the commands

client.run(Token, reconnect=True)

# Starts the bot and automaticly reconnects if needed
