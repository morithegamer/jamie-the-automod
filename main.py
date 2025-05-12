
import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded: {filename}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(
        activity=discord.Game(name="Jamie Being a Cute Automod~"),
        status=discord.Status.online
    )
    try:
        await bot.tree.sync()
        print("✅ Slash Commands Synced.")
    except Exception as e:
        print(f"❌ Error syncing Slash Commands: {e}")

async def main():
    try:
        await load_cogs()
        await bot.start(os.getenv("DISCORD_TOKEN"))
    except Exception as e:
        print(f"🚨 Critical Error: {e}")

asyncio.run(main())
