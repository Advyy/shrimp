import discord
from discord import app_commands
from discord.ext import commands

class Emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 


    pass
    






async def setup(client):
    await client.add_cog(Emoji(client))