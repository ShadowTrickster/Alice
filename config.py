import os

#Bot Basics
PREFIX = ";"
BOT_NAME = "Alice"
BOT_TOKEN = os.getenv("DISCORD_TOKEN", "")

#Guild
GUILD_ID = int(os.getenv("GUILD_ID", ""))
TWITCH_CH= int(os.getenv("TWITCH_CH_ID", ""))

#Discord Roles ID
ASPECTO_ID = int(os.getenv("ASPECTO_ID", ""))
CELESTIAL_ID = int(os.getenv("CELESTIAL_ID", ""))
STREAMER_ID = int(os.getenv("STREAMER_ID", ""))
