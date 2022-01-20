from discord.ext import commands
from discord.ext.commands.core import command
from W2G import W2G
from dotenv import load_dotenv
import os

load_dotenv()
W2G_TOKEN = os.getenv('W2G_TOKEN')

@commands.command(name="test")
async def test(ctx,args):
        await ctx.send(args)

@commands.command(name="fu")
async def fu(ctx):
        await ctx.send("You too!")
@commands.command(name="w2g")
async def w2g(ctx, arg1=None, arg2=None,arg3 = None):
        W2G_Handler = W2G(W2G_TOKEN)
        if arg1 == "create":
                link,streamkey = W2G_Handler.makeRoom(arg2)
                await ctx.send(f'Your Streamkey is: {streamkey} \nHere is your Room: {link}')
        elif arg1  == "update":
                if W2G_Handler.updateRoom(arg2,arg3):
                        await ctx.send(f'Update sucessfull on Room: {arg2}')
                        return
                else:
                        await ctx.send(f'Somthing went wrong using the following information to update room \nStreamkey:{arg2}\nURL:{arg3}')
        else:
                # Write some more instrutions
                await ctx.send(f'command {arg1} not found!')