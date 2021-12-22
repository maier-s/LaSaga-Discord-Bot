import os
from LaSaga_Bot import LaSaga_Bot
from dotenv import load_dotenv

def setup():
    load_dotenv()

if __name__ == "__main__":
    #setup environment
    setup()

    #load neccessary data
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    # Create Discord Bot Class and Run it

    bot = LaSaga_Bot()
    bot.run(TOKEN)