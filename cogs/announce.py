import discord

from discord import app_commands
from discord.utils import get
from discord.ext import commands

class Announce(commands.Cog): 
    def __init__(self, client): 
        self.client = client

    @app_commands.command(name="announce", description="Announce an embed to a channel")
    @app_commands.describe(channel="What channel would you like to announce to?", title="What do you want the title of the announcement to be?", desc="What do you want the description of the announcement to be?")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def _announce(self, interaction: discord.Interaction, channel: discord.TextChannel, title: str, desc: str): 
        
        # ann = get(interaction.guild.channels, id=799471370677387264)

        if channel: 
            embed = discord.Embed(title=f"{title}", description=f"{desc}", color=discord.Colour.purple())
            embed.set_thumbnail(url=f"{self.client.user.avatar.url}")
            embed.set_footer(text=f"Announced by: {interaction.user.name} ({interaction.user.id})", icon_url=f'{interaction.user.avatar.url}')
            await channel.send(embed=embed)
            await interaction.response.send_message(embed=embed)
            return

        embed = discord.Embed(title=f"{title}", description=f"{desc}", color=discord.Colour.purple())
        embed.set_thumbnail(url=f"{self.client.user.avatar.url}")
        embed.set_footer(text=f"Announced by: {interaction.user.name} ({interaction.user.id})", icon_url=f'{interaction.user.avatar.url}')

        await interaction.response.send_message(embed=embed)

    @_announce.error
    async def announce_error(self, interaction: discord.Interaction, error): 
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Tell advy he broke something :D")
        await interaction.channel.send(embed=embed)
        
    
    


async def setup(client): 
    await client.add_cog(Announce(client))
    print("announce is loaded")