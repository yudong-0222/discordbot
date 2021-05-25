import discord
from discord import message
from discord.ext import commands
import random
import json
import os


with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='[')


@bot.event
async def on_ready():
    print(">>Bot is online!<<")
    channel = bot.get_channel(845966992485253150)
    await channel.send('**>>bot加入了戰場 看我的大雞雞<<**')

    @bot.command()
    async def sayd(ctx,  *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @bot.command()
    async def clean(ctx, num: int):
        await ctx.channel.purge(limit=num+1)
    @bot.command()
    async def HP(ctx):
        await ctx.channel.send('**小雞雞所飼養的雞雞 VER 0.3-b**')  
        await ctx.channel.send('**指令列表**')  
        await ctx.channel.send('載入中...')  
        await ctx.channel.send('**尚未支援**')  
        await ctx.channel.send('**尚未支援**')  
        await ctx.channel.send('**小雞雞所飼養的雞雞 VER 0.3-b**') 





bot.run('ODQ2MjI0NzY3MTk1NTQ1NjMw.YKsaOg.I_K4Droo2FtLLTb_jGthmWAA-QI')        