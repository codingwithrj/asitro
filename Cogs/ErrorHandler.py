# Command error handler


from discord.ext import commands
from Utilities.Log.Log import *

# My imports

Log = Logger("errors")

# setup my logger

# cog class


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    # basic cog code

    # logs when cog is online
    @commands.Cog.listener()
    async def on_ready(self):
        await Log.info("Errors cog loaded.")

    # some basic error handler (only got one setup and need to add more)

    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        # checks if the user has perms to use the command

        if isinstance(error, commands.CheckFailure):
            await context.reply(
                "You are not priveleged enough to use this command.",
                mention_author=False
            )

        # handles any other errors

        else:
            await context.reply(
                f"**Error**\n```diff\n- {error}```",
                mention_author=False
            )

# cog setup so i can use it later


def setup(client):
    client.add_cog(Errors(client))
