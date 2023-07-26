from environs import Env
import json
import os

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
CHANNEL_ID_1 = env.str("CHANNEL_ID_1")
CHANNEL_ID_2 = env.str("CHANNEL_ID_2")
ADMINS = env.list("ADMINS")  
USERS = env.list("USERS")
MAIN_SHEET_ID = env.str("MAIN_SHEET_ID")
KEY = json.loads(os.environ['KEY'])