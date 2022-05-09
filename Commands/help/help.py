from typing import Optional
from nextcord.ext import commands
from nextcord import Embed

class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return f"{self.context.clean_prefix}{command.qualified_name} {command.signature}"

    async def _help_embed(self, title: str, description: Optional[str] = None, mapping: Optional[str] = None, 
    command_set: Optional[set[commands.command]] = None): 

        embed = Embed(title=title)
        if description:
            embed.description = description
        avatar = self.context.bot.user.avatar or self.context.bot.user.default_avatar
        embed.set_author(name=self.context.bot.user.name, icon_url=avatar.url)
        
        if command_set:
            #Muestra ayuda de todos los comandos en el set
            filtered = await self.filter_command(command_set, sort=True)
            for command in filtered: embed.add_field(
                name=self.get_command_signature(command), 
                value = command.short_doc or ". . .", 
                inline=False
                )

        elif mapping:
            #Da una descripcion de comandos en cada cog
            for cog, command_set in mapping.items():
                filtered = await self.filter_commands(command_set, sort=True)          #Esto permite filtrar comandos basados en rol, por ejemplo admin only commands
                if not filtered:
                    continue
                name = cog.qualified_name if cog else "No category"
                #\u2002 is an en-space
                cmd_list = "\u2002".join(
                    f"`{self.context.clean_prefix}{cmd.name}`" for cmd in filtered
                )
                value = (
                    f"{cog.description}\n{cmd_list}"
                    if cog and cog.description
                    else cmd_list
                )
                embed.add_field(name=name, value=value)
        return embed


    async def send_bot_help(self, mapping: dict):                         #esto creara un mapping. dict tiene los cog y su respectiva comandos
        embed = await self._help_embed(
            title = "Comandos",
            description=self.context.bot.description,
            mapping=mapping
        )
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command: commands.Command):        #esta opcion da informacion de un comando en especifico y lo que hace
        embed = await self._help_embed(
            title = command.qualified_name,
            description = command.help,
            command_set = command.commands if isinstance(command, commands.Group) else None
        )
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog:commands.Cog):                     #este envia info en el cog y una pequeña desc de los comandos
        embed = await self._help_embed(
            title = cog.qualified_name,
            description = cog.description,
            mapping = cog.get_commands()
        )
        await self.get_destination().send(embed=embed)

    send_group_help = send_command_help