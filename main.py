import discord
import time
import requests
from discord.ext import tasks
from dotenv import load_dotenv
load_dotenv()
bot = discord.Client()


def getprice():
    url = 'https://api.pancakeswap.info/api/v2/tokens/0x5d4eaf65b348be3889193913ef366d306a9fbd73'
    data = requests.get(url).json()
    price = float(data['data']['price'][:6])  # to get the first 6 d
    return(price)
print(getprice())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord! ')
    for guild in bot.guilds:
        print("connected to ", guild.name)
    refresh_price.start()

    print('The Crypto Token Price Bot is ready!')

@tasks.loop(seconds=float(60))
async def refresh_price():
    for guild in bot.guilds:
        price = getprice()
        NAME = "RVT(Bsc)"
        er = (f"{NAME}: ${price}")
        await guild.me.edit(nick= er)
        print(er)


bot.run(TOKEN)
