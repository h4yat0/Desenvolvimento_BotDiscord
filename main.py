import os
import discord
import random

client = discord.Client()


@client.event
async def on_ready():
  print('Estou logado como {0.user}'.format(client))

@client.event
async def on_message(message):

  msg = message.content

  if message.author == client.user:
    return

  if msg.startswith('.dado'):
    dices = ['d2', 'd4', 'd6', 'd8', 'd10', 'd12', 'd20']
    dice = msg.split('.dado ', 1)[1]

    if dice in dices:
      dice = dice.lower()
      dice =  int(dice.replace('d', ''))
      await message.channel.send(f'Seu resultado: {random.randint(1, dice)}')
    
    else:
      await message.channel.send('Digite um um dado entre as opções: \n\nd2  - dado de 2  lados \nd4  - dado de 4  lados \nd6  - dado de 6  lados \nd8  - dado de 8  lados \nd10 - dado de 10 lados \nd12 - dado de 12 lados \nd20 - dado de 20 lados')

  
  if msg.startswith('$video'):
    await message.channel.send(f'Video: https://www.youtube.com/watch?v=SPTfmiYiuok')
  
  if msg.startswith('$image'):
    await message.channel.send(f'image: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkozfDxmnmovg2tDYpHHC3JG9ttFBZCGNoP-F71Efwp_JVmlVmtQH5NdyE_aULWtEG-DM&usqp=CAU')


senha_do_bot = os.environ['TOKEN']

client.run(senha_do_bot)
