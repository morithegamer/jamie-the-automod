
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs dynamically
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded: {filename}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.loop.create_task(load_cogs())
bot.run(os.getenv("DISCORD_TOKEN"))
