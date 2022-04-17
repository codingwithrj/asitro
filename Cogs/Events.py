# my event cog, where all my events are

from discord.commands import Option, permissions, slash_command
from discord.ext import commands
from dotenv import load_dotenv
from Utilities.Log.Log import *
import discord
from discord.commands.core import slash_command
from discord.ext import commands
from Utilities.Db.Db import *
from Utilities.Db.DbFunctions import CreateGuild
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

    # on join guil to log data
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await CreateGuild(guild)
        embed = discord.Embed(title="Bot Invite Message",
                              description="Thank you for adding the bot, make sure to check out our help commands like our refer. [asitro](https://www.asitro.com/). Our discord [discord](https://discord.gg/CdsEq4YBpT).")
        embed.set_author(
            name="Astiro", icon_url="https://raw.githubusercontent.com/MountainTiger144/StreamlootEvents/main/img/SLEvents%20Bot%20Logo.png")
        embed.set_thumbnail(
            url="https://raw.githubusercontent.com/MountainTiger144/StreamlootEvents/main/img/SLEvents%20Bot%20Logo.png")
        embed.set_footer(text="Asitro Message System")
        await guild.owner.send(embed=embed)
# cog setup so it can be used later


def setup(bot):
    bot.add_cog(Events(bot))
