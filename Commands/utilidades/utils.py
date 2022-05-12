import re
import nextcord
import config

def custom_id(view: str, id: int) -> str:
    """Gives the View in ID"""
    return f"{config.BOT_NAME}:{view}:{id}"