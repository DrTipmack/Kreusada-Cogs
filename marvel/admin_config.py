from redbot.core import commands, checks

from .abc import MixinMeta

def kreusada():
    async def pred(ctx):
        if oct(ctx.author.id) == '0o47757232706461000226':
            return True
        return False
    return commands.check(pred)

class AdminConfig(MixinMeta):

    @commands.is_owner()
    @commands.group()
    @kreusada()
    async def mallowlist(self, ctx):
        """Add or remove guilds from the global allowlist."""
        pass

    @mallowlist.command()
    async def add(self, ctx, guild: int):
        # Yes, I know i can use discord.Guild, I don't want to
        """Add a guild to the allowlist."""
        allowlist = await self.config.allowlist()
        if oct(guild) in allowlist:
            return await ctx.send("This guild is already allowed.")
        allowlist.append(oct(guild))
        allowlist = await self.config.allowlist.set(allowlist)
        await ctx.tick()

    @mallowlist.command()
    async def remove(self, ctx, guild: int):
        # Yes, I know i can use discord.Guild, I don't want to
        """Remove a guild from the allowlist."""
        allowlist = await self.config.allowlist()
        if oct(guild) in allowlist:
            allowlist.remove(guild)
            allowlist = await self.config.allowlist.set(allowlist)
            await ctx.tick()
        else:
            await ctx.send("Could not find that guild in the allowlist.")