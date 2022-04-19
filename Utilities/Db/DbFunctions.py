# This is any functions that use the database


import pymongo
from Utilities.Db.Db import *
from Utilities.Log.Log import *
from Utilities.Ults.Ult import time
# my imports

Log = Logger("db_functions")

# Setting up my logger

# Creating the user obkect into database


async def CreateGuild(guild):
    myquery = {"Id": guild.id}
    check = guilds.find_one(myquery)
    if check is None:
        payload = {
            "Name": guild.name,
            "Guild_Id": guild.id,
            "Owner_Id": guild.owner.id,
            "Owner_Name": guild.owner.name
        }
        return guilds.insert_one(payload)


async def CreateItemsCoins():
    myquery = {"Made": True}
    check = items.find_one(myquery)
    if check is None:
        await Log.info("Creating items payload")
        payload = {
            "SpaceShip": [{"Price": 250000000}, {"Desc": "Only the top few can get this item."}, {"TradeAbled": False}]
        }
        await Log.info("Created items")
        return items.insert_one(payload)


async def CreateUser(id):
    myquery = {"Id": id.id}
    check = users.find_one(myquery)
    if check is None:
        # checking if user is in db
        await Log.info("Creating user payload")
        banner = id.banner
        if banner != None:
            banner = id.banner.url
        # idd = users.count()
        # idd = idd + 1
        payload = {
            "Id": id.id,
            "Created_At": id.created_at.timestamp(),
            'First_Use': time,
            "Name": id.name,
            "Discriminator": id.discriminator,
            "Name_Full": f'{id.name}#{id.discriminator}',
            "Balance": 0,
            "Bank_Max": 1000,
            "Bank_Balance": 500,
            "Xp": 12312,
            "Level": 12,
            "Xp_Level": 100,
            "Prestige": 1,
            "Level_In_tell_Prestige": 1000,
            "Mutli": 1,
            "Email": None,
            "Phone": None,
            "Ip": None,
            "Bot_Admin": False,
            "Banned": False,
            "Ban_Reason": None,
            "Items": [{"Loot Box 1": 1, "Loot Box 2": 0, "loot Box 3": 0}],
            "Cypto": [{"Bitcoin": 1}, {"Ethereum": 0}, {"DogeCoin": 0}, {"MXR": 0}],
            "Server_Ban": False,
            "Server_Ban_Reason": None,
            "Server_Kicks": 0,
            "Server_Warns": 0,
        }
        await Log.info(f"Created user with the discord id of {id.id}")
        return users.insert_one(payload)
        # inserting


async def GetUserStatById(id):
    UserData = users.find_one({"Id": id})
    if UserData is None:
        return "Error 1"
    return UserData
