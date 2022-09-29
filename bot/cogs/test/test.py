import nextcord
from nextcord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.bot = client
        
    @nextcord.slash_command()
    async def test(self, inter):
    	await inter.send("work good!")
