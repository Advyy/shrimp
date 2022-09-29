import discord
import requests
import math

from discord.utils import get
from discord.ext import commands

class Insult(commands.Cog): 
    def __init__(self, client): 
        self.client = client
    
    @commands.command(name="insult")
    async def _insult(self, ctx, user: discord.Member=None): 
        
        ad = self.client.get_user(311301728580665354)

        if user is None: 
            reponse = requests.get(f"https://insult.mattbas.org/api/insult.json?who={ctx.author.name}")
            json = reponse.json()
            print(json) 
            embed = discord.Embed(title=json["insult"], color=discord.Colour.purple())
            await ctx.send(embed=embed)
        else: 
            if user.id is ad.id:
                await ctx.send("That user can not be insulted")
            elif user.id is self.client.user.id: 
                await ctx.send("You can't insult me LOL")
            else:
                reponse = requests.get(f"https://insult.mattbas.org/api/insult.json?who={user.name}")
                json = reponse.json()
                print(json)  
                embed = discord.Embed(title=json["insult"], color=discord.Colour.purple())
                await ctx.send(embed=embed)

    @_insult.error
    async def insult_error(self, ctx, error): 
        if isinstance(error, commands.CommandOnCooldown): 
            await ctx.send(f"You can do this command again in {math.floor(error.retry_after)}s", delete_after=5)


async def setup(client): 
    await client.add_cog(Insult(client))
    print("insult is loaded")