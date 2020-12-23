import os
from dotenv import load_env
import discord
from discord.ext import commands
from asyncio import sleep

client = commands.Bot(command_prefix='-', help_command=None)

load_env()

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='1'))
        await sleep(60*10)
        await client.change_presence(activity=discord.Game(name='2'))
        await sleep(60*10)
        await client.change_presence(activity=discord.Game(name='3'))
        await sleep(60*10) ## take off if you want.
        
@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
    await client.loop.create_task(status())


@client.command(name='hi', aliases=['Hi'])
async def hi_cmd(ctx):
    await ctx.send('hi bot user.')

@client.event
async def on_member_join(member):
    mbed = discord.Embed(
        colour = (discord.Colour.magenta()),
        title = 'Welcome Message',
        description = f'Welcome {member.mention}, enjoy your stay!'
    )
    await member.send(embed=mbed)
    

client.run(os.getenv('TOKEN'))

