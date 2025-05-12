
import discord
from discord.ext import commands

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = discord.utils.get(message.guild.text_channels, name="logs")
        if channel:
            await channel.send(f"Message deleted: {message.content} (By {message.author.mention})")

async def setup(bot):
    await bot.add_cog(Logging(bot))
