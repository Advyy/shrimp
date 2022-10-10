import discord
import re

from collections import OrderedDict
from datetime import datetime
from utils.utils import str_to_hex, merge
from discord import app_commands
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="poll", description="make a poll")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.describe(title="Poll Title", questions="The questions want in the poll seperated by a |", emojis="Emojis you want used in the poll seperated by spaces", color="The color of the embed (if not inputed it will default to no color). Use a hex value to select the color ex. #f15a22")
    async def _poll(self, interaction: discord.Interaction, title: str, questions: str, emojis: str, color: str=None):

        questionsList = questions.split("|")
        emojisList = emojis.split(" ")

        new = "\n"

        if len(questionsList) > len(emojisList) or len(emojisList) > len(questionsList):
            await interaction.response.send_message(embed=discord.Embed(title="Please make sure the amount of questions and the amount of emojis you input are the same", description=f"Current Count: \nQuestion: {len(questionsList)}\nEmojis: {len(emojisList)}"))
            return

        # this took way too fucking long to figure out bro, but merges emojis and questions into a list of tuples
        merged = merge(emojisList, questionsList)

        # sorts through tuples
        eAndQ = list(" ".join(tups) for tups in merged)

        # eAndQ for i in zip(emojisList, questionsList) for eAndQ in i
        if color is None:
            # and this fucker joins the list of sorted tuples 😀🔫
            embed = discord.Embed(title=f"{title}", description=f"{new.join(eAndQ)}")
            embed.add_field(name="Emojis", value=f"{new.join(emojisList)}")
        else: 
            hex = str_to_hex(color)
            embed = discord.Embed(title=f"{title}", description=f"{new.join(questionsList)}", color=hex)
        embed.timestamp = datetime.now()
        embed.set_footer(text=f"Poll hosted by: {interaction.user.name} ({interaction.user.id})", icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)


        # loop through messgages in channel to find the embed
        async for message in interaction.channel.history():
            if not message.embeds:
                continue
            if message.embeds[0].title == embed.title and message.embeds[0].description == embed.description:
                # assign a variable to the message so we can use the message
                msg = message
                break

        # loop through the emoji list and add reactions to the message
        for i in emojisList: 
            try:
                await msg.add_reaction(f"{i}")
            # if emoji is a custom emoji, grab the ID from it and fetch it from the guild
            except discord.errors.HTTPException:
                emojiID = int(re.search(r'\d+', i))
                nEmoji = await interaction.channel.guild.fetch_emoji(emojiID)
                await msg.add_reaction(f"{nEmoji}")
    
    @_poll.error
    async def poll_error(self, interaction: discord.Interaction, error): 
        await interaction.user.send(embed=discord.Embed(title="Poll Error", description=f"{error}", color=discord.Colour.red()).set_footer(text="Tell advy he broke something"))

async def setup(client):
    await client.add_cog(Poll(client))