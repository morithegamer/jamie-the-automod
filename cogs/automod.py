
import discord
from discord.ext import commands
import re
import json
import os

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_settings()

    def load_settings(self):
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as f:
                self.settings = json.load(f)
        else:
            self.settings = {
                "spam_threshold": 5,
                "warn_threshold": 3,
                "mute_threshold": 5,
                "kick_threshold": 7,
                "ban_threshold": 10,
                "log_channel": None,
                "banned_words": [],
                "regex_filters": []
            }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # Spam Detection (5 messages in 10 seconds)
        await self.check_spam(message)

        # Banned Words Detection
        for word in self.settings["banned_words"]:
            if word.lower() in message.content.lower():
                await message.delete()
                await self.warn_user(message.author, message.guild)
                return

        # Regex Filtering
        for pattern in self.settings["regex_filters"]:
            if re.search(pattern, message.content):
                await message.delete()
                await self.warn_user(message.author, message.guild)
                return

    async def check_spam(self, message):
        author_id = str(message.author.id)
        if author_id not in self.settings.get("user_warnings", {}):
            self.settings["user_warnings"][author_id] = {"warnings": 0, "messages": []}

        self.settings["user_warnings"][author_id]["messages"].append(message.created_at.timestamp())

        # Remove old messages (10 seconds)
        self.settings["user_warnings"][author_id]["messages"] = [
            t for t in self.settings["user_warnings"][author_id]["messages"] 
            if (message.created_at.timestamp() - t) <= 10
        ]

        if len(self.settings["user_warnings"][author_id]["messages"]) > self.settings["spam_threshold"]:
            await self.warn_user(message.author, message.guild)
            self.settings["user_warnings"][author_id]["messages"] = []

    async def warn_user(self, user, guild):
        author_id = str(user.id)
        if author_id not in self.settings.get("user_warnings", {}):
            self.settings["user_warnings"][author_id] = {"warnings": 0}

        self.settings["user_warnings"][author_id]["warnings"] += 1

        if self.settings["log_channel"]:
            log_channel = self.bot.get_channel(self.settings["log_channel"])
            if log_channel:
                await log_channel.send(f"{user.mention} warned. Warnings: {self.settings['user_warnings'][author_id]['warnings']}")

        self.save_settings()

    def save_settings(self):
        with open("settings.json", "w") as f:
            json.dump(self.settings, f)

async def setup(bot):
    await bot.add_cog(AutoMod(bot))
