import discord
from dotenv import load_dotenv
import os
import discord.ext.commands as commands
import logging

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# print(f"Mein Token ist: {token}")

# Logging handler:
handler = logging.FileHandler(filename='discordBot.log', encoding='utf-8', mode='w')


intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}') 
    
    


    
    
    
    
    
    
bot.run(token, log_handler=handler, log_level=logging.DEBUG)

