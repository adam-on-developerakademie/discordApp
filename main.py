import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

print(f"Mein Token ist: {token}")

