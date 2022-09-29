from discord_webhook import DiscordWebhook
from discord.ext import commands
from utils.utils import spoiler

class Spoil(commands.Cog): 
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="spoil", aliases=["spoiler", "sp", "spoiled"])
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def _spoil(self, ctx, *, message):
        await ctx.message.delete()
        
        spoiled = spoiler(message) 
        createhook = await ctx.channel.create_webhook(name='spoil')
        webhook = DiscordWebhook(url=f'{createhook.url}', content=spoiled, username=f'{ctx.author.display_name}', avatar_url=f'{ctx.author.avatar.url}')
        response = webhook.execute()

        if response.status_code == 400: 
            await ctx.send("Message must be 2000 characters or fewer", delete_after=10)
        await createhook.delete()
        
        





async def setup(client): 
    await client.add_cog(Spoil(client))
