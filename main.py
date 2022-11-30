import os
import discord
from discord.ext import commands
import requests
from discord.ui import Button,View

intents = discord.Intents.all()

helpCommand=commands.DefaultHelpCommand(no_category='Commands')

bot=commands.Bot(command_prefix='!Gavin', intents=intents, helpCommmand=helpCommand)


@bot.event
async def on_connect():
  print("Your bot is online")



@bot.command(brief="play tic tac toe using an API!")
async def TTT(ctx):
  
  
  global turn
  global gameover
  global count

  global board
  button1=Button(label = " ")
  button2=Button()
  button3=Button()
  button4=Button()
  button5=Button()
  button6=Button()
  button7=Button()
  button8=Button()
  button9=Button()


  async def button1Clicked(interaction):
    await interaction.response.send_message("thanks ")
  
  button1.callback=button1Clicked
  view=View()
  
  view.add_item(button1)
  

  
  

  state="1"
  player="1"
  
  url = "https://stujo-tic-tac-toe-stujo-v1.p.rapidapi.com/"+state+"/"+player
  my_secretAPI = os.environ['TTT']
  headers = {
  	"X-RapidAPI-Key": my_secretAPI,
  	"X-RapidAPI-Host": "stujo-tic-tac-toe-stujo-v1.p.rapidapi.com"
  }
  
  response = requests.request("GET", url, headers=headers)
  
  await ctx.send("hello",view=view)



my_secret = os.environ['TOKEN']
bot.run(my_secret)