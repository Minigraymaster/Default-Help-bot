import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

Bot = commands.Bot(command_prefix='!')

Bot.remove_command('help')

@Bot.event
async def on_ready():
    print("Bot is online")

@Bot.command(pass_context= True)

async def info():
    await Bot.say("Я БОТ И МОЯ ВЕРСИ Я V1")

@Bot.command(pass_context= True)

async def contacts():
    await Bot.say("e-mail:admin@skymine.kl.com.ua")

@Bot.command(pass_context= True)

async def help():
    await Bot.say("Префикс ты знаеш а вот команды неее смотри info  ето инва о боте,а contacts емеил разраба.ПОКА!")

@Bot.command(pass_context= True)
async def music(ctx):
    emb = discord.Embed(title= "В разработке...", color = 12390624)
    emb.add_field(name= "Mr.Hacker", value= "90990", inline= False)
    emb.set_author(name= "Музыка")
    emb.set_footer(text= "Music Bar", icon_url= "https://telegraf.com.ua/files/2017/12/000000046.jpg")
    await Bot.say(embed= emb)

@Bot.command(pass_context= True)
async def help_moder(ctx):
    emb = discord.Embed(title= "Помощь по командам:", description= "", color = 12390624)
    emb.add_field(name= "Тест", value= "текст", inline= False)
    emb.set_author(name= "Автор")
    emb.set_footer(text= "Футер текст")
    await Bot.say(embed= emb)

    
Bot.run("NTQxMjE2Mzc3NzI2NDM1MzQy.DzcOuQ.rdTjDo2wjeWFAL7uh3Mb7Y-jhjY")
