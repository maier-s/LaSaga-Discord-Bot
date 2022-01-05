from discord.ext import commands

@commands.command(name="test")
async def test(ctx,args):
        await ctx.send(args)

@commands.command(name="fu")
async def fu(ctx):
        await ctx.send("You too!")