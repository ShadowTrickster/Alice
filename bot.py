import os
import discord
from nextcord import Activity, Guild
import nextcord
from nextcord.ext import commands
from nextcord.utils import get
import config
import nextcord
import logging

logger = logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def main():
    intents = nextcord.Intents.default()
    client = commands.Bot(command_prefix=config.PREFIX, 
    intents = intents, 
    activity = nextcord.Activity
    (type = nextcord.ActivityType.watching, 
    name = f"Millions of worlds!"),
    status = nextcord.Status.idle)

    @client.event
    async def on_ready():
        print(f"{client.user.name} a despertado apropiadamente")
       

    for folder in os.listdir("Commands"):
        if os.path.exists(os.path.join("Commands", folder, "commands.py")):
            client.load_extension(f"Commands.{folder}.commands")

    client.run(config.BOT_TOKEN)

if __name__ == '__main__':
    main()