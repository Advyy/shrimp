from ctypes.wintypes import RGB
import discord
import colorname

from discord import app_commands
from discord.ext import commands

class Test(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="idk", description="Gets color codes of embeds in a selected channel")
    @app_commands.describe(channel="What channel would you like to retrieve color codes from?")
    async def _test(self, interaction: discord.Interaction, channel: discord.TextChannel):
        back = "\n"
        colorCodes = []

        async for message in channel.history(limit=100):
            for embed in message.embeds:
                hex = str(embed.color).lstrip('#')
                rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
                colorCodes.append(f"{str(embed.color)} ({colorname.get_color_name(rgb[0], rgb[1], rgb[2])})")
        
        await interaction.response.send_message(f'Colors for embeds in {channel.mention}\n\n{back.join(reversed(colorCodes))}')

    @_test.error
    async def test_error(self, interaction: discord.Interaction, error):
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Tell advy he broke something :D")
        await interaction.response.send_message(embed=embed)


async def setup(client): 
    await client.add_cog(Test(client))

