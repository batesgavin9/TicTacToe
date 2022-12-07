import os
import discord
from discord.ext import commands
import requests
from discord.ui import Button,View

intents = discord.Intents.all()

helpCommand=commands.DefaultHelpCommand(no_category='Commands')

bot=commands.Bot(command_prefix='!GavinL', intents=intents, helpCommmand=helpCommand)


@bot.event
async def on_connect():
  print("Your bot is online")



@bot.command(brief="play tic tac toe using an API!")
async def TTT(ctx):
 
  global id
  #global rowforbutton
  rowforbutton=3
  global turn
  global gameover
  global count
  count=0
  turn=""
  global button1
  totalPlays=0

  global buttons
  button1=Button(label = " ", row=0, custom_id="0")  
  button2=Button(label = " ", row=0, custom_id="1")
  button3=Button(label = " ", row=0, custom_id="2")
  button4=Button(label = " ", row=1, custom_id="3")
  button5=Button(label = " ", row=1, custom_id="4")
  button6=Button(label = " ", row=1, custom_id="5")
  button7=Button(label = " ", row=2, custom_id="6")
  button8=Button(label = " ", row=2, custom_id="7")
  button9=Button(label = " ", row=2, custom_id="8")
  buttons=[button1, button2, button3, button4, button5, button6, button7, button8, button9] #made the buttons into list
 
  async def buttonClick():
    #this code lets us know which button was clicked 1 through 9
    global id
    nonlocal rowforbutton
    global buttons
    global turn
    turn="---------"
    nonlocal totalPlays
    totalPlays+=1

    turnLetter=""
    #This alternates X and O - I thought we would need this but we dont
    if totalPlays%2==0:
      turnLetter="X"
    else: 
      turnLetter="O"
    #buttons[int(id)]=Button(label = "O")
    #view=View()
    #for b in buttons:
      #view.add_item(b)  
    #else:
    #buttons[int(id)]=Button(label = "X")
    #view=View()
    #for b in buttons:
      #view.add_item(b)  

   
    print("Function ran"+ id)
    print(buttons[int(id)]) #gets correctly clicked button from list using the id
    buttons[int(id)]=Button(label = turnLetter, row=rowforbutton, style=discord.ButtonStyle.red)
    buttons[int(id)].disabled=True
    view=View()
    count=+1
    turn+="X"             #according to console it added 1 to count variable
    print(count)



  #-----------------------------------------------------
  #This works in trinket havent been able to test because phone dont work
  #now we just need to change it so it adds the O
  #I added back the alternatnig x and o

    turn="---------"
    

    for i in range(len(turn)):
      if i==id:
        if totalPlays%2==0:
          turn+="X"
        else:
          turn+="O"
      else:
        turn+=turn[i:i+1]

    turn = turn[-9:]



    print(turn)



  #IF DOESNT WORK
  #THIS WILL FS WORK-


    #turn="---------"
    #id=8

    #for i in range(len(turn)):
      #if i==id:
        #turn+="X"
      #else:
        #turn+=turn[i:i+1]

    #turn = turn[-9:]



    #print(turn)











    
    
    for b in buttons:
      view.add_item(b)  
   
   

    await ctx.send("hello1",view=view)
   
    # if buttons[int(id)]==Button(label="X"):      tried to do the code above right here but it didn't work.
    #   count=+1
    #   turn+="X"
    #   print(count)
    # elif button1==Button(label="O"):
    #   turn+="O"
    # elif button1!=Button(label="O")&button1!=Button(label="X"):
    #   turn+="-"
    # if button2==Button(label="X"):
    #   turn+="X"
    # elif button2==Button(label="O"):
    #   turn+="O"
    # elif button2!=Button(label="O")&button2!=Button(label="X"):
    #   turn+="-"
    # if button3==Button(label="X"):
    #   turn+="X"
    # elif button3==Button(label="O"):
    #   turn+="O"
    # elif button3!=Button(label="O")&button3!=Button(label="X"):
    #   turn+="-"
    # if button4==Button(label="X"):
    #   turn+="X"
    # elif button4==Button(label="O"):
    #   turn+="O"
    # elif button4!=Button(label="O")&button4!=Button(label="X"):
    #   turn+="-"
    # if button5==Button(label="X"):
    #   turn+="X"
    # elif button5==Button(label="O"):
    #   turn+="O"
    # elif button5!=Button(label="O")&button5!=Button(label="X"):
    #   turn+="-"
    # if button6==Button(label="X"):
    #   turn+="X"
    # elif button6==Button(label="O"):
    #   turn+="O"
    # elif button6!=Button(label="O")&button6!=Button(label="X"):
    #   turn+="-"
    # if button7==Button(label="X"):
    #   turn+="X"
    # elif button7==Button(label="O"):
    #   turn+="O"
    # elif button7!=Button(label="O")&button7!=Button(label="X"):
    #   turn+="-"
    # if button8==Button(label="X"):
    #   turn+="X"
    # elif button8==Button(label="O"):
    #   turn+="O"
    # elif button8!=Button(label="O")&button8!=Button(label="X"):
    #   turn+="-"
    # if button9==Button(label="X"):
    #   turn+="X"
    # elif button9==Button(label="O"):
    #   turn+="O"
    # elif button9!=Button(label="O")&button9!=Button(label="X"):
    #   turn+="-"



    state=turn
    player="O"
   
    url = "https://stujo-tic-tac-toe-stujo-v1.p.rapidapi.com/"+state+"/"+player
    my_secretAPI = os.environ['TTT']
    headers = {
    "X-RapidAPI-Key": my_secretAPI,
    "X-RapidAPI-Host": "stujo-tic-tac-toe-stujo-v1.p.rapidapi.com"
    }
   
    response = requests.request("GET", url, headers=headers)

    print(response)


 
  async def button1Clicked(interaction):
    global id
    nonlocal rowforbutton
    global button1
    rowforbutton=0
    id=interaction.data["custom_id"]
    print(id)
    await interaction.response.send_message("thanks ")
    button1.disabled=True
    await buttonClick()
    
    if count%2!=0:
      print("F")
    else:
      print("E")
   
 
  async def button2Clicked(interaction):
    global id
    nonlocal rowforbutton
    rowforbutton=0
    id=interaction.data["custom_id"]
    print(id)
    await interaction.response.send_message("thanks ")
    await buttonClick()
    if count%2!=0:
      print("F")
    else:
      print("E")
   
  async def button3Clicked(interaction):
    global id
    nonlocal rowforbutton
    rowforbutton=0
    id=interaction.data["custom_id"]
    print(id)
    await interaction.response.send_message("thanks ")
    await buttonClick()
    if count%2!=0:
      print("F")
    else:
      print("E")

  async def button4Clicked(interaction):
    global id
    nonlocal rowforbutton
    rowforbutton=1
    id=interaction.data["custom_id"]
    print(id)
    await interaction.response.send_message("thanks ")
    await buttonClick()
    if count%2!=0:
      print("F")
    else:
      print("E")  

  async def button5Clicked(interaction):
    global id
    nonlocal rowforbutton
    rowforbutton=1
    id=interaction.data["custom_id"]
    print("rowforbutton")
    await interaction.response.send_message("thanks ")
    await buttonClick()
    if count%2!=0:
      print("F")
    else:
      print("E")    

  async def button6Clicked(interaction):
    global id
    nonlocal rowforbutton
    rowforbutton=1
    id=interaction.data["custom_id"]
    print(id)
    await interaction.response.send_message("thanks ")
    await buttonClick()
    if count%2!=0:
      print("F")
    else:
      print("E")

  async def button7Clicked(interaction):
    global id
    nonlocal rowforbutton
    rowforbutton=2
    id=interaction.data["custom_id"]
    print(id)
    await interaction.response.send_message("thanks ")
    await buttonClick()
    if count%2!=0:
      print("F")
    else:
      print("E")    

  async def button8Clicked(interaction):
    global id
    nonlocal rowforbutton
    rowforbutton=2
    id=interaction.data["custom_id"]
    print("id")
    await interaction.response.send_message("thanks ")
    await buttonClick()
    if count%2!=0:
      print("F")
    else:
      print("E")    

  async def button9Clicked(interaction):
    global id
    nonlocal rowforbutton
    rowforbutton=2
    id=interaction.data["custom_id"]
    print(id)
    await interaction.response.send_message("thanks ")
    await buttonClick()
    if count%2!=0:
      print("F")
    else:
      print("E")    
   
 
  button1.callback=button1Clicked
  button2.callback=button2Clicked
  button3.callback=button3Clicked
  button4.callback=button4Clicked
  button5.callback=button5Clicked
  button6.callback=button6Clicked
  button7.callback=button7Clicked
  button8.callback=button8Clicked
  button9.callback=button9Clicked
  view=View()
 
  view.add_item(button1)  
  view.add_item(button5)
  view.add_item(button6)
  view.add_item(button7)
  view.add_item(button8)
  view.add_item(button9)

 
 

 
 
  await ctx.send("hello",view=view)

my_secret = os.environ['TOKEN']
bot.run(my_secret)