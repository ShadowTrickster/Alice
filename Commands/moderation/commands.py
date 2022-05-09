from distutils import config
from http import client
import nextcord
from nextcord.ext import commands
from config import GUILD_ID
from .role_view import RoleView   

class Administracion(commands.Cog, name="Administracion"):
    """Commandos de administracion y moderacion"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """permite activar el mensaje que otorga o revoca el rol asignado"""
        self.bot.add_view(RoleView())

    @commands.command()
    #@commands.is_owner()                                        #permite que solo el owner lo ejecute
    @commands.has_permissions(administrator=True)                #Permite que solo los admin lo ejecuten
    async def roles(self, ctx: commands.Context):
        """Permite activar el mensaje que otorga o revoca el/los rol(es) asignado(s)"""
        await ctx.send("Presione el botton para volverse un Aspecto y comenzar su aventura!.", view=RoleView())

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.context, user: nextcord.Member):
        """Permite expulsar miembros del servidor"""
        try:
            if user == None:
                await ctx.send("Porfavor introduzca usuario")
                return

            await user.kick()
            await ctx.send(f" {user.name} a sido expulsado ")
        except Exception:
            await ctx.send("Porfavor mencione un usuario valido")

#setup
def setup(bot):
    bot.add_cog(Administracion(bot))