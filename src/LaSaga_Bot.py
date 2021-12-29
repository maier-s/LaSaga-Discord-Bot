import discord
from discord.ext import commands
import Com_Bot
from inspect import getmembers
from Com_Bot import *

class LaSaga_Bot(commands.Bot):
    def __init__(self)->None:

        #Set some security settings
        intend = discord.Intents.default()
        intend.members = True

        #Initialize the Command Bot
        super().__init__(command_prefix = "$",intents =intend)

        #Initialize commands that are registered for the bot
        self.init_commands()
        
        
    def init_commands(self)->None:
        #Be carefull eval function is used that resolves unsecure strings!
        #Todo find better solution for eval function
        com_functions = []
        for object in getmembers(Com_Bot):
            if type(object[1]) == discord.ext.commands.core.Command:
                com_functions.append(eval(object[0]))
        for com in com_functions:
            super().add_command(com)

    #Overwrrite on_ready method of super class
    async def on_ready(self):
        # assume that the first registert server is the originally la saga server!
        members = '\n - '.join([member.name for member in self.guilds[0].members])
        print(
            f'{self.user} is connected to the following guild:\n'
            f'{self.guilds[0].name}(id: {self.guilds[0].id})\n'
            f'Guild Members:\n - {members}')


