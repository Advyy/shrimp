import discord
import random

from discord.ext import commands, tasks

class Loops(commands.Cog):
    def __init__(self, client):
        self.client = client
        # self.status_change.start()

    def cog_unload(self):
        self.status_change.cancel()
    
    
    @tasks.loop(minutes=5)
    async def status_change(self):
        statuses = ["bacon", "shrimp", "test"]
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=random.choice(statuses), type=discord.ActivityType.listening))
        
    
    @status_change.before_loop
    async def before_status_change(self):
        print('Waiting')
        await self.client.wait_until_ready()

async def setup(client):
    await client.add_cog(Loops(client))
    print("loaded loops")