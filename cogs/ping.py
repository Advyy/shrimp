import discord
import time
from discord.ext import commands

class PingCommand(commands.Cog): 
    def __init__(self, client): 
        self.client = client

    @commands.command(name="ping", aliases=["latency", "lat"])
    async def _ping(self, ctx): 
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        lat= round((time_2-time_1)*1000)

        embed = discord.Embed(color=discord.Colour.purple())
        embed.set_author(name="Ping", icon_url=f'{self.client.user.avatar_url}')
        embed.add_field(name="Bot Ping", value=f'{lat}ms')
        embed.add_field(name="API Ping", value=f'{round(self.client.latency * 1000)}ms')
        embed.set_footer(text=f'Requested by: {ctx.author.name}({ctx.author.id})', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)


async def setup(client): 
    await client.add_cog(PingCommand(client))