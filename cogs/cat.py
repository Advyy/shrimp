import discord 
import requests
import math
from discord.ext import commands


class Cat(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.command(name="dog")
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def _cat(self, ctx):
        headers = { 
            'x-api-key': '6d6c2593-01b2-45af-a500-05350059fbf8'
        }

        reponse = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
        json = reponse.json()

        print(json)

        for i in json: 
            url = i['url']

        embed = discord.Embed(title='dog', color=0xe67e22)
        embed.set_image(url=url)

        await ctx.send(embed=embed)
            
    @_cat.error
    async def cat_error(self, interaction: discord.Interaction, error): 
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Tell advy he broke something :D")
        await interaction.channel.send(embed=embed)


async def setup(client): 
    await client.add_cog(Cat(client))