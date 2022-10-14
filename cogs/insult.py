import discord
import requests
import math

from discord import app_commands
from discord.utils import get
from discord.ext import commands

class Insult(commands.Cog): 
    def __init__(self, client): 
        self.client = client
    
    @app_commands.command(name="insult")
    @app_commands.describe(user="Who you want to insult")
    async def _insult(self, interaction: discord.Interaction, user: discord.Member=None): 
        
        ad = self.client.get_user(311301728580665354)

        if user is None: 
            reponse = requests.get(f"https://insult.mattbas.org/api/insult.json?who={ctx.author.name}")
            json = reponse.json()
            print(json) 
            embed = discord.Embed(title=json["insult"], color=discord.Colour.purple())
            await interaction.response.send_message(embed=embed)
        else: 
            if user.id is ad.id:
                await interaction.response.send_message("That user can not be insulted")
            elif user.id is self.client.user.id: 
                await interaction.response.send_message("You can't insult me LOL")
            else:
                reponse = requests.get(f"https://insult.mattbas.org/api/insult.json?who={user.name}")
                json = reponse.json()
                print(json)  
                embed = discord.Embed(title=json["insult"], color=discord.Colour.purple())
                await interaction.response.send_message(embed=embed)

    @_insult.error
    async def insult_error(self, interaction: discord.Interaction, error): 
        await interaction.response.send_message(embed=discord.Embed(title="Error", description=f"{error}", color=discord.Colour.red()))
        # if isinstance(error, commands.CommandOnCooldown): 
        #     await ctx.send(f"You can do this command again in {math.floor(error.retry_after)}s", delete_after=5)


async def setup(client): 
    await client.add_cog(Insult(client))
    print("insult is loaded")