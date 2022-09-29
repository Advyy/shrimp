import discord

from discord import Embed
from discord.ext import commands

class Embed(commands.Cog): 
    def __init__(self, client): 
        self.client = client

    @commands.command(name="embed")
    @commands.has_permissions(administrator=True)
    async def _embed(self, ctx, color=None):

        color = color.replace("#", "")

        thing = f"0x{color}"

        int_thing = int(thing, 16)

        if color is None: 
            await ctx.send("Please give me a color for the embed `-embed fffff` ")
        else: 
            begin = await ctx.send("Please give me a title for the embed")
            titlem = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel.id == begin.channel.id)

            await ctx.send("Please give me a description for the embed (The actual text contents of the message itself)")
            descem = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel.id == begin.channel.id)

            embed = discord.Embed(title=f"{titlem.content}", description=f"{descem.content}", color=int_thing)
            await ctx.send(embed=embed)



"""
        titlem = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel.id == begin.channel.id, timeout=60)
        descem = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel.id == begin.channel.id, timeout=60)
"""

async def setup(client): 
    await client.add_cog(Embed(client))
    print("embed is loaded")