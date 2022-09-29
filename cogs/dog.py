import discord
import requests
import math

from discord import app_commands
from discord.ext import commands

class Dog(commands.Cog): 
    def __init__(self, client): 
        self.client = client

    @app_commands.command(name="cat", description="Sends a Cat 😉")
    async def _dog(self, interaction: discord.Interaction): 
        reponse = requests.get("https://dog.ceo/api/breeds/image/random")
        json1 = reponse.json()

        if json1["status"] == "success": 
            print(json1)
            image = json1["message"]
            image1 = image
            print(image)
            embed = discord.Embed(title='cat', color=0xe67e22)
            embed.set_image(url=image)

            await interaction.response.send_message(embed=embed)
            
    @_dog.error
    async def dog_error(self, interaction: discord.Interaction, error): 
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Tell advy he broke something :D")
        await interaction.response.send_message(embed=embed)

async def setup(client): 
    await client.add_cog(Dog(client))
    print("dog is loaded")