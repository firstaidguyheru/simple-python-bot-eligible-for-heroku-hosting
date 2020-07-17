import discord
from discord.ext import commands

client = commands.Bot(command_prefix='-', help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="I Am A Python Bot!"))
    print('I have Awoken!')

@client.command(name='hi', aliases=['Hi'])
async def hi_cmd(ctx):
    await ctx.channel.send('hi bot user.')

token = 'NzMwNjY0OTQzMTQ5MzgzNzAx.XxHnBQ.NSbmzNg44H3mWPbzXcfej5d8oUk'

{
    client.run(token)
}
