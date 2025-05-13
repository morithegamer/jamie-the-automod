
import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f"Pong! 🏓 {round(self.bot.latency * 1000)}ms")

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send(
            f"User Info for {member}:
"
            f"ID: {member.id}
"
            f"Joined: {member.joined_at}"
        )

    @commands.command(name="serverinfo")
    async def serverinfo(self, ctx):
        guild = ctx.guild
        await ctx.send(
            f"Server Info:
"
            f"Name: {guild.name}
"
            f"Members: {guild.member_count}"
        )

async def setup(bot):
    await bot.add_cog(Utilities(bot))
