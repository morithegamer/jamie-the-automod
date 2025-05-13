
import discord
from discord import app_commands
from discord.ext import commands

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="status", description="Show the status of all loaded Cogs and Slash Commands.")
    async def status(self, interaction: discord.Interaction):
        loaded_cogs = list(self.bot.cogs.keys())
        if loaded_cogs:
            cogs_list = "\n".join(loaded_cogs)
            embed = discord.Embed(
                title="Jamie Status - Everything is running smoothly! 💙",
                description=f"✅ Loaded Cogs:\n```{cogs_list}```",
                color=discord.Color.green()
            )
        else:
            embed = discord.Embed(
                title="Jamie Status - Issues Detected! 🚨",
                description="❌ No Cogs are loaded. Please check the console for errors.",
                color=discord.Color.red()
            )
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Status(bot))
