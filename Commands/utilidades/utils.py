import re
import nextcord
import config

def custom_id(view: str, id: int) -> str:
    """Devuelve el view con el ID"""
    return f"{config.BOT_NAME}:{view}:{id}"