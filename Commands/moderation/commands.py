from distutils import config
from http import client
from re import purge
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
    @commands.is_owner()                                        
    async def roles(self, ctx: commands.Context):
        """Lets you activate the Rol bottom"""
        await ctx.send("Press here to become an Aspect and begin your adventure!", view=RoleView())

    @commands.command("kick")
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

    @commands.command("purge")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx: commands.context, amount: int):
        """Deletes certain amount of messages
        
        example:
        ;purge 10
        """
        try:
            deleted = await ctx.channel.purge(limit=amount+1)
            await ctx.send(f"{len(deleted)-1} Messages have been purged")
        except:
            ctx.send("Something went wrong...somehow")
    @purge.error
    async def purge_error(error, ctx, exc):
        if isinstance(exc, nextcord.NotFound):
            await ctx.send("Something went wrong!")

#setup
def setup(bot):
    bot.add_cog(Administracion(bot))