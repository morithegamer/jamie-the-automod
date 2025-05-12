
import discord
from discord import app_commands
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="List all commands and their usage.")
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Jamie - Your Favorite AutoMod Bot 💙",
            description="Here are all the commands you can use with Jamie:",
            color=discord.Color.blue()
        )
        embed.add_field(name="/addregex <pattern>", value="Add a custom regex filter to block links or patterns.", inline=False)
        embed.add_field(name="/removeregex <pattern>", value="Remove an existing regex filter.", inline=False)
        embed.add_field(name="/phishinglist", value="View all blocked phishing domains.", inline=False)
        embed.add_field(name="/setlog <#channel>", value="Set the logging channel for Jamie.", inline=False)
        embed.add_field(name="/settings", value="View current AutoMod settings.", inline=False)
        embed.add_field(name="/help", value="Show this help message.", inline=False)
        embed.set_footer(text="Jamie - Keeping your server safe 💙")
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
