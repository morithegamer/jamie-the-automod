
import discord
from discord import app_commands
from discord.ext import commands
import re
import json
import os

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings_file = "settings.json"
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                settings = json.load(f)
                self.nsfw_keywords = settings.get("nsfw_keywords", [])
                self.phishing_domains = settings.get("phishing_domains", [])
        else:
            self.nsfw_keywords = ["porn", "xxx", "hentai", "nsfw", "lewd"]
            self.phishing_domains = [
                r"https?://.*steamunlocked\.net.*",
                r"https?://.*free-steam-games\.com.*",
                r"https?://.*epicfreegames\.com.*",
                r"https?://.*giftcardgenerator\.com.*",
                r"https?://.*freerobux\.com.*"
            ]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # ✅ Respecting NSFW (Age-Restricted) Channels
        if message.channel.is_nsfw():
            return  # Skip filtering in NSFW channels

        # NSFW Detection (Direct from settings.json)
        for keyword in self.nsfw_keywords:
            if keyword.lower() in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention}, NSFW content is not allowed here.")
                return

        # Phishing Detection (Dynamic from settings.json)
        for pattern in self.phishing_domains:
            if re.search(pattern, message.content):
                await message.delete()
                await message.channel.send(f"{message.author.mention}, this link is blocked for safety.")
                return

    @app_commands.command(name="reloadsettings", description="Reload settings (NSFW Keywords & Phishing) without restarting.")
    async def reload_settings(self, interaction: discord.Interaction):
        self.load_settings()
        await interaction.response.send_message("✅ Settings reloaded.")

async def setup(bot):
    await bot.add_cog(AutoMod(bot))
