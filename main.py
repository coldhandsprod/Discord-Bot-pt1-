import discord
from discord.ext import commands
from datetime import datetime
import os

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_message(message):
  if isinstance(message.channel, discord.DMChannel):
    with open('dmshistory.txt', 'a') as dmshistory:
      dmshistory.write(f'''
{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
[DMS] {message.author}: {message.content}
''')
  return await bot.process_commands(message)

@bot.command()
async def example(ctx):
  return await ctx.send('Hey!')

bot.run(os.getenv('TOKEN'))
