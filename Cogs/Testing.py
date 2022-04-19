# testing cog, for new stuff


from discord.commands import (  # Importing the decorator that makes slash commands.
    Option, permissions, slash_command)
from discord.ext import commands
from dotenv import load_dotenv
from Utilities.Log.Log import *
from Utilities.Db.DbFunctions import CreateUser, CreateItemsCoins
from Utilities.Ults.Ult import Home_Guild
from Utilities.Ults.CommandLogging import logCommand

# my imports

Log = Logger("test")

# setting up my logger


# creating the cog class

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # basic cog  start code

    # logs when the cog is laoded
    @commands.Cog.listener()
    async def on_ready(self):
        await Log.info("Test cog loaded.")

    # basic test command to create user
    @slash_command(guild_ids=[Home_Guild])
    async def test(self, ctx):
        await logCommand("test", ctx.author.id, ctx.author)
        id = int(ctx.author.id)
        user = await self.bot.fetch_user(id)
        await CreateUser(user)
        await CreateItemsCoins()
        await ctx.respond("test command runned")

# setup for the cog, so it can be loaded later


def setup(bot):
    bot.add_cog(Example(bot))
