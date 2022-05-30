from nextcord.ext import commands
import random
from nextcord.errors import HTTPException

class Fun(commands.Cog, name="Fun"):
    """Fun Commands"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

################## ROLL COMMAN BREAKS THE WHOLE SHIT WHEN OVER 1000ROLLS, NEEDS FIXING#####################
    # @commands.command("roll")
    # async def roll(self, ctx: commands.Context, dice: str):
    #     """Roll a dice in _d_ format
        
    #     Example:
    #     ;roll 8d7"""

    #     try:
    #         rolls = ""
    #         total = 0
    #         amount, die = dice.split ("d")
    #         for _ in range(int(amount)):
    #             roll = random.randint(1, int(die))
    #             total += roll
    #             rolls += f"{roll} "
    #         await ctx.send(f"Rolls: {rolls}\nTotal: {total}")
    #     except ValueError:
    #         await ctx.send ("The roll must be in NdN format")
    #     except commands.MissingRequiredArgument:
    #         await ctx.send("Please insert a valid numerical number")
    
    # @roll.error
    # async def roll_error(error, ctx, exc):
    #     if isinstance(exc, commands.MissingRequiredArgument):
    #         await ctx.send("Please insert valid numerical values")
    #     else:   
    #         await ctx.send("Something went wrong, please try again")

    @commands.command("choose")
    async def choose(self, ctx: commands.Context, *args):
        """Choose between multiple options given

        Example:
        ;choose A B C D E"""

        try:
            choice = random.choice(args)
            await ctx.send(choice)
        except IndexError:
            await ctx.send("Please insert valid targets to choose from")


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))