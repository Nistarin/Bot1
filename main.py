from discord.ext import commands
import asyncio

prefix = '!'

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print('Time magic is fully charged!!')


@client.command(pass_context=True)
async def teste(ctx):
    await client.say("```++ Buffs are up! Time Magic ACTIVE!! ++```")
    await asyncio.sleep(5)
    await client.say("```++ Buffs are down! Recharging Time Magic!!")


client.run('NTM3NDg0ODcxMjUwMDgzODQw.Dyl7eg.pOivRyU7D5o5kbXiCc9vlJ-wR64')
