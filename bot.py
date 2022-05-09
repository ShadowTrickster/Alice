import os
import nextcord
from nextcord.ext import commands
from nextcord.utils import get
import config

import Commands

def main():
    intents = nextcord.Intents.default()

    client = commands.Bot(command_prefix=config.PREFIX, intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user.name} a despertado apropiadamente")

    for folder in os.listdir("Commands"):
        if os.path.exists(os.path.join("Commands", folder, "commands.py")):
            client.load_extension(f"Commands.{folder}.commands")

    client.run(config.BOT_TOKEN)

if __name__ == '__main__':
    main()