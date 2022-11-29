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
  my_secretAPI = os.environ['TTT']
  headers = {
  	"X-RapidAPI-Key": my_secretAPI,
  	"X-RapidAPI-Host": "stujo-tic-tac-toe-stujo-v1.p.rapidapi.com"
  }
  
  response = requests.request("GET", url, headers=headers)
  
  await ctx.send(response.text)



my_secret = os.environ['TOKEN']
bot.run(my_secret)