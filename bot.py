import discord
import os 
import asyncio

from discord.ext import commands
from utils.utils import read_json

settings = read_json("settings")

intents = discord.Intents.all()
cache_flags = discord.MemberCacheFlags.all()

client = commands.Bot(
    command_prefix="s;",
    intents=intents,
    member_cache_flags=cache_flags,
    help_command=None,
    owner_id=311301728580665354
    )

@client.event
async def on_ready(): 
    print(f"Logged on as: {client.user}")
    logs = client.get_channel(908277402994618418)
    new = "\n"
    
    try: 
        synced = await client.tree.sync()

        cmdNames = []

        for command in synced: 
            cmdNames.append(command.name)

        if len(synced) == 1:
            print(f"Synced {len(synced)} command ({','.join(cmdNames)})")
            embed = discord.Embed(title=f"Synced {len(synced)} command", description=f"{new.join(cmdNames)}")
            await logs.send(embed=embed)
            return

        print(f"Synced {len(synced)} commands ({', '.join(cmdNames)})")
        embedM = discord.Embed(title=f"Synced {len(synced)} commands", description=f"{new.join(cmdNames)}")
        await logs.send(embed=embedM)
    except Exception as e:
        print(f"Error syncing commands {e}")


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            await client.load_extension(f"cogs.{filename[:-3]}")
            
async def main(): 
    await load()
    await client.start(settings["token"])

asyncio.run(main())