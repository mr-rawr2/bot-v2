import discord
from discord.ext import commands
import random, os, requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def checkAI(ctx):
    if ctx.mesagge.attachment:
        for file in ctx.mesagge.attachment:
            namafile = file.filename
            urlfile = file.url
            await file.save(f'./{namafile}')
            await ctx.send(f'gambar udah di simpan dengan nama {namafile}')

            kelas, skor = get_class('keras_model.h5', 'labels.txt', namafile)

            if kelas == 'Merpati\n' and skor >= 0.75:
                await ctx.send('ini adalah burung merpati')
                await ctx.send('makanan burung merpati adalah gabah beras')

            elif kelas == 'Pipit\n' and skor >= 0.75:
                await ctx.send('ini adalah burung pipit')
                await ctx.send('makanan burung pipit adalah kacang-kacangan')
            
            elif kelas == 'Perkutuk\n' and skor >= 0.75:
                await ctx.send('ini adalah burung perkutuk')
                await ctx.send('makanan burung perkutuk adalah buah')

            else:
                await ctx.send('KAYAKNYA BUKAN BURUNG DEH')

    else:
        await ctx.send('gambarnya di mana?')

bot.run("token lu")
