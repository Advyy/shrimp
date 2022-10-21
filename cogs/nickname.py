import discord

from asyncio import sleep
from discord.ext import commands

class Nickname(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # pass
        print(before.nick) # executes
        print(after.nick) # executes

        if after.nick or before.nick is not before.name:
            print(f"this executes {before.id}") # executes
            print(f"this executes {after.id}") # executes
            mId = self.client.get_member(after.id) # dies, with and without
            await mId.edit(nick=None) # dies with "before.edit() too"

async def setup(client):
    await client.add_cog(Nickname(client))