import os
import discord
from discord.ext import commands
import random

print('Está vivo!!!')

client = discord.Client()

@client.event
async def on_ready():
  print('Estou logado como {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$d20'):
    await message.channel.send(f'Seu resultado: {random.randint(1, 20)}')
  
  if message.content.startswith('$video'):
    await message.channel.send(f'Video: https://www.youtube.com/watch?v=SPTfmiYiuok')
  
  if message.content.startswith('$image'):
    await message.channel.send(f'image: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkozfDxmnmovg2tDYpHHC3JG9ttFBZCGNoP-F71Efwp_JVmlVmtQH5NdyE_aULWtEG-DM&usqp=CAU')


senha_do_bot = os.environ['TOKEN']

client.run(senha_do_bot)
