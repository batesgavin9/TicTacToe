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
  count=0
  turn=""
  global button1

  
  button1=Button(label = " ")   
  button2=Button(label = " ")
  button3=Button(label = " ")
  button4=Button(label = " ", row=1)
  button5=Button(label = " ", row=1)
  button6=Button(label = " ", row=1)
  button7=Button(label = " ", row=2)
  button8=Button(label = " ", row=2)
  button9=Button(label = " ", row=2)
 
  async def buttonClick():
    if button1==Button(label="X"):
      count+1
      turn+="X"
    elif button1==Button(label="O"):
      turn+="O"
    elif button1!=Button(label="O")&button1!=Button(label="X"):
      turn+="-"
    if button2==Button(label="X"):
      count+1
    elif button2==Button(label="O"):
      turn+="O"
    elif button2!=Button(label="O")&button2!=Button(label="X"):
      turn+="-"
    if button3==Button(label="X"):
      count+1
    elif button3==Button(label="O"):
      turn+="O"
    elif button3!=Button(label="O")&button3!=Button(label="X"):
      turn+="-"
    if button4==Button(label="X"):
      count+1
    elif button4==Button(label="O"):
      turn+="O"
    elif button4!=Button(label="O")&button4!=Button(label="X"):
      turn+="-"
    if button5==Button(label="X"):
      count+1
    elif button5==Button(label="O"):
      turn+="O"
    elif button5!=Button(label="O")&button5!=Button(label="X"):
      turn+="-"
    if button6==Button(label="X"):
      count+1
    elif button6==Button(label="O"):
      turn+="O"
    elif button6!=Button(label="O")&button6!=Button(label="X"):
      turn+="-"
    if button7==Button(label="X"):
      count+1
    elif button7==Button(label="O"):
      turn+="O"
    elif button7!=Button(label="O")&button7!=Button(label="X"):
      turn+="-"
    if button8==Button(label="X"):
      count+1
    elif button8==Button(label="O"):
      turn+="O"
    elif button8!=Button(label="O")&button8!=Button(label="X"):
      turn+="-"
    if button9==Button(label="X"):
      count+1
    elif button9==Button(label="O"):
      turn+="O"
    elif button9!=Button(label="O")&button9!=Button(label="X"):
      turn+="-"
      

  async def button1Clicked(interaction):
    await interaction.response.send_message("thanks ")
    buttonClick()
    if count%2!=0:
      print("KillYRSELF")
    #WORKING HERE
    #NEED to figure out how to change labels once clicked on a button
    #Then we need to use the imput from the buttonClick() function to somehow use the api to get the best move
      
    
    
    
 
  button1.callback=button1Clicked
  view=View()
 
  view.add_item(button1)  
  view.add_item(button2)
  view.add_item(button3)
  view.add_item(button4)
  view.add_item(button5)
  view.add_item(button6)
  view.add_item(button7)
  view.add_item(button8)
  view.add_item(button9)

 
 

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