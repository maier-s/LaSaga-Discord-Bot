import os
import sys
from LaSaga_Bot import LaSaga_Bot

TOKEN = None # Acess Token for Discord API
GUILD = None # Guild name for securing that the correct Server is managed

def setup():
    global TOKEN
    global GUILD

    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    if not TOKEN:
        print("Environment variable TOKEN ist empty")
        sys.exit()
    
    if not GUILD:
        print("Environment variable GUILD ist empty")
        sys.exit()

if __name__ == "__main__":
    #setup environment
    setup()

    #load neccessary data

    # Create Discord Bot Class and Run it

    bot = LaSaga_Bot()
    bot.run(TOKEN)