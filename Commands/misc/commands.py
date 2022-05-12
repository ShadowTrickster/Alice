from nextcord.ext import commands

class Misc(commands.Cog, name="Misc"):
    """Commands with no specific category"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command("ping")
    async def ping(self, ctx:commands.Context):
        """Tests the response time of the bot"""
        await ctx.send("Pong")
  
def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))