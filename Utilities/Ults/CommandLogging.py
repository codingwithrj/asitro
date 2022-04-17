# This file is to log my commands, to a webhook and console

import aiohttp
from discord import Webhook
from Utilities.Log.Log import *
import discord
from discord.ext import commands
from Utilities.Ults.Ult import webhook as webhookurl
from Utilities.Ults.Ult import command_img, time

# My imports

Log = Logger("Command_Logs")

# settings up the logger

# Logger async function


async def logCommand(command, id, name):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhookurl, session=session)
        # basic webhook setup
        embed = discord.Embed(
            title="Asitro Logs", description="Asitro Command Logs", color=0x00ff1e)
        embed.set_author(name="Asitro Logging System",
                         icon_url=command_img)
        embed.set_thumbnail(
            url=command_img)
        embed.add_field(name="Command", value=command, inline=True)
        embed.add_field(name="User", value=name, inline=True)
        embed.add_field(name="Id", value=id, inline=True)
        embed.add_field(name="Time", value=time, inline=True)
        embed.set_footer(text="Asitro Logs")
        # Webhook embed
        await webhook.send(embed=embed, username='Asitro logs', avatar_url=command_img)
        await Log.info(f"User {name} with the id {id} used command {command}")
        # Sending the log and webhook
