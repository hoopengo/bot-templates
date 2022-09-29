import nextcord
from nextcord.ext import commands

from bot.cogs import register_all_cogs
from bot.misc.config import config

bot = commands.Bot(
    commands.when_mentioned_or(config.CMD_PREFIX),
    intents=nextcord.Intents.all(),
)


@bot.event
async def on_ready():
    """При включении бота"""

    print("INFO", "Change presence..")
    activity = nextcord.Streaming(
        name=f"травоман такой зайка",
        url="https://www.twitch.tv/tpabomah",
        type=3,
    )
    await bot.change_presence(status=nextcord.Status.dnd, activity=activity)
    print("DONE", "Change presence - DONE")

    print(
        "DONE",
        f"Bot started at {bot.user.name}#{bot.user.discriminator}\n|\
 {config.TOKEN=}\n",
    )

if __name__ == "__main__":
    register_all_cogs(bot)
    bot.run(config.TOKEN)
