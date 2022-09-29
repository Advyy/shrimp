import discord
import datetime as datetime
import time

from discord.ext import commands

class Uptime(commands.Cog): 
    def __init__(self, client): 
        self.client = client
        self.start_time = datetime.datetime.utcnow()
    
    @commands.command(name="uptime", aliases=["up"], usage=';uptime', description="Show's how long the bot has been online")
    async def _uptime(self, ctx):
        
        uptime = datetime.datetime.utcnow() - self.start_time

        day = uptime.days
        day = str(day)

        uptime = str(uptime)
        uptime = uptime.split(":")

        hours = uptime[0]

        minutes = uptime[1]

        seconds = uptime[2]
        seconds = seconds.split(".")
        seconds = seconds[0]
        
        embed = discord.Embed(color=discord.Color.purple())
        embed.add_field(name="Uptime", value=f'I have been on for `{hours}h:{minutes}m:{seconds}s`')
        embed.set_footer(text=f"Requested by: {ctx.author.name}({ctx.author.id})", icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
        
    @_uptime.error
    async def uptime_error(self, interaction: discord.Interaction, error): 
        embed = discord.Embed(title="Error", description=error, color=discord.Colour.red())
        embed.set_footer(text="Tell advy he broke something :D")
        await interaction.response.send_message(embed=embed)


async def setup(client): 
    await client.add_cog(Uptime(client))