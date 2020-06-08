import discord
from discord.ext import commands


client=commands.Bot(command_prefix='uwu')


@client.event
async def on_ready():
    print('Bot ready')


client.run('NzE5NTg0NDgwODY3NjQ3NjM4.Xt5qLg.ucq07e3DhMc78DQhdzZEwc72n2o')