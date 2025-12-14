import discord
from dotenv import load_dotenv
import os
import discord.ext.commands as commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# print(f"Mein Token ist: {token}")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}') 
    
bot.run(token)
