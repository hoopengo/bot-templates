from nextcord.ext.commands import Bot

from .test import TestCog


def register_all_cogs(bot: Bot) -> None:
    cogs = (TestCog,)
    for cog in cogs:
        bot.add_cog(cog(bot))
