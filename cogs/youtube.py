import discord
import requests
from discord.ext import commands

class Youtube(commands.Cog): 
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="youtube")
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def _youtube(self, ctx, userID): 

        response = requests.get(f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&part=statistics&part=snippet&id={userID}&key=AIzaSyBP2GHEFZMyUxWqdVyaRsutWidbnfOp1zQ")
        json = response.json()
        for item in json["items"]: 
            viewerss = int(item["statistics"]["viewCount"])
            subss = int(item["statistics"]["subscriberCount"])
            videoss = int(item["statistics"]["videoCount"])
            embed = discord.Embed(
                title=f'{item["snippet"]["title"]} Youtube', 
                description=f'Subs: {subss:,}\n Views: {viewerss:,}\n Videos: {videoss:,}',
                color=discord.Colour.blue(), 
                url=f'https://www.youtube.com/channel/{item["id"]}'
            )
            embed.set_thumbnail(url=item["snippet"]["thumbnails"]["high"]["url"])
            await ctx.send(embed=embed)
            print(json)

async def setup(client): 
    await client.add_cog(Youtube(client))