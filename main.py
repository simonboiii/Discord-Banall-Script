import os

try:
  import discord, threading
except:
  os.system('pip install discord')
  os.system('pip install threading')
  
import discord
import threading
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = 'put your bot token here'

@client.event
async def on_connect():
    print('bot is ready for banning')

@client.command()
@commands.is_owner()
async def banall(ctx):
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason='banall')
        await ctx.send(f'Banned {member}')
      except:
        await ctx.send(f'Unable to ban {member}')
    
    for i in range(int(50)):
       t = threading.Thread(target=banall).start

client.run(token, bot=True)
