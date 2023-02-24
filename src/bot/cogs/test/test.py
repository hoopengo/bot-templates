import nextcord
from nextcord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(description="A test command!")
    async def test(self, interaction: nextcord.Interaction):
        """A test command that sends a message saying 'work good!'"""
        await interaction.send("work good!")
