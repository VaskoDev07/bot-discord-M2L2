import discord
import os
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi! I am a bot {bot.user}!")


@bot.command()
async def guess(ctx):
    await ctx.send("Guess a number 1 until 10")

@bot.command()
async def answer(ctx, n):
    if n == random.randint(1, 10):
        await ctx.send("Nice work!")
    else:
        await ctx.send("Try again...")

@bot.command()
async def mem(ctx):
    with open('images/meme1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def poll(ctx, agree):
    await ctx.send(f"Do you agree that waste can be recycled?")

    if agree == "ya" or agree == "Y":
        await ctx.send(f"You right!")
    else:
        await ctx.send(f"Well, there may be some that cannot be done, but generally trash can be turned into interesting creations.")

    await ctx.send(f'Next step type $jacob')

@bot.command()
async def start(ctx):
    await ctx.send(f"Type this command to activated me !")
    await ctx.send(f"$hello = say hello")
    await ctx.send(f"$guess = number guessing game")
    await ctx.send(f"$pool = Recycle question")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run('TOKEN')
