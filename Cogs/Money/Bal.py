# testing cog, for new stuff


from discord.commands import (  # Importing the decorator that makes slash commands.
    Option, permissions, slash_command)
from discord.ext import commands
from dotenv import load_dotenv
from Utilities.Log.Log import *
from Utilities.Db.DbFunctions import CreateUser, CreateItemsCoins, GetUserStatById
from Utilities.Ults.Ult import Home_Guild
from Utilities.Ults.CommandLogging import logCommand
import discord
from discord.ext import commands
# my imports

Log = Logger("Balance")

# setting up my logger


# creating the cog class

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # basic cog  start code

    # logs when the cog is laoded
    @commands.Cog.listener()
    async def on_ready(self):
        await Log.info("Balance cog loaded.")

    @slash_command(guild_ids=[Home_Guild], description="Check your balance or a another user.")
    async def balance(self, ctx, member: discord.Member = None):
        user = member or ctx.author
        UserData = await GetUserStatById(user.id)
        if UserData == "Error 1":
            await Log.info(f"No user found {user.id}.")
            await ctx.respond("This user has not been found, ask them to run a command to create account.", ephemeral=True)
        else:
            await Log.info("Return user balance")
            if member is None:
                await ctx.respond(f"{user.name} balance is {UserData['Balance']}")
            elif member != None:
                await ctx.respond(f"Your Balance is {UserData['Balance']}")

    # create a user command for the supplied guilds
    @commands.user_command(name="balance", guild_ids=[Home_Guild])
    async def UserBalance(self, ctx, member: discord.Member = None):
        user = member or ctx.author
        UserData = await GetUserStatById(user.id)
        if UserData == "Error 1":
            await Log.info(f"No user found {user.id}.")
            await ctx.respond("This user has not been found, ask them to run a command to create account.", ephemeral=True)
        else:
            await Log.info("Return user balance")
            if member is None:
                await ctx.respond(f"{user.name} balance is {UserData['Balance']}")
            elif member != None:
                await ctx.respond(f"Your Balance is {UserData['Balance']}")

    # user commands and message commands can have spaces in their names

    # creates a global message command
    @commands.message_command(name="balance", guild_ids=[Home_Guild])
    async def MessageBalance(self, ctx, member: discord.Member = None):
        user = member or ctx.author
        UserData = await GetUserStatById(user.id)
        if UserData == "Error 1":
            await Log.info(f"No user found {user.id}.")
            await ctx.respond("This user has not been found, ask them to run a command to create account.", ephemeral=True)
        else:
            await Log.info("Return user balance")
            if member is None:
                await ctx.respond(f"{user.name} balance is {UserData['Balance']}")
            elif member != None:
                await ctx.respond(f"Your Balance is {UserData['Balance']}")


# setup for the cog, so it can be loaded later


def setup(bot):
    bot.add_cog(Balance(bot))
