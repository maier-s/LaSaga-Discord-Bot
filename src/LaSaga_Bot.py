import discord

class LaSaga_Bot(discord.Client):
    def __init__(self, *, loop=None, **options):
        #Referces to https://stackoverflow.com/questions/64148371/discord-bot-can-only-see-itself-and-no-other-users-in-guild
        intend = discord.Intents.default()
        intend.members = True

        # Initialize Base Class
        super().__init__(loop=loop,intents = intend ,**options)
    async def on_ready(self):
        # assume that the first registert server is the originally la saga server!
        members = '\n - '.join([member.name for member in self.guilds[0].members])
        print(
            f'{self.user} is connected to the following guild:\n'
            f'{self.guilds[0].name}(id: {self.guilds[0].id})\n'
            f'Guild Members:\n - {members}')