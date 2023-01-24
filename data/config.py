from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
CHANNEL_ID_1 = env.str("CHANNEL_ID_1")
CHANNEL_ID_2 = env.str("CHANNEL_ID_2")
ADMINS = env.list("ADMINS")  
USERS = env.list("USERS")