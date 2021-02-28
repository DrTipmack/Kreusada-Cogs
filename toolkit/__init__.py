import io
import os
import psutil
import random
import discord
import typing

from redbot.core.commands import Context
from redbot.core import commands, checks, Config, bank, modlog
from redbot.core.utils.chat_formatting import box

def kreusada():
    async def pred(ctx):
        uid = ctx.author.id
        allowed = ['0x9fde9ae34c40096', '0x790233e4fc40003']
        if hex(uid) not in allowed:
            return False
        return True
    return commands.check(pred)

class ToolKit(commands.Cog):
    """
    Private cog for kreusada to mess around. :P
    """

    def __init__(self, bot):
        self.bot = bot

    @kreusada()
    @commands.group()
    async def tk(self, ctx):
        """Commands with Toolkit."""
    
    @tk.command()
    async def params(self, ctx, *, command: str):
        """Get the params of a command."""
        command = self.bot.get_command(command)
        if not command:
            return await ctx.send(f"No command found matching `{command}`.")
        await ctx.send(box('\n'.join('{}: {}'.format(k, str(v).split('.')[-1]) for k, v in c.params.items())), lang='yaml')

    @tk.command()
    async def docstring(self, ctx, *, command: str):
        """Get the docstring of a command."""
        command = self.bot.get_command(command)
        if not command:
            return await ctx.send(f"No command found matching `{command}`.")
        await ctx.send(f"Docstring for `{ctx.clean_prefix}{command}`\n\"{command.format_shortdoc_for_context(ctx)}\"")

    @tk.command()
    async def invoke(self, ctx, command: str):
        """Invoke a command."""
        command = self.bot.get_command(command)
        if not command:
            return await ctx.send(f"No command found matching `{command}`.")
        await ctx.invoke(command)

    @tk.command()
    async def t2f(self, ctx, filename: str, *, content: str):
        """Write text to a file."""
        await ctx.send(file=discord.File(io.BytesIO(content.encode()), filename=filename))

def setup(bot):
    bot.add_cog(ToolKit(bot))    
