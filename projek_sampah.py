#projek py

import discord
from discord.ext import commands
import os , random
from sampah import sampah_organik, sampah_anorganik

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"bot sudah login dengan nama {bot.user}")

@bot.command()
async def organik(ctx):
    await ctx.send("salah satu sampah organik adalah:")
    await ctx.send(sampah_organik())

@bot.command()
async def anorganik(ctx):
    await ctx.send("salah satu sampah anorganik adalah:")
    await ctx.send(sampah_anorganik())

bot.run(muehehe)

#sampah py

import random

def sampah_organik():
    nama_sampah = ["daun" , "sayur busuk" ,
                   "buah busuk" , "nasi basi" ,
                   "bangkai" , "kotoran hewan" ,
                   "ranting pohon" , "limbah ternak" ,
                   "tulang" , "kulit buah" , "cangkang telur" , 
                   "ampas kopi" , "ampas teh"]
    
    return random.choice(nama_sampah)


def sampah_anorganik():
    nama_sampah = ["botol plastik" , "karet" , "bungkus plastik" ,
                   "kresek" , "kotak" , "kardus" , " kertas" ,
                   "baterai" , "besi" , "kaleng" , "sampah dvd" , 
                   "gelas kaca"]
    
    return random.choice(nama_sampah)

