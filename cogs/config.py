
import discord
from discord import app_commands
from discord.ext import commands
import json
import os

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings_file = "settings.json"
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                return json.load(f)
        else:
            return {"log_channel": None, "nsfw_keywords": ["porn", "xxx", "hentai", "nsfw", "lewd"]}

    def save_settings(self):
        with open(self.settings_file, "w") as f:
            json.dump(self.settings, f, indent=4)

    @app_commands.command(name="config", description="View and change Jamie's settings in real-time.")
    async def config(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Jamie Config - Current Settings",
            description="Here are the current settings you can manage:",
            color=discord.Color.blue()
        )
        embed.add_field(name="Log Channel", value=f"<#{self.settings.get('log_channel', 'Not Set')}>", inline=False)
        embed.add_field(name="NSFW Keywords", value=", ".join(self.settings.get("nsfw_keywords", [])), inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="setlog", description="Set the logging channel for Jamie.")
    async def set_log_channel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        self.settings["log_channel"] = channel.id
        self.save_settings()
        await interaction.response.send_message(f"✅ Logging channel set to {channel.mention}.")

    @app_commands.command(name="addnsfw", description="Add an NSFW keyword to the list.")
    async def add_nsfw(self, interaction: discord.Interaction, keyword: str):
        if keyword.lower() not in self.settings["nsfw_keywords"]:
            self.settings["nsfw_keywords"].append(keyword.lower())
            self.save_settings()
            await interaction.response.send_message(f"✅ Added NSFW keyword: `{keyword}`")
        else:
            await interaction.response.send_message(f"⚠️ That keyword is already in the list.")

    @app_commands.command(name="removensfw", description="Remove an NSFW keyword.")
    async def remove_nsfw(self, interaction: discord.Interaction, keyword: str):
        if keyword.lower() in self.settings["nsfw_keywords"]:
            self.settings["nsfw_keywords"].remove(keyword.lower())
            self.save_settings()
            await interaction.response.send_message(f"✅ Removed NSFW keyword: `{keyword}`")
        else:
            await interaction.response.send_message(f"❌ Keyword not found.")

async def setup(bot):
    await bot.add_cog(Config(bot))
