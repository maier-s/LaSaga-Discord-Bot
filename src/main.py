from logging import lastResort
import os
import discord
from dotenv import load_dotenv

def setup():
    load_dotenv()
class LaSaga_Bot(discord.Client):
    async def on_ready(self):
        # assume that the first registert server is the originally la saga server!
        members = '\n - '.join([member.name for member in self.guilds[0].members])
        print(
            f'{self.user} is connected to the following guild:\n'
            f'{self.guilds[0].name}(id: {self.guilds[0].id})\n'
            f'Guild Members:\n - {members}')
if __name__ == "__main__":
    #setup environment
    setup()

    #load neccessary data
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    # Declaration of Discord Bot functionallity

    #Referces to https://stackoverflow.com/questions/64148371/discord-bot-can-only-see-itself-and-no-other-users-in-guild
    intend = discord.Intents.default()
    intend.members = True

    bot = LaSaga_Bot(intents=intend)
    bot.run(TOKEN)