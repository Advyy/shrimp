import discord
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name="server")
    async def _server(self, ctx):
        pass
        

    @_server.error
    async def server_error(self, ctx, error):
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Message advy LOL he broke something")

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Server(client))