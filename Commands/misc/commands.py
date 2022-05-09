from nextcord.ext import commands

class Misc(commands.Cog, name="Misc"):
    """Comandos sin categoria especifica"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command("ping")
    async def ping(self, ctx:commands.Context):
        """Prueba el tiempo de respuesta del bot"""
        await ctx.send("Pong")
  
def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))