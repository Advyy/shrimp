import discord

from discord import app_commands
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client


        @app_commands.command(name="server")
        async def _server(self, interaction: discord.Interaction):
            bots = []
            for member in interaction.guild.members: 
                if member.bot == True: 
                    bots.append(member.id)
            embed = discord.Embed(title=f"{interaction.guild.name} Stats", description="")
            embed.add_field(name="Server Owner", value=f"{interaction.guild.owner}")
            embed.add_field(name="Channels", value=f"Total Channels: {len(interaction.guild.channels)}\nText Channels: {len(interaction.guild.text_channels)}\nVoice Channels {len(interaction.guild.voice_channels)}")
            embed.add_field(name="Roles", value=f"{' '.join(role.mention for role in interaction.guild.roles)}")
            embed.add_field(name="Members", value=f"{interaction.guild.member_count}\n Bots: {len(bots)} ") # it wouldn't let me do an inline for loop again 
        # so I just did it above instead of figuring out why because I cba 


    @_server.error
    async def server_error(self, ctx, error):
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Message advy LOL he broke something")
        await ctx.send(embed=embed)

        

    @_server.error
    async def server_error(self, ctx, error):
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Message advy LOL he broke something")

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Server(client))