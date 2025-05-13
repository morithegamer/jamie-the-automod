
import discord
from discord.ext import commands
import json
import os

class Punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warnings_file = "warnings.json"
        self.load_warnings()

    def load_warnings(self):
        if os.path.exists(self.warnings_file):
            with open(self.warnings_file, "r") as f:
                self.warnings = json.load(f)
        else:
            self.warnings = {}

    def save_warnings(self):
        with open(self.warnings_file, "w") as f:
            json.dump(self.warnings, f, indent=4)

    @commands.command(name="warn")
    async def warn(self, ctx, member: discord.Member, reason="Violation of rules"):
        user_id = str(member.id)
        self.warnings[user_id] = self.warnings.get(user_id, 0) + 1
        self.save_warnings()
        await ctx.send(f"{member.mention} has been warned. Total Warnings: {self.warnings[user_id]}")

        if self.warnings[user_id] >= 3:
            await member.timeout(None, reason="3 Warnings Reached")
            await ctx.send(f"{member.mention} has been muted for reaching 3 warnings.")

async def setup(bot):
    await bot.add_cog(Punishments(bot))
