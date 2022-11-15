import os


import discord
from discord.ext import commands
import requests


intents = discord.Intents.all()

helpCommand=commands.DefaultHelpCommand(no_category='Commands')

bot=commands.Bot(command_prefix='!Gavin', intents=intents, helpCommmand=helpCommand)


@bot.event
async def on_connect():
  print("Your bot is online")



@bot.command(brief="play tic tac toe using an API!")
async def TTT(ctx,state,player):
  

  url = "https://stujo-tic-tac-toe-stujo-v1.p.rapidapi.com/"+state+"/"+player

  headers = {
  	"X-RapidAPI-Key": "c076970653mshf55839d326b1e54p197082jsn2134344cf5de",
  	"X-RapidAPI-Host": "stujo-tic-tac-toe-stujo-v1.p.rapidapi.com"
  }
  
  response = requests.request("GET", url, headers=headers)
  response = response["recommendation"]
  await ctx.send(response.text)



my_secret = os.environ['TOKEN']
bot.run(my_secret)