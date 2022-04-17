# db setup

import pymongo
from Utilities.Log.Log import *

# My imports

Log = Logger("db_manager")

# setting up my logger

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# my connection to localhost ( wil change to env once i move to a vps, etc)

db = myclient["mydatabase"]

# setting up the database

users = db["users"]


# setting up the user collection
