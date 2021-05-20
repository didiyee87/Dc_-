import discord 
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='[',intents = intents)

@bot.event 
async def on_ready():
    print(">>Bot is online<<")


@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(825789805370540056)
    await channel.send(f'{member} 好遮')
    print(f'{member} 好遮')

bot.run('ODQ0NjA0MjQ5Njg1MDk4NTU2.YKU1AQ.VW5NljLDv-pKicPcEPC8QO4nGzQ') 