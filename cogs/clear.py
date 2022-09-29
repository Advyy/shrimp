import discord
from discord.ext import commands

class Clear(commands.Cog): 
    def __init__(self, client): 
        self.client = client

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, num:int, user:discord.Member=None): 
        await ctx.message.delete()

        if num and user == None:
            embed = discord.Embed(title="", color=discord.Colour.purple())
            embed.set_author(name=f"Cleared {num} messages", icon_url=f"{self.client.user.avatar_url}")
            embed.set_footer(text=f"Executed by: {ctx.author}")
            await ctx.channel.purge(limit=num + 1)
            await ctx.send(embed=embed, delete_after=10)
            
        if num and user is not None: 
            for msg in await ctx.channel.history(limit=num).flatten():
                if msg.author.id == user.id: 
                    await msg.delete()
            embed = discord.Embed(title="", color=discord.Colour.purple())
            embed.set_author(name=f"Cleared", icon_url=f"{self.client.user.avatar_url}")
            embed.add_field(name="Amount", value=f"{num}")
            embed.add_field(name="Users Messages Deleted", value=f"{user.mention}", inline=False)
            embed.set_footer(text=f"Executed by: {ctx.author}")
            await ctx.send(embed=embed)   
        

         
async def setup(client): 
    await client.add_cog(Clear(client))