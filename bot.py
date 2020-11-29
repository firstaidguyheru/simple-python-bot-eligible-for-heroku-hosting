import discord
from discord.ext import commands
from asyncio import sleep
client = commands.Bot(command_prefix='-', help_command=None)


async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='1'))
        await sleep(5)
        await client.change_presence(activity=discord.Game(name='2'))
        await sleep(5)
        await client.change_presence(activity=discord.Game(name='3'))
        await sleep(5) ## take off if you want.
        
@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
    await client.loop.create_task(status())


@client.command(name='hi', aliases=['Hi'])
async def hi_cmd(ctx):
    await ctx.channel.send('hi bot user.')

@client.event
async def on_member_join(member):
    mbed = discord.Embed(
        colour = (discord.Colour.magenta()),
        title = 'Welcome Message',
        description = f'Welcome {member.mention}, enjoy your stay!'
    )
    await member.send(embed=mbed)
    
token = ''

{
    client.run(token)
}
