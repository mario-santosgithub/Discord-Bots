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

@bot.event
async def on_ready():
    change_status.start()
    print('Logged in as {0.user}'.format(bot))


@bot.command(pass_context=True)
async def hello(ctx):
    print("here")
    await ctx.channel.send("Hello :D")


@bot.command(pass_context=True)
async def ai(ctx, *message):
    author = ctx.message.author.id
    

    message = ' '.join(message)

    bot_response = "```python{}```".format(chatgpt_response(prompt=message))
    
    finalMsg = discord.Embed(
        title="Input: {}".format(message),
        description= bot_response,
        url = 'https://www.youtube.com/watch?v=Yt6PPkTDsWg',
        color = 16677215
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


@bot.event
async def on_raw_reaction_add(payload):
    msgId = 983667995203239947

    if msgId == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name

        if emoji == '0️⃣':
            role = discord.utils.get(guild.roles, name="IPS")

        if emoji == '0️⃣0️⃣':
            role = discord.utils.get(guild.roles, name="IST")

        if emoji == '0️⃣1️⃣':
            role = discord.utils.get(guild.roles, name="Minecraft")

        if emoji == '0️⃣2️⃣':
            role = discord.utils.get(guild.roles, name="LOL")

        if emoji == '0️⃣3️⃣':
            role = discord.utils.get(guild.roles, name="Fortnite")

        if emoji == '0️⃣4️⃣':
            role = discord.utils.get(guild.roles, name="Genshin Impact")

        if emoji == '0️⃣5️⃣':
            role = discord.utils.get(guild.roles, name="Valorant")

        if emoji == '0️⃣6️⃣':
            role = discord.utils.get(guild.roles, name="Yu-gi-oh")  
            
        if emoji == '0️⃣7️⃣':
            role = discord.utils.get(guild.roles, name="Rocket League")  
            
        if emoji == '0️⃣8️⃣':
            role = discord.utils.get(guild.roles, name="")  
            
        if emoji == '0️⃣9️⃣':
            role = discord.utils.get(guild.roles, name="")  
            
        if emoji == '1️⃣0️⃣':
            role = discord.utils.get(guild.roles, name="")  
      
        await member.add_roles(role)
        role = discord.utils.get(guild.roles, name="Gamer")
        await member.add_roles(role)


@bot.command(pass_context=True)
async def roles(ctx):

    emojis = ['0️⃣1️⃣', '0️⃣2️⃣', '0️⃣3️⃣', '0️⃣4️⃣', '0️⃣5️⃣', '0️⃣6️⃣', '0️⃣7️⃣']

    embed = discord.Embed(
        title="Escolhe aqui as tuas roles de jogos (Não cliques no nome, pois vais adorar)",
        description='''
        01- Minecraft
        02- League of Lasagna
        03- Valorant
        04- Fortnite
        06- Rocket League
        07- Yu-Gi-Oh
        08- Hearthstone
        09- Need for Speed
        10- FIFA
        11- Genshin Impact
        12- Mosnter Hunter
        13- Albion
        14- New World
        15- Lost Ark
        16- World of Warcraft
        ''',
        url = 'https://www.youtube.com/watch?v=Yt6PPkTDsWg',
        color = 16677215
    )# M4-people  M8+/-people
    msg = await ctx.channel.send(embed=embed)

    for i in range(len(emojis)):
        await msg.add_reaction(emojis[i])


@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status)))

keep_alive()
bot.run(TOKEN)