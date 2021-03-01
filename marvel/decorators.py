from redbot.core import  commands

def limit_guilds():
    async def pred(ctx):
        g = ctx.guild.id
        allowed = ['0o51252007112140000074']
        if oct(g) not in allowed:
            return False
        return True
    return commands.check(pred)