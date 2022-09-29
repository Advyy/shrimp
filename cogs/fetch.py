import discord
from discord.ext import commands

class Fetch(commands.Cog): 
    def __init__(self, client): 
        self.client = client

    @commands.command(name="fetch")
    @commands.is_owner()
    async def _fetch(self, ctx, user: discord.User): 
        formatt = "%B %d %Y %I:%M:%S %p"
        created = user.created_at.strftime(formatt)

        embed = discord.Embed(title=f"", color=discord.Colour.purple())
        embed.set_author(name=f"Fetched info for {user.name} ({user.id})", icon_url=f'{user.avatar_url}')
        embed.add_field(name="Name", value=f'{user.name}')
        embed.add_field(name="Discriminator", value=f'#{user.discriminator}', inline=False)
        embed.add_field(name="Account created on", value=f'{created}', inline=False)
        
        if user.bot is True: 
            embed.add_field(name="Is Bot", value="Yes")
            
        await ctx.send(embed=embed)

async def setup(client): 
    await client.add_cog(Fetch(client))