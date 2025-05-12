
import discord
from discord.ext import commands

class Punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}

    @commands.command()
    async def warn(self, ctx, member: discord.Member, reason="Violation of rules"):
        if member.bot:
            return

        user_id = str(member.id)
        if user_id not in self.warnings:
            self.warnings[user_id] = 0

        self.warnings[user_id] += 1
        await ctx.send(f"{member.mention} has been warned. Total Warnings: {self.warnings[user_id]}")

        if self.warnings[user_id] >= 3:
            await member.timeout(discord.utils.utcnow(), reason="3 Warnings")
            await ctx.send(f"{member.mention} has been muted for repeated violations.")

async def setup(bot):
    await bot.add_cog(Punishments(bot))
