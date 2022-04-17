# my event cog, where all my events are

from discord.commands import Option, permissions, slash_command
from discord.ext import commands
from dotenv import load_dotenv
from Utilities.Log.Log import *

# my imports

Log = Logger("events")

# setting up my logger

# cog class


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # basic cog code

    # logs when the cog is online

    @commands.Cog.listener()
    async def on_ready(self):
        await Log.info("Events cog loaded.")

    # on shard ready event, tells me when a shard is ready (shard is a instance of the bot (discord requires if the bot is in more then 2000 servers))

    @commands.Cog.listener()
    async def on_shard_ready(self, shard_id):
        await Log.info(f"shard ID: {shard_id} is online and ready.")

# cog setup so it can be used later


def setup(bot):
    bot.add_cog(Events(bot))
