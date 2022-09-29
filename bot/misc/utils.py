from random import randint
import nextcord


def random_guild_emoji(guild: nextcord.Guild):
    if len(guild.emojis) < 1:
        return r"🤡"

    return guild.emojis[randint(0, len(guild.emojis) - 1)]
