import os
from LaSaga_Bot import LaSaga_Bot
from dotenv import load_dotenv

TOKEN = None # Acess Token for Discord API
GUILD = None # Guild name for securing that the correct Server is managed

#This is a test commit some more changes

def setup():
    global TOKEN
    global GUILD

    load_dotenv()

    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

if __name__ == "__main__":
    #setup environment
    setup()

    #load neccessary data
    

    # Create Discord Bot Class and Run it

    bot = LaSaga_Bot()
    bot.run(TOKEN)