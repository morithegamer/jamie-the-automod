
import discord
from discord.ext import commands
import json
import os
import re

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings_file = "settings.json"
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                self.settings = json.load(f)
        else:
            self.settings = {
                "nsfw_keywords": [],
                "phishing_domains": [],
                "regex_patterns": [r"(https?://[^\s]+)"],
                "mention_limit": 5,
                "safe_mode": False,
                "anti_raid_threshold": 5
            }
            self.save_settings()

    def save_settings(self):
        with open(self.settings_file, "w") as f:
            json.dump(self.settings, f, indent=4)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.settings.get("anti_raid_threshold"):
            guild = member.guild
            join_times = getattr(guild, "join_times", [])
            join_times.append(member.joined_at.timestamp())
            guild.join_times = join_times[-10:]
            if len(join_times) >= self.settings["anti_raid_threshold"]:
                await guild.system_channel.send("🚨 Possible Raid Detected!")

async def setup(bot):
    await bot.add_cog(AutoMod(bot))
