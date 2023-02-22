import nextcord.ext.commands as commands

from .test import TestCog

def register_all_cogs(bot: commands.Bot) -> None:
    # Tuple containing all the cogs to register
    cogs = (TestCog,)

    # Loop through each cog and register it with the bot
    for cog in cogs:
        bot.add_cog(cog(bot))
