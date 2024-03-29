import random

import nextcord


def random_guild_emoji(guild: nextcord.Guild) -> str:
    """Returns a random emoji from the given guild."""
    if not guild.emojis:
        return "🤡"  # Clown emoji as fallback

    random_emoji = random.choice(guild.emojis)
    return str(random_emoji)  # Convert the emoji to a string for consistent return type
