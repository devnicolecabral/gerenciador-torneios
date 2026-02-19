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
bot = commands.Bot(command_prefix="!", intents=intents)

