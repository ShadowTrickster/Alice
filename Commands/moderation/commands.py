from distutils import config
from http import client
import nextcord
from nextcord.ext import commands
from config import GUILD_ID
from .role_view import RoleView   

class Administracion(commands.Cog, name="Administracion"):
    """Administration and moderation commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Activate the rol message"""
        self.bot.add_view(RoleView())

    @commands.command()
    @commands.is_owner()                                        #permite que solo el owner lo ejecute               #Permite que solo los admin lo ejecuten
    async def roles(self, ctx: commands.Context):
        """Lets you activate the Rol bottom"""
        await ctx.send("Press here to become an Aspect and begin your adventure!", view=RoleView())

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.context, user: nextcord.Member):
        """Kicks a member from the server"""
        try:
            if user == None:
                await ctx.send("Please mention a user")
                return

            await user.kick()
            await ctx.send(f" {user.name} has been kicked :( ")
        except Exception:
            await ctx.send("Please mention a valid user")

#setup
def setup(bot):
    bot.add_cog(Administracion(bot))