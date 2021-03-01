from redbot.core import commands, Config

from .abc import MixinMeta

class Pred(MixinMeta):
    pass

    def limit_guilds():
        async def pred(ctx):
            allowed = await self.config.allowlist()
            g = ctx.guild.id
            if oct(g) not in allowed:
                return False
            return True
        return commands.check(pred)
