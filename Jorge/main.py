import discord
from discord import Member
from discord.utils import get
from discord.ext import commands, tasks
from random import choice
from keep_alive import keep_alive
from config import *
import os
import openai

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

status = [status1, status2, status3]

bot = commands.Bot(command_prefix=PREFIX, description="O Jorge", intents=intents)


'''
Send a notification when the bot is ready
'''
@bot.event
async def on_ready():
    change_status.start()
    print('Logged in as {0.user}'.format(bot))


'''
Return a Hello messaga, it's mostly for debug
'''
@bot.command(pass_context=True)
async def hello(ctx):
    print("here")
    await ctx.channel.send("Hello :D")

'''
The AI function
'''
@bot.command(pass_context=True)
async def ai(ctx, *message):
    author = ctx.message.author.id

    message = ' '.join(message)

    bot_response = "```python{}```".format(chatgpt_response(prompt=message))

    finalMsg = discord.Embed(
        title="Input: {}".format(message),
        description=bot_response,
        url='https://www.youtube.com/watch?v=Yt6PPkTDsWg',
        color=16677215
    )
    await ctx.channel.send(ctx.message.author.mention)
    await ctx.channel.send(embed=finalMsg)


openai.api_key = CHATGPT_API_KEY


def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=2049
    )
    print(response)
    response_dic = response.get("choices")
    if response_dic and len(response_dic) > 0:
        prompt_response = response_dic[0]["text"]
    return prompt_response

'''
Function that adds the emojis to the Roles command
'''
@bot.event
async def on_raw_reaction_add(payload):
    msgId = 983667995203239947

    if msgId == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        def rolee(emojii):
            return {
                'a': 'Minecraft',
                'b': 'League of Lasagna',
                'c': 'Valorant',
                'd': 'Counter Strike',
                'e': 'Fortnite',
                'f': 'Rocket League',
                'g': 'Yu-Gi-Oh',
                'h': 'Hearthstone',
                'i': 'Need for Speed',
                'j': 'FIFA',
                'k': 'Genshin Impact',
                'l': 'Mosnter Hunter',
                'm': 'Albion',
                'n': 'New World',
                'o': 'Lost Ark',
                'p': 'World of Warcraft'
            }.get(emojii, '')

        role = discord.utils.get(guild.roles, name=rolee(emoji))
        await member.add_roles(role)
        role = discord.utils.get(guild.roles, name="Gamer")
        await member.add_roles(role)


@bot.command(pass_context=True)
async def roles(ctx):
    emojis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    embed = discord.Embed(
        title="Escolhe aqui as tuas roles de jogos (Não cliques no nome, pois vais adorar)",
        description='''
        a: Minecraft
        b: League of Lasagna
        c: Valorant
        d: Counter Strike
        e: Fortnite
        f: Rocket League
        g: Yu-Gi-Oh
        h: Hearthstone
        i: Need for Speed
        j: FIFA
        k: Genshin Impact
        l: Mosnter Hunter
        m: Albion
        n: New World
        o: Lost Ark
        p: World of Warcraft
        ''',
        url='https://www.youtube.com/watch?v=Yt6PPkTDsWg',
        color=16677215
    )  # M4-people  M8+/-people
    msg = await ctx.channel.send(embed=embed)

    for i in range(len(emojis)):
        await msg.add_reaction(emojis[i])

'''
Change the status 
'''
@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status)))

# Keep alive and run the bot
keep_alive()
bot.run(TOKEN)
