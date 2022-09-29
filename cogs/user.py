import discord
import time


from discord import app_commands
from datetime import datetime
from discord.ext import commands

class User(commands.Cog): 
    def __init__(self, client): 
        self.client = client
        self.formatt = "%B %d %Y %I:%M:%S %p"
    
    @app_commands.command(name="user", description="Get user information")
    @app_commands.describe(member="Specify a member to get information about")
    async def _user(self, interaction: discord.Interaction, member: discord.Member):

        # joinedd = member.joined_at
        # jyear = joinedd.year
        # jmonth = joinedd.month
        # jday = joinedd.day
        # now = datetime.datetime.now()
        # nyear = now.year
        # nmonth = now.month
        # nday = now.day

        # resulty = nyear - jyear
        # resultm = jmonth - nmonth
        # resultd = jday - nday

        # createdd = member.created_at
        # cyear = createdd.year
        # cmonth = createdd.month
        # cday = createdd.day

        # resultyy = nyear - cyear
        # resultmm = cmonth - nmonth
        # resultdd = cday - nday




        formatt = "%B %d %Y %I:%M:%S %p"
        joined = member.joined_at.strftime(formatt)
        created = member.created_at.strftime(formatt)

        # created = member.created_at.strftime(self.formatt)
        # dayss = datetime.now() - member.created_at
        # days =  member.created_at.strftime(self.formatt)
        # daysn = dayss.days
        # years = daysn / 365

        embed = discord.Embed(title="", color=discord.Colour.purple())
        embed.set_author(name=f"{member.name} ({member.id})", icon_url=f'{member.avatar.url}')
        embed.add_field(name="Name", value=f'{member}')
        embed.add_field(name="Status", value=f'{member.desktop_status}')
        embed.add_field(name="Account created", value=f'{created}\n', inline=False)
        embed.add_field(name="Joined Server", value=f'{joined}\n', inline=False)
        embed.add_field(name="Is on Mobile", value=f'{member.is_on_mobile()}')
        embed.add_field(name=f"Roles", value=f'{", ".join(str(role) for role in reversed(member.roles))}')

        await interaction.response.send_message(embed=embed)
        await interaction.message.delete(delay=5)

    @_user.error
    async def user_error(self, interaction: discord.Interaction, error): 
        await interaction.channel.send(error)


async def setup(client): 
    await client.add_cog(User(client))