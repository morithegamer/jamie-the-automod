
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
        embed = discord.Embed(title=f"User Info for {member}", color=0x00ff00)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"), inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo")
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f"Server Info: {guild.name}", color=0x00ff00)
        embed.add_field(name="Members", value=guild.member_count, inline=False)
        embed.add_field(name="Owner", value=guild.owner, inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utilities(bot))
