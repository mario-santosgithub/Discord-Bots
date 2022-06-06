import discord
import asyncio
import requests
from discord import Member
from discord.utils import get
from discord.ext import commands, tasks
from random import choice
import youtube_dl
from keep_alive import keep_alive
from config import *


bot = commands.Bot(command_prefix=PREFIX, description="O Jorge")

status = [status1, status2, status3]

@bot.event
async def on_ready():
    change_status.start()
    print('Logged in as {0.user}'.format(bot))


@bot.event
async def on_raw_reaction_add(payload):
    msgId = 979739479835299900

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

        if emoji == '4️⃣':
            role = discord.utils.get(guild.roles, name="Genshin Impact")

        if emoji == '5️⃣':
            role = discord.utils.get(guild.roles, name="Valorant")

        if emoji == '6️⃣':
            role = discord.utils.get(guild.roles, name="Yu-gi-oh")
        
        await member.add_roles(role)
        role = discord.utils.get(guild.roles, name="Gamer")
        await member.add_roles(role)


@bot.command(pass_context=True)
async def roles(ctx):

    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']

    embed = discord.Embed(
        title="Escolhe aqui as tuas roles (Não cliques no nome)",
        description='''1- Minecraft
        2- League of Lasagna
        3- Fortnite
        4- Genshin Impact
        5- Valorant
        6- Yu-Gi-Oh
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

keep_alive()
bot.run(TOKEN)
