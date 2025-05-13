
import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    async def eight_ball(self, ctx, *, question: str):
        responses = [
            "Yes.", "No.", "Maybe.", "Absolutely!", "Never.", "Ask again later."
        ]
        await ctx.send(f"🎱 {random.choice(responses)}")

    @commands.command(name="coinflip")
    async def coinflip(self, ctx):
        await ctx.send(f"🪙 {random.choice(['Heads', 'Tails'])}")

    @commands.command(name="roll")
    async def roll(self, ctx, sides: int = 6):
        result = random.randint(1, sides)
        await ctx.send(f"🎲 You rolled a {result}.")

async def setup(bot):
    await bot.add_cog(Fun(bot))
