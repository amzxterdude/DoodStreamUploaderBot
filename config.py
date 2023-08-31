#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("6445661694:AAH58ONy4e7npQwKIju3FJk_iHQrUD-VBrk", "") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("5052763", "0")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("25fc53e982e5a16dcaa5b8e4d232c97f", "") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("-1158786002", None)) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("mongodb+srv://amalkochuparambilp:amalkochuparambilp@cluster0.m96k6qd.mongodb.net/?retryWrites=true&w=majority", "") # Get from MongoDB Atlas

