import discord
from discord.ext import commands

class Help(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.command(name="help", usage=";help")
    async def _help(self, ctx): 

        embed = discord.Embed(title="", color=discord.Colour.purple())
        embed.set_author(name=f"Command List ({len(self.client.commands)})")

        for command in self.client.commands: 
            embed.add_field(name=command.name, value=f"**Usage**: `{command.usage}`\n**Description**: `{command.description}`", inline=False)
            # print(f"{command.name} ({command.description})")
        await ctx.send(embed=embed)
        
async def setup(client): 
    await client.add_cog(Help(client))