import discord
from discord.ext import commands

from Com_Bot import test

class LaSaga_Bot(commands.Bot):
    def __init__(self):
        intend = discord.Intents.default()
        intend.members = True

        super().__init__(command_prefix = "$",intents =intend)
        super().add_command(test)
    
    async def on_ready(self):
        # assume that the first registert server is the originally la saga server!
        members = '\n - '.join([member.name for member in self.guilds[0].members])
        print(
            f'{self.user} is connected to the following guild:\n'
            f'{self.guilds[0].name}(id: {self.guilds[0].id})\n'
            f'Guild Members:\n - {members}')


