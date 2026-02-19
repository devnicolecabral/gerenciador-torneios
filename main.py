import os 
import discord
from discord.ext import commands 
from dotenv import load_dotenv

# Carrega as credenciais 
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Configura as permissões 
intents = discord.Intents.default()
intents.message_content = True

# Cria o bot e define que ele vai responder a comandos que começam com "!"
bot = commands.Bot(command_prefix="sam!", intents=intents)

# Evento conectar 
@bot.event
async def on_ready():
    print(f"Sucesso! O bot {bot.user.name} está pronto para uso.")
    print("--------------------------------------------------")

# Comando de teste
@bot.command()
async def oi(ctx):
    await ctx.send("Olá! Estou online e me preparando para puxar os dados da Challenger Mode! 🚀")

# 6. A última linha do arquivo: Ligar o bot usando o Token
bot.run(DISCORD_TOKEN)