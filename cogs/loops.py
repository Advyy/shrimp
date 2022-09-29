import discord

from discord.ext import commands, tasks

class Loops(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.status_change.start()

    @tasks.loop(seconds=1)
    async def status_change(self):
        print("asd")


async def setup(client):
    await client.add_cog(Loops(client))
    print("loaded loops")