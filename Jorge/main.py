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
        if emoji == '7️⃣':
            role = discord.utils.get(guild.roles, name="Rocket League")  
      
        await member.add_roles(role)
        role = discord.utils.get(guild.roles, name="Gamer")
        await member.add_roles(role)


@bot.command(pass_context=True)
async def roles(ctx):

    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣']

    embed = discord.Embed(
        title="Escolhe aqui as tuas roles (Não cliques no nome)",
        description='''1- Minecraft
        2- League of Lasagna
        3- Fortnite
        4- Genshin Impact
        5- Valorant
        6- Yu-Gi-Oh
        7- Rocket League
        ''',
        url = 'https://www.youtube.com/watch?v=Yt6PPkTDsWg',
        color = 16677215
    )
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