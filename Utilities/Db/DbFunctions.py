# This is any functions that use the database


import pymongo
from Utilities.Db.Db import *
from Utilities.Log.Log import *

# my imports

Log = Logger("db_functions")

# Setting up my logger

# Creating the user obkect into database


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
            "Bug_Bunter": id.public_flags.bug_hunter,
            "Partner": id.public_flags.partner,
            "Hypesquad_Member": id.public_flags.hypesquad,
            "Bug_Hunter": id.public_flags.bug_hunter,
            "Premium_promo_dismissed": id.public_flags.premium_promo_dismissed,
            "Hypesquad_Bravery": id.public_flags.hypesquad_bravery,
            "Hypesquad_Brilliance": id.public_flags.hypesquad_brilliance,
            "Hypesquad_Balance": id.public_flags.hypesquad_balance,
            "Early_Supporter": id.public_flags.early_supporter,
            "Team_User": id.public_flags.team_user,
            "System": id.public_flags.system,
            "Bug_Hunter_Level_2": id.public_flags.bug_hunter_level_2,
            "Verified_Bot_Developer": id.public_flags.verified_bot_developer,
            "Discord_Certified_Moderator": id.public_flags.discord_certified_moderator,
            "Bot_Admin": False,
            "Banned": False,
            "Ban_Reason": None,
            "Items": [{"Loot Box 1": 1, "Loot Box 2": 0, "loot Box 3": 0}]
        }
        await Log.info(f"Created user with the discord id of {id.id}")
        return users.insert_one(payload)
        # inserting
