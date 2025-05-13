
import discord
from discord import app_commands
from discord.ext import commands

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild:
            channel = discord.utils.get(message.guild.text_channels, name="logs")
            if channel:
                embed = discord.Embed(
                    title="Message Deleted 🚨",
                    description=f"**User:** {message.author.mention}\n**Content:** {message.content}",
                    color=discord.Color.red()
                )
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("✅ Logging System Active.")

async def setup(bot):
    await bot.add_cog(Logging(bot))
