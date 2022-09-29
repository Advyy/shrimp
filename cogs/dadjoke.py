import discord
import requests
import math

from discord import app_commands
from discord.ext import commands

class dadjoke(commands.Cog): 
    def __init__(self, client): 
        self.client = client

    @app_commands.command(name="dadjoke", description="Sends an awful dad joke")
    async def _dadjoke(self, interaction: discord.Interaction): 
        headers = {'Accept': 'application/json'}

        response = requests.get("https://icanhazdadjoke.com/", headers=headers)
        json = response.json()
        
        embed = discord.Embed(title=f'{json["joke"]}', color=0xe67e22)
        await interaction.response.send_message(embed=embed)
    
    @_dadjoke.error
    async def dad_joke_error(self, interaction: discord.Interaction, error): 
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Tell advy he broke something :D")
        await interaction.response.send_message(embed=embed)

# https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&part=statistics&id=UCYd_GdgAae7qqUErgAcp5gw&key=AIzaSyBP2GHEFZMyUxWqdVyaRsutWidbnfOp1zQ


async def setup(client): 
    await client.add_cog(dadjoke(client))
    print("dadjoke is loaded")