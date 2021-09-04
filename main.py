import discord
from discord.ext import commands
from dotenv import load_dotenv

import os


load_dotenv()


client = commands.Bot(command_prefix="!")


@client.remove_command('help')
@client.command(name="help", description="Show this menu", aliases=['cmd', 'cmds', 'commands'])
async def get_help(ctx, commandename=""):
    """
    show a list of all the commands the bot has
    """
    to_send = """\n> \n> **Commands List** : \n"""
    to_send += "> \n"
    for commande in client.commands:
        to_send += "> \n"
        to_send += f"""> `!{commande.name}` : {commande.description}\n"""

    to_send += "> \n"
    to_send += f"""> _Bot created for the **Ursina** discord server_ \n"""
    await ctx.send(content=to_send)


@client.command(name="github", description="Show the link to the official ursina github", aliases=['gh', 'git'])
async def github(ctx):
    await ctx.send(f'``This is the github`` https://github.com/pokepetter/ursina')


@client.command(name="api", description="Link you to the Api reference")
async def api(ctx):
    await ctx.send(f'``This is the api refrence`` - https://www.ursinaengine.org/cheat_sheet.html')


@client.command(name="ursina", description="Gives you info about what is Ursina", aliases=['info', 'Ursina'])
async def ursina(ctx):
    await ctx.send(f'``Ursina`` makes it easier to develop games, visualizations and other kinds of software,with ``Python!``')


@client.command(name="msg", description="Show you how an help on how to post code")
async def msg(ctx):
    await ctx.send(f'``This how you post your code``'
                     'https://discord.com/channels/593486730187899041/593501819213316185/815179461711757321')


@client.command(name="mcclone", description="How to make a minecraft clone", aliases=['minecraft-clone', 'minecraft'])
async def mcclone(ctx):
    await ctx.send(f'``Refer this`` - https://github.com/pokepetter/ursina/blob/master/samples/minecraft_clone.py')


@client.command(name="shaders", description="Quick information about what are shaders and how use them", aliases=['shader'])
async def shaders(ctx):
    await ctx.send(f'``Check this out for the type of shaders and an example`` - https://www.ursinaengine.org/cheat_sheet.html#shaders')

@client.command(name="entity", description="Show you how an help on how to post code")
async def entity(ctx):
    await ctx.send(f'``Check this out for understanding entitys`` - https://www.ursinaengine.org/cheat_sheet.html#Entity')

@client.command(name="mcinfgen", description="Show you how an help on how to post code")
async def inf_gen(ctx):
    await ctx.send(f'*Procedural generation* can be achieved by using the mesh class wisely or by *creating multiple entities around the player in a chunked manner.*')

@client.command(name="exit-button", description="How to remove exit button",aliases=['exitbutton','exitb'])
async def exit_b(ctx):
    await ctx.send(f'``window.exit_button.enabled = False``')

@client.command(name="fps-counter", description="How to hide the FPS counter ?",aliases=['fpscnt','exitb'])
async def fps_cnt(ctx):
    await ctx.send(f'``window.fps_counter.enabled = False``')

@client.command(name="crosshair", description="How to hide the change the FirstPersonController crosshair ?",aliases=['xhair','cross-hair'])
async def xhair(ctx):
    await ctx.send(f'``change player.cursor to a different entity``')



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help"))
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

client.run(os.getenv("TOKEN"))


"""
    if message.content.startswith(("!tex", "What files can I use as texture in ursina ?")):
        await message.channel.send('``.tif, .jpg, .jpeg, .png, .gif, .mp4``')
    if message.content.startswith(("!mod", "What files can I use as models in ursina ?")):
        await message.channel.send('``.bam, .ursinamesh, .obj, .glb, .gltf, .blend``')
    if message.content.startswith(("!col","!Col", "How can I add collisions to my game with ursina ?")):
        await message.channel.send('``.bam, .ursinamesh, .obj, .glb, .gltf, .blend``')
    if message.content.startswith(("!rel", "How can I release my game with ursina ?")):
        await message.channel.send('``You can release your game here - https://www.ursinaengine.org/building.html``')
    if message.content.lower().startswith(('!gif', '!animation', '!animations')):
        await message.channel.send('To load a `.gif` file use `Animation(‘gifName.gif’)`')
    if message.content.lower().startswith('!mesh'):
        await message.channel.send('To make a mesh use `Mesh(vertices, triangles)`')
    if message.content.lower().startswith(('!audio', '!aud', '!music')):
        await message.channel.send('''To play a sound use `Audio()`''')
    if message.content.lower().startswith(('!rule', '!rules')):
        await message.channel.send(RuLe)
    if message.content.lower().startswith(('!py', '!python')):
        await message.channel.send('''**Python** is a easy to learn and use programming languege. It is present in `Top 5 Programming Languages`.''')
    if message.content.lower().startswith(('!chan','!chans','!channels','!channel')):
        await message.channel.send('''- Here's a list of channels with there uses 
1.	#help  –  For help.
2.	#help_2 – For help, only use if #help is busy.
3.	#devlopment – For development of ursina engine.
4.	#show_off – To show off your games.
5.	#github – To see the commits of ursina engine's github.
6.	#tect – For stuff related to technology.
7.	#general – For general stuff.
''')


    if message.content.lower().startswith('!doc entity'):
        await message.channel.send(Entitydoc)
    if message.content.lower().startswith('!doc text'):
        await message.channel.send(textdoc)
    if message.content.lower().startswith('!doc button'):
        await message.channel.send(buttondoc)
    if message.content.lower().startswith('!doc mouse'):
        await message.channel.send(mousedoc)
    if message.content.lower().startswith('!doc raycast'):
        await message.channel.send(raycastdoc)
"""
