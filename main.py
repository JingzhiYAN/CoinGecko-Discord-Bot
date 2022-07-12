import discord
from discord.ext import commands
import datetime

import json
from urllib.request import Request, urlopen

#-----------------------------------------------------------------------------
#- Config:                                                                   -
#-      name_prj     - The name of the project                               -
#-      token_adr    - The address of the token                              -
#-      abbreviation - The abbreviation of the token                         -
#-      
- Emoji for beautify purpose                            -
#-----------------------------------------------------------------------------

name_prj = "rvtbot"
token_adr = "0x5d4eaf65b348be3889193913ef366d306a9fbd73"
abbreviation = "RVT"
emoji = ""


url = "https://api.pancakeswap.info/api/v2/tokens/"+token_adr


bot = commands.Bot(command_prefix='!', description="This is the price bot for "+name_prj+", best project in the DeFi world!", help_command=None)


#Price-message:
@bot.command()
async def price(ctx):
    #j_token : json with token data-------------------------------------------------
    req = Request(url_cow, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    j_token = json.loads(webpage)
    #---------------------------------------------------------------------------

    embed = discord.Embed()

    embed.description ="""
    **${:s}** {:s}
    Price: $ {:f}
    Price in BNB: {:f}
    💱 [Buy ${:s}](https://pancakeswap.finance/swap?outputCurrency={:s})
    📈 [Poocoin chart](https://poocoin.app/tokens/{:s})
    """.format(abbreviation, emoji, round(float(j_token["data"]["price"]), 6), round(float(j_token["data"]["price_BNB"]), 6), abbreviation, token_adr, token_adr)

    await ctx.send(embed=embed)

@bot.command()
async  def  help(ctx):
    des = """
    Commands for Crypto Token Price Bot:\n
     **Prefix**:       !\n
     **!price**:       Get information about tokens price\n
    """
    embed = discord.Embed(title="I'm the price bot for "+name_prj+", best project in the DeFi world!",url="##########",description= des,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.blue())
    embed.set_footer(text="Made by v0st0k1")


    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))
    print('The Crypto Token Price Bot is ready!')



bot.run('OTgzMTgzNzY0MTgyMTM4OTMx.GBrvcD.tmKI2oxZPRDKN3TqF5UJeM7SOBxIU8M3f4pVpg')
