from redbot.core import commands

allowed = [
    '0o51252007112140000074',
    '0o21554327060500400026',
]

def limit_guilds():
    async def pred(ctx):
        g = ctx.guild.id
        if oct(g) not in allowed:
            return False
        return True
    return commands.check(pred)
