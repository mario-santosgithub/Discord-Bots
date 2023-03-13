import discord
from discord import Member
from discord.utils import get
from discord.ext import commands, tasks
from random import choice
from keep_alive import keep_alive
from config import *
import os
import openai
import discord.ui
from discord.ui import View, Button, Select

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




@bot.command(pass_context=True)
async def roles(ctx):
    gameRoles = Button(label="Jogos", style=discord.ButtonStyle.green)
    gameRoles.callback = callbackGames

    uniRoles = Button(label="Universidade", style=discord.ButtonStyle.blurple)
    

    view = View(timeout=None)
    view.add_item(gameRoles)
    view.add_item(uniRoles)
    await ctx.send("Select Options", view=view)


async def callbackGames(interaction):
    
    select = Select(options=[
        discord.SelectOption(label="Minecraft", value="01", description="This will open"),
        discord.SelectOption(label="League of Lasagna", value="02", description="This will open2"),
        discord.SelectOption(label="Valorant", value="03", description="This will open2"),
        discord.SelectOption(label="Counter Strike", value="04", description="This will open2"),
        discord.SelectOption(label="Fortnite", value="05", description="This will open2"),
        discord.SelectOption(label="Rocket League", value="06", description="This will open2"),
        discord.SelectOption(label="Yu-Gi-Oh", value="07", description="This will open2"),
        discord.SelectOption(label="HearthStone", value="08", description="This will open2"),
        discord.SelectOption(label="Need For Speed", value="09", description="This will open2"),
        discord.SelectOption(label="FIFA", value="10", description="This will open2"),
        discord.SelectOption(label="Genshin Impact", value="11", description="This will open2"),
        discord.SelectOption(label="Monster Hunter", value="12", description="This will open2"),
        discord.SelectOption(label="Albion", value="13", description="This will open2"),
        discord.SelectOption(label="New World", value="14", description="This will open2"),
        discord.SelectOption(label="Lost Ark", value="15", description="This will open2"),
        discord.SelectOption(label="World Of Warcraft", value="16", description="This will open2"),
        discord.SelectOption(label="Stradew Valley", value="17", description="This will open2")
    ])  


    async def newCallbackGames(interaction):
        member = interaction.user    
        guild = member.guild

        newRole = rolesList.get(select.values[0])
        role = discord.utils.get(guild.roles, name=newRole)

        await member.add_roles(role)
        await interaction.response.send_message("Já está :D", ephemeral=True)

    
    select.callback = newCallbackGames
    view = View(timeout=None)
    view.add_item(select)
    await interaction.response.send_message("Escolhe uma opção", view=view, ephemeral=True)


    return

'''
Change the status 
'''
@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status)))

# Keep alive and run the bot
keep_alive()
bot.run(TOKEN)