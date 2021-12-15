import discord
import random
from os import environ
from discord.ext import commands


# -> Prefixo Definido
bot = commands.Bot(command_prefix='.')

client = discord.Client()


@client.event
async def on_ready():
    print('Estou logado como {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    # ===================== Comandos de Help ============================
    if msg.startswith('.help'):
        await message.channel.send(f':bookmark_tabs: Veja os comandos abaixo :bookmark_tabs: \n\n')
        await message.channel.send(f'‎‎')
        await message.channel.send(f':small_blue_diamond: .dado + (d2, d4, d6, d8, d10, d12, d20)')
        await message.channel.send(f':small_blue_diamond: .video')
        await message.channel.send(f':small_blue_diamond: .image')
        await message.channel.send(f':small_blue_diamond: .classe')

    # ===================== Comandos de Dado ============================

    if msg.startswith('.dado'):
        dices = ['d2', 'd4', 'd6', 'd8', 'd10', 'd12', 'd20']
        dice = msg.split('.dado ', 1)[1]

        if dice in dices:
            dice = dice.lower()
            dice = int(dice.replace('d', ''))
            await message.channel.send(f'Seu resultado: {random.randint(1, dice)}')

        else:
            await message.channel.send(
                'Digite um um dado entre as opções: \n\nd2  - dado de 2  lados \nd4  - dado de 4  lados\nd6  - dado '
                'de 6  lados\nd8  - dado de 8  lados\nd10 - dado de 10 lados\nd12 - dado de 12 lados\nd20 - dado de '
                '20 lados')

    # ===================== Comandos Classes ============================

    if msg.startswith('.classe'):
        await message.channel.send(
            'Escolha uma classe: \n\nGuerreiro\nFeiticeiro\nLadino\nBarbáro\nBardo\nBruxo\nClérigo\nDruida\nMago'
            '\nMonge\nPaladino') 

    # ===================== Comandos de imagem ou vídeo ============================

    if msg.startswith('$video'):
        await message.channel.send(f'Video: https://www.youtube.com/watch?v=SPTfmiYiuok')

    if msg.startswith('$image'):
        await message.channel.send(
            f'image: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkozfDxmnmovg2tDYpHHC3JG9ttFBZCGNoP-F71Efwp_JVmlVmtQH5NdyE_aULWtEG-DM&usqp=CAU')


password = environ.get('TOKEN')

client.run(password)
