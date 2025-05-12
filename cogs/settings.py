
import discord
from discord.ext import commands
import json
import os

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings_file = "settings.json"
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                return json.load(f)
        else:
            return {"log_channel": None}

    def save_settings(self):
        with open(self.settings_file, "w") as f:
            json.dump(self.settings, f)

    @commands.command()
    async def setlog(self, ctx, channel: discord.TextChannel):
        self.settings["log_channel"] = channel.id
        self.save_settings()
        await ctx.send(f"✅ Logging channel set to {channel.mention}.")

async def setup(bot):
    await bot.add_cog(Settings(bot))
