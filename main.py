import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random
import pip
import sys
import io

# --- INFO 
token = "DISCORD_TOKEN_HERE"
id_server = 555555555555555555 # ID OF YOUR SERVER
# --- END INFO

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!!!!!!", intents=intents)

intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@bot.event
async def on_ready():

  print("BOT RUNNING SUCCES")
  try:
    synced = await bot.tree.sync(guild=discord.Object(id=id_server))
  except Exception as e:
    print(e)

@bot.event
@bot.event
async def on_message(message):
  if message.author == bot.user:
        return

  if bot.user in message.mentions:
        async with message.channel.typing():
          a = message.content.replace(bot.user.mention, '').strip()
          if a.startswith("!pip_install"):
             try:
                pip.main(['install',a.replace("!pip_install",'').strip()])
                await message.channel.send(f"Package {a.replace('!pip_install','').strip()} is successfully installed {message.author.mention}")
             except Exception as e:
                await message.channel.send(f"Error PIP :\n```\n{str(e)}\n```\n {message.author.mention}")
          else:
             
             old_stdout = sys.stdout
             new_stdout = io.StringIO()
             sys.stdout = new_stdout
             exec(a)
             output = new_stdout.getvalue()
             sys.stdout = old_stdout
             if len(str(output)) > 4000:
            
                parts = [str(output)[i:i + 4000] for i in range(0, len(str(output)), 4000)]
                for part in parts:
                   await message.channel.send(f"Output :\n```\n{str(part)}\n```\n {message.author.mention}")
             else:
                await message.channel.send(f"Output :\n```\n{str(output)}\n```\n {message.author.mention}")

bot.run(token)
