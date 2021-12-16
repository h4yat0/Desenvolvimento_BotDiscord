import random
from os import environ
import discord
import psycopg2
from discord import message
from discord.ext import commands  # , tasks

# import requests
# import datetime
# import json
# import aiohttp

# # -> Conexão com banco de dados
# conexao_banco_de_dados = psycopg2.connect(
#     host=environ.get('DB_HOST'),
#     dbname=environ.get('DB_NAME'),
#     user=environ.get('DB_USER'),
#     password=environ.get('DB_PASSWORD'))
#
# cur = conexao_banco_de_dados.cursor()
# cur.execute("SELECT * FROM players;")
# print(cur.fetchall())
# conexao_banco_de_dados.commit()
# cur.close()

# -> Prefixo Definido
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Estou logado como {0.user}'.format(client))


@client.command()
async def ping(ctx):
    await ctx.send('Pong')


# @client.event
# async def on_message(message):
#     msg = message.content
#     if message.author == client.user:
#         return


# ===================== Comandos de Help ===============================================================

@client.command(aliases=['helpe'])
async def helpme(ctx):
    await ctx.channel.send(':bookmark_tabs: Veja os comandos abaixo \n\n')
    await ctx.channel.send('‎‎')
    await ctx.channel.send('.dado + (d2, d4, d6, d8, d10, d12, d20)\n'
                           '.video\n'
                           '.image\n'
                           '.classes\n'
                           '    ')


# ===================== Comandos de Dado ===============================================================

@client.command()
async def dado(ctx, *dados):
    username = ctx.message.author.mention
    for _dados in dados:
        dice_location = _dados.find('d')
        if dice_location != -1:
            if dice_location == 0:
                await ctx.channel.send(f'{username} {_dados} --> {random.randint(1, int(_dados[dice_location + 1:]))}')
            if _dados[0].isnumeric() and _dados[0] != 0:
                number_of_repetitions = int(_dados[:dice_location])
                final_value = 0
                summation = '['

                for i in range(number_of_repetitions):
                    roll = random.randint(1, int(_dados[dice_location + 1:]))
                    final_value += roll
                    summation = summation + str(roll) + '+'
                await ctx.channel.send(f'{username} {_dados} {summation[:-1]}] --> {final_value}')
        else:
            await ctx.channel.send(f'{username} Dado não idêntificado!')


# ===================== Comandos Classes ================================================================

@client.command()
async def classes(ctx):
    await ctx.channel.send(
        'Escolha uma classe: \n\nGuerreiro\nFeiticeiro\nLadino\nBarbáro\nBardo\nBruxo\nClérigo\nDruida\nMago'
        '\nMonge\nPaladino')


# ===================== Comandos de imagem ou vídeo ====================================================

@client.command()
async def send_video(ctx):
    await ctx.channel.send(f'Video: https://www.youtube.com/watch?v=SPTfmiYiuok')


@client.command()
async def send_image(ctx):
    await ctx.channel.send(
        f'image: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkozfDxmnmovg2tDYpHHC3JG9ttFBZCGNoP'
        f'-F71Efwp_JVmlVmtQH5NdyE_aULWtEG-DM&usqp=CAU')


password = environ.get('TOKEN')

client.run(password)
