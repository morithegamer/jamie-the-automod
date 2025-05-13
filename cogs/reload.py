
import discord
from discord import app_commands
from discord.ext import commands

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="reload", description="Reload a specific Cog or all Cogs without restarting the bot.")
    @app_commands.describe(cog="The name of the Cog you want to reload (leave blank for all).")
    async def reload(self, interaction: discord.Interaction, cog: str = None):
        if cog:
            try:
                await self.bot.reload_extension(f"cogs.{cog}")
                await interaction.response.send_message(f"✅ Reloaded Cog: `{cog}.py`")
            except Exception as e:
                await interaction.response.send_message(f"❌ Failed to reload `{cog}`: {e}")
        else:
            # Reloading all Cogs
            reloaded_cogs = []
            for filename in self.bot.extensions.keys():
                if filename.startswith("cogs."):
                    try:
                        await self.bot.reload_extension(filename)
                        reloaded_cogs.append(filename)
                    except Exception as e:
                        await interaction.response.send_message(f"❌ Failed to reload `{filename}`: {e}")

            if reloaded_cogs:
                await interaction.response.send_message(f"✅ Reloaded Cogs: {', '.join(reloaded_cogs)}")
            else:
                await interaction.response.send_message("❌ No Cogs were reloaded.")

async def setup(bot):
    await bot.add_cog(Reload(bot))
