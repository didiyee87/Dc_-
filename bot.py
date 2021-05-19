import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event 
async def on_ready():
    print(">>Bot is online<<")

bot.run('ODQ0NjA0MjQ5Njg1MDk4NTU2.YKU1AQ.O1MNPKpayAjmquGQrTSwLwwyvbY') 