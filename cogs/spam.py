
import discord
from discord import app_commands
from discord.ext import commands

class SpamDetection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spam_threshold = 5
        self.user_messages = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        user_id = str(message.author.id)
        if user_id not in self.user_messages:
            self.user_messages[user_id] = []

        self.user_messages[user_id].append(message.created_at.timestamp())

        # Remove old messages (10 seconds)
        self.user_messages[user_id] = [t for t in self.user_messages[user_id] if (message.created_at.timestamp() - t) <= 10]

        if len(self.user_messages[user_id]) > self.spam_threshold:
            await message.channel.send(f"{message.author.mention}, please avoid spamming.")

async def setup(bot):
    await bot.add_cog(SpamDetection(bot))
