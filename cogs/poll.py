import discord
import re

from collections import OrderedDict
from datetime import datetime
from utils.utils import str_to_hex, merge, prepend
from discord import app_commands
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="poll", description="make a poll")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.describe(title="Poll Title", questions="The questions want in the poll seperated by a |", emojis="Emojis you want used in the poll seperated by spaces", color="The color of the embed (if not inputed it will default to no color). Use a hex value to select the color ex. #f15a22", channel="The channel you want to send the poll in", notes="Notes you want at the end of the questions", content="Content you want outside the embed, maybe a mention")
    async def _poll(self, interaction: discord.Interaction, title: str, questions: str, emojis: str, channel: discord.TextChannel, color: str=None, notes: str=None, content: str=None):

        questionsList = questions.split("|")
        emojisList = emojis.split(" ")

        new = "\n"

        if len(questionsList) > len(emojisList) or len(emojisList) > len(questionsList):
            await interaction.response.send_message(embed=discord.Embed(title="Please make sure the amount of questions and the amount of emojis you input are the same", description=f"Current Count: \nQuestion: {len(questionsList)}\nEmojis: {len(emojisList)}"))
            return

        # this took way too fucking long to figure out bro, but merges emojis and questions into a list of tuples
        merged = merge(emojisList, questionsList)
        print(merged)

        # # sorts through tuples
        eAndQ = list(" ".join(tups) for tups in merged)

        if color is None:
            # and this fucker joins the list of sorted tuples 😀🔫
            if notes is not None: 
                embed = discord.Embed(title=f"{title}", description=f"{new.join(prepend(eAndQ, new))}\n\n{notes}", color=discord.Colour.dark_theme())
            else:
                embed = discord.Embed(title=f"{title}", description=f"{new.join(prepend(eAndQ, new))}", color=discord.Colour.dark_theme())
        else: 
            hex = str_to_hex(color)
            if notes is not None: 
                embed = discord.Embed(title=f"{title}", description=f"{new.join(prepend(eAndQ, new))}\n\n{notes}", color=hex)
            else:
                embed = discord.Embed(title=f"{title}", description=f"{new.join(prepend(eAndQ, new))}", color=hex)
        embed.timestamp = datetime.now()
        embed.set_footer(text=f"Poll hosted by: {interaction.user.name} ({interaction.user.id})", icon_url=interaction.user.avatar.url)

        if content is None:
            chanMsg = await channel.send(content=content, embed=embed)
        else: 
            chanMsg = await channel.send(embed=embed)
        
        # loop through messgages in channel to find the embed
        # loop through the emoji list and add reactions to the message
        for i in emojisList: 
            try:
                await chanMsg.add_reaction(f"{i}")
            # if emoji is a custom emoji, grab the ID from it and fetch it from the guild
            except discord.errors.HTTPException:
                emojiID = int(re.search(r'\d+', i))
                nEmoji = await interaction.channel.guild.fetch_emoji(emojiID)
                await chanMsg.add_reaction(f"{nEmoji}")
        
        if channel is not None: 
            await interaction.response.send_message(f"Poll sent to {channel.mention}")
    
    @_poll.error
    async def poll_error(self, interaction: discord.Interaction, error): 
        await interaction.user.send(embed=discord.Embed(title="Poll Error", description=f"{error}", color=discord.Colour.red()).set_footer(text="Tell advy he broke something"))

async def setup(client):
    await client.add_cog(Poll(client))