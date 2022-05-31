import discord
import asyncio
import requests
from discord import Member
from discord.utils import get
from discord.ext import commands, tasks
from random import choice
import youtube_dl

import music

cogs = [music]




PREFIX = '!'


bot = commands.Bot(command_prefix=PREFIX, description="O Jorge")

status = ['Status1', 'Status2', 'Status3']

for i in range(len(cogs)):
    cogs[i].setup(bot)

#remove the default help command so that we can write out own
bot.remove_command('help')

@bot.event
async def on_ready():
    change_status.start()
    print('Logged in as {0.user}'.format(bot))


@bot.event
async def on_raw_reaction_add(payload):
    msgId = 964321005055119380

    if msgId == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == '1️⃣':
            role = discord.utils.get(guild.roles, name="Minecraft")

        if emoji == '2️⃣':
            role = discord.utils.get(guild.roles, name="LOL")

        if emoji == '3️⃣':
            role = discord.utils.get(guild.roles, name="Fortnite")

        await member.add_roles(role)


@bot.command(pass_context=True)
async def roles(ctx):

    emojis = ['1️⃣', '2️⃣', '3️⃣']

    embed = discord.Embed(
        title="Escolhe aqui as tuas roles (Não cliques no nome)",
        description='''1- Minecraft
        2- League of Lasagna
        3- Fortnite
        ''',
        url = 'https://www.youtube.com/watch?v=Yt6PPkTDsWg',
        color = 16677215
    )
    msg = await ctx.channel.send(embed=embed)

    for i in range(len(emojis)):
        await msg.add_reaction(emojis[i])

@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status)))


bot.run(TOKEN)
