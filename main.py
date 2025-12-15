import discord
from dotenv import load_dotenv
import os
import discord.ext.commands as commands
import logging

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# print(f"Mein Token ist: {token}")

# Loging handler:
handler = logging.FileHandler(filename='discordBot.log', encoding='utf-8', mode='w')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event # Ereignis, wenn der Bot bereit ist
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}') # Begrüßungsbefehl
    
@bot.command() 
async def hallo(ctx):
    await ctx.send(f'Hallo {ctx.author} wie kann ich dir helfen?')   # Einfache Begrüßung wenn der Befehl !hallo eingegeben wird
    
    
@bot.command()
async def msg(ctx, arg ):
    await ctx.send(f'OK {ctx.author} du hast mir gesagt: {arg}')   # Bot wiederholt die Nachricht die nach !msg eingegeben wird



@bot.command()      # Befehl zum Hinzufügen einer Rolle
async def addRole(ctx, new_role = "Neue-Rolle"):
    member = discord.utils.get(ctx.guild.members, id=ctx.author.id)
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role is None:
        await ctx.send(f'Rolle {new_role} existiert nicht!')
        return
    await member.add_roles(role)
    await ctx.send(f'Rolle {new_role} wurde zu {ctx.author} hinzugefügt!')
    
new_role = "Neue-Rolle"
@bot.command()     # Befehl zum Entfernen einer Rolle   
async def removeRole(ctx, new_role = "Neue-Rolle"):
    member = discord.utils.get(ctx.guild.members, id=ctx.author.id)
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role is None:
        await ctx.send(f'Rolle {new_role} existiert nicht!')
        return
    await member.remove_roles(role)
    await ctx.send(f'Rolle {new_role} wurde von {ctx.author} entfernt!')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Vermeide, auf eigene Nachrichten zu reagieren

    if "banana" in message.content.lower():
        await message.delete() # Lösche die Nachricht mit "banana"
        channel = message.channel # Hole den Kanal, in dem die Nachricht gesendet wurde
        await channel.send(f"Banana is nur DA Schüler erlaubt! 🍌 {message.author}") #ersetze die nachricht entsprechend 

    await bot.process_commands(message)  # Stelle sicher, dass Befehle weiterhin/widerhold verarbeitet werden
    
    
    
    
    
bot.run(token, log_handler=handler, log_level=logging.DEBUG)

