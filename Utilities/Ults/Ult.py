# This is where i most of the time but variables, etc that i will use a lot


from Utilities.Log.Log import *
import os
from discord.ext import commands
import datetime

# My imports

Log = Logger("ult")

# Settings up my Logger

token = os.getenv("CLIENT_TOKEN")
GuildID = os.getenv("GUILD_ID")
Home_Guild = int(GuildID)
webhook = os.getenv("WEBHOOK")
command_img = os.getenv("COMMAND_LOGS")


# Loading all my variables from my Env file
