
import discord
from discord import app_commands
from discord.ext import commands
import re

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.regex_filters = [
            r"https?://.*steamunlocked\.net.*", 
            r"https?://.*free-steam-games\.com.*",
            r"https?://.*epicfreegames\.com.*",
            r"https?://.*giftcardgenerator\.com.*",
            r"https?://.*freerobux\.com.*",
        ]
        self.nsfw_keywords = ["porn", "xxx", "hentai", "nsfw", "lewd"]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # Phishing Detection
        for pattern in self.regex_filters:
            if re.search(pattern, message.content):
                await message.delete()
                await message.channel.send(f"{message.author.mention}, this link is blocked for safety.")
                return

        # NSFW Link Detection
        for keyword in self.nsfw_keywords:
            if keyword in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention}, NSFW content is not allowed.")
                return

    @app_commands.command(name="addregex", description="Add a regex filter to block links or patterns.")
    async def add_regex(self, interaction: discord.Interaction, pattern: str):
        if pattern not in self.regex_filters:
            self.regex_filters.append(pattern)
            await interaction.response.send_message(f"✅ Added regex filter: `{pattern}`")
        else:
            await interaction.response.send_message(f"⚠️ That regex filter is already in use.")

    @app_commands.command(name="removeregex", description="Remove a regex filter.")
    async def remove_regex(self, interaction: discord.Interaction, pattern: str):
        if pattern in self.regex_filters:
            self.regex_filters.remove(pattern)
            await interaction.response.send_message(f"✅ Removed regex filter: `{pattern}`")
        else:
            await interaction.response.send_message(f"❌ Regex filter not found.")

    @app_commands.command(name="phishinglist", description="View all blocked phishing domains.")
    async def phishing_list(self, interaction: discord.Interaction):
        if self.regex_filters:
            filters_list = "
".join(self.regex_filters)
            await interaction.response.send_message(f"🚨 Blocked Phishing Domains:
```{filters_list}```")
        else:
            await interaction.response.send_message("✅ No phishing domains are currently blocked.")

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.tree.add_command(self.add_regex)
        self.bot.tree.add_command(self.remove_regex)
        self.bot.tree.add_command(self.phishing_list)
        print("✅ AutoMod Regex and NSFW Slash Commands Registered.")

async def setup(bot):
    await bot.add_cog(AutoMod(bot))
