from discord.ext import commands
import asyncio

prefix = '!'

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print('Time Machine is ready!')


@client.command(pass_context=True)
async def teste(ctx)
    await client.say("```++ Time Machine: Active! ++```")
    await asyncio.sleep(60*60*7.5)
    await client.say("```++ Time Machine: Running low on gas ++```")
    await asyncio.sleep(60*60*8)
    await client.say("```++ Time Machine: Deactivate ++```")


client.run(NTM3NDg0ODcxMjUwMDgzODQw.DyoO5g.am-NvQVAe31YWzOcDR2vbIJaHM8)