
import discord
from discord.ext import commands

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings = {
            "spam_threshold": 5,
            "warn_threshold": 3,
            "banned_words": ["badword"],
            "log_channel": None
        }

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setlog(self, ctx, channel: discord.TextChannel):
        self.settings["log_channel"] = channel.id
        await ctx.send(f"Logging channel set to {channel.mention}.")

    @commands.command()
    async def settings(self, ctx):
        await ctx.send(str(self.settings))

async def setup(bot):
    await bot.add_cog(Settings(bot))
