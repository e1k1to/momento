import discord
import os
import requests
from keep_alive import keep_alive
from discord.ext import commands

dog_api = 'https://dog.ceo/api/breeds/image/random'
client = commands.Bot(command_prefix = '&',help_command=None,case_insensitive=True)
game = discord.Game("momento | &help")

@client.event
async def on_ready():
    print('bora')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=game)

@client.command(pass_content=True)
async def regra10(ctx,member:discord.Member,nome='Nick Irregular', *args):
    nick = nome
    for arg in args:
      nick += " {}".format(arg)
    await ctx.send('```Nick de {} Alterado para "{}"```'.format(member,nick.strip()))
    await member.edit(nick=nick)

@regra10.error
async def info_error(ctx,error):
    if isinstance(error,commands.MemberNotFound):
      await ctx.send("```Usuário inválido```")

@client.command(pass_content=True)
async def id(ctx,id_da_pessoa):
    await ctx.send("<@!{}>".format(id_da_pessoa)) if len(id_da_pessoa) == 18 else await ctx.send("```Erro: Id inválido```")

@client.command(pass_content=True)
async def nick(ctx,member:discord.Member=None):
    await ctx.send(member)

@nick.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("```Erro: Id inválido ou dono do id não está no servidor.```")


@client.command()
async def wow(ctx):
    await ctx.send("https://media.discordapp.net/attachments/822624250292469803/865587237503893527/unknown.png")

@client.command()
async def cachorro(ctx):
    req = requests.get(dog_api)
    chorro = req.json()
    await ctx.send(chorro['message'])

@client.command()
async def help(ctx):
    await ctx.send('''
    ```Comandos:
    &id {id da pessoa} => Marca o dono do ID.
    
    &nick {id da pessoa} => Mostra o Nick e HashTag do dono do ID. (Caso o dono do ID não esteja no server, será retornado um erro.)

    &regra10 {id da pessoa} {nick novo}=> Muda o nick da pessoa para o nick novo. Se "nick novo" estiver vazio, o nick será "Nick Irregular"
    
    &wow => wow
    
    &cachorro => Manda foto de um cachorro :)

    &help => Mostra esse texto.
    
    Para sugestões ou perguntas adicione Eiki.#6969```
    ''')

keep_alive()

client.run(os.environ['TOKEN'])