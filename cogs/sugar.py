import discord

from discord import app_commands
from datetime import datetime
from discord.ext import commands
from utils.utils import get_sugar
from asyncio import sleep

class Sugar(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="sugar")
    async def _sugar(self, interaction: discord.Interaction): 
        sugar = get_sugar()

        embed = discord.Embed(title="", color=discord.Colour.purple())
        embed.set_author(name="Advy's Blood Sugar because why not LMFAO")
        embed.add_field(name="Number:", value=sugar["value"])
        embed.add_field(name="Trend:", value=sugar["trend"])
        embed.timestamp = datetime.now()

        await interaction.response.send_message(embed=embed)

    @_sugar.error
    async def sugar_error(self, interaction: discord.Interaction, error):
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Tell advy he broke something :D")
        await interaction.response.send_message(embed=embed)



async def setup(client): 
    await client.add_cog(Sugar(client))