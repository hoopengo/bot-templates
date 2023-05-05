import disnake
from disnake.ext import commands


class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="A test command!")
    async def test(self, interaction: disnake.ApplicationCommandInteraction):
        """A test command that sends a message saying 'work good!'"""
        await interaction.send("work good!")
