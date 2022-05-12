from nextcord.ext import commands
import random

class Fun(commands.Cog, name="Fun"):
    """Fun Commands"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command("roll")
    async def roll(self, ctx: commands.Context, dice: str):
        """Roll a dice in _d_ format
        
        Example:
        ;roll 8d7"""

        try:
            rolls = ""
            total = 0
            amount, die = dice.split ("d")
            for _ in range(int(amount)):
                roll = random.randint(1, int(die))
                total += roll
                rolls += f"{roll} "             
            await ctx.send(f"Rolls: {rolls}\nTotal: {total}")
        except ValueError:
            await ctx.send ("El dado debe ser en formato de NdN, por ejemplo 1d2")
        except Exception:
            await ctx.send("Algo salio mal, intentelo nuevamente con diferentes valores")

    @commands.command("choose")
    async def choose(self, ctx: commands.Context, *args):
        """Choose between multiple options given

        Example:
        ;choose A B C D E"""
        try:
            choice = random.choice(args)
            await ctx.send(choice)
        except IndexError:
            await ctx.send("Porfavor introduzca Valores para selecionar")

def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))