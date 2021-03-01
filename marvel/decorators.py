from redbot.core import commands

from .abc import MixinMeta

class Decorators(MixinMeta):
    
    def __init__(self, bot):
        self.bot = bot
        
    def kreusada():
        async def pred(ctx):
            if oct(ctx.author.id) == '0o47757232706461000226':
                return True
            return False
        return commands.check(pred)

    def limit_guilds():
        async def pred(ctx):
            allowed = await self.config.allowlist()
            g = ctx.guild.id
            if oct(g) not in allowed:
                return False
            return True
        return commands.check(pred)