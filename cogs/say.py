import discord

from discord_webhook import DiscordWebhook
from discord.ext import commands

class Say(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.command(name="say")
    async def _say(self, ctx, user: discord.User=None, *, message: str):

        await ctx.message.delete()

        if user.id == 311301728580665354: 
            await ctx.send("You cannot talk as this user", delete_after=15)
            return
        
        createhook = await ctx.channel.create_webhook(name='talk')
        webhook = DiscordWebhook(url=f'{createhook.url}', content=f'{message}', username=f'{user.display_name}', avatar_url=f'{user.avatar.url}')
        response = webhook.execute()
        await createhook.delete()
    
    @_say.error
    async def say_error(self, ctx, error):
        print(error)

        
async def setup(client): 
    await client.add_cog(Say(client))