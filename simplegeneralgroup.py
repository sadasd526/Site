import discord
from discord import app_commands as apc
class Generalgroup(apc.Group):
    """Manage general commands"""
    def __init__(self, bot: discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message('Hello')

    @apc.command()
    async def version(self, interaction: discord.Interaction):
        """tells you what version of the bot software is running."""
        await interaction.response.send_message('This is an untested test version')