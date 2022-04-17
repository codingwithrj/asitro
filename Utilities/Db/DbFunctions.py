# This is any functions that use the database


import pymongo
from Utilities.Db.Db import *
from Utilities.Log.Log import *

# my imports

Log = Logger("db_functions")

# Setting up my logger

# Creating the user obkect into database


async def CreateGuild(guild):
    myquery = {"Id": guild.id}
    check = guilds.find_one(myquery)
    if check == None:
        payload = {
            "Name": guild.name,
            "Guild_Id": guild.id,
            "Owner_Id": guild.owner.id,
            "Owner_Name": guild.owner.name
        }
        return guilds.insert_one(payload)


async def CreateUser(id):
    myquery = {"Id": id.id}
    check = users.find_one(myquery)
    if check == None:
        # checking if user is in db
        await Log.info("Creating payload")
        banner = id.banner
        if banner != None:
            banner = id.banner.url
        # idd = users.count()
        # idd = idd + 1
        payload = {
            "Id": id.id,
            "Created_At": id.created_at.timestamp(),
            "Defualt_Avatar": id.default_avatar.url,
            "Banner": banner,
            "Avatar": id.avatar.url,
            "User_Accent_Colour": id.accent_colour,
            "Name": id.name,
            "Discriminator": id.discriminator,
            "Name_Full": f'{id.name}#{id.discriminator}',
            "Balance": 0,
            "Level": 0,
            "Mutli": 1,
            "Email": None,
            "Phone": None,
            "Ip": None,
            "Staff": id.public_flags.staff,
            "Partner": id.public_flags.partner,
            "Early_Supporter": id.public_flags.early_supporter,
            "Team_User": id.public_flags.team_user,
            "System": id.public_flags.system,
            "Verified_Bot_Developer": id.public_flags.verified_bot_developer,
            "Discord_Certified_Moderator": id.public_flags.discord_certified_moderator,
            "Bot_Admin": False,
            "Banned": False,
            "Ban_Reason": None,
            "Items": [{"Loot Box 1": 1, "Loot Box 2": 0, "loot Box 3": 0}],
            "Server_Ban": False,
            "Server_Ban_Reason": None,
            "Server_Kicks": 0,
            "Server_Warns": 0,
        }
        await Log.info(f"Created user with the discord id of {id.id}")
        return users.insert_one(payload)
        # inserting
