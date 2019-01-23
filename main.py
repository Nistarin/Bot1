from discord.ext import commands
import asyncio

prefix = '!'

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print('Time Machine is ready!')


@client.command(pass_context=True)
async def start(ctx):
    await client.say(" Time Machine: Active! @here")
    await asyncio.sleep(5)
    await client.say(" Time Machine: Running low on gas @here")
    await asyncio.sleep(5)
    await client.say(" Time Machine: Deactivate @here")


client.run('NTM3NDg0ODcxMjUwMDgzODQw.DyoO5g.am-NvQVAe31YWzOcDR2vbIJaHM8')