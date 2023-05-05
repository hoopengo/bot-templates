import logging

import disnake
from disnake.ext import commands

from bot.cogs import register_all_cogs
from bot.misc.config import config


def main() -> None:
    # Set up logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    # Create a bot instance with intents
    intents = disnake.Intents.all()
    bot = commands.Bot(command_prefix=config.CMD_PREFIX, intents=intents)

    # Set up bot event listeners
    @bot.event
    async def on_ready() -> None:
        """Runs when the bot is ready"""
        logger.info("Bot is online.")
        activity = disnake.Streaming(
            name="травоман такой зайка",
            url="https://www.twitch.tv/tpabomah",
            type=disnake.ActivityType.streaming,
        )
        await bot.change_presence(status=disnake.Status.dnd, activity=activity)
        logger.info(
            f"Changed presence to {activity.type.name} "
            f"{activity.name} ({activity.url})."
        )
        logger.info(f"Bot started at {bot.user.name}#{bot.user.discriminator}.")

    # Register all cogs
    register_all_cogs(bot)

    # Start the bot
    if config.TOKEN:
        bot.run(config.TOKEN)
    else:
        logger.error("TOKEN not found in environment variables.")


if __name__ == "__main__":
    main()
