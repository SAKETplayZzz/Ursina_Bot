import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from math import ceil


import ursina_doc
from docs import CheatSheet

load_dotenv()

BOT_PREFIX = "." if os.getenv("DEBUG") else "!"


cheatsheet = CheatSheet(local_html="test_data/ursina_cheat_sheet.html")

client = commands.Bot(case_insensitive=True, command_prefix=BOT_PREFIX)


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


@client.command(name="ursina", description="Gives you info about what is Ursina", aliases=['info'])
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

@client.command(name="fps-counter", description="How to hide the FPS counter ?",aliases=['fpscnt','fpscounter'])
async def fps_cnt(ctx):
    await ctx.send(f'``window.fps_counter.enabled = False``')

@client.command(name="crosshair", description="How to hide the change the FirstPersonController crosshair ?",aliases=['xhair','cross-hair'])
async def xhair(ctx):
    await ctx.send(f'``change player.cursor to a different entity``')

@client.command(name="textures", description="What file type can I use as textures",aliases=['texture','tex'])
async def tex(ctx):
    await ctx.send(f'``.tif, .jpg, .jpeg, .png, .gif, .mp4``')

@client.command(name="model", description="What file type can I use as models",aliases=['models','mod'])
async def mod(ctx):
    await ctx.send(f'``.bam, .ursinamesh, .obj, .glb, .gltf, .blend``')

@client.command(name="collision", description="How can I add collisions to my game with ursina ?",aliases=['collisions','col'])
async def col(ctx):
    await ctx.send(f'There you go : https://www.ursinaengine.org/collision.html')

@client.command(name="build", description="How can I release my game with ursina ?",aliases=['release','rel'])
async def release(ctx):
    await ctx.send(f'``Follow this guide - https://www.ursinaengine.org/building.html``')

@client.command(name="gif", description="How can I load a `.gif` file ?",aliases=['animation','animations'])
async def gif(ctx):
    await ctx.send(f'To load a `.gif` file use `Animation(‘gifName.gif’)`')

@client.command(name="mesh", description="How to create a mesh ?")
async def mesh(ctx):
    await ctx.send(f'To make a mesh use `Mesh(vertices, triangles)`')

@client.command(name="sound", description="How can I load a `.gif` file ?",aliases=['audio','music','aud'])
async def gif(ctx):
    await ctx.send(f'To play a sound use `Audio()`')

@client.command(name="channels", description="List all channels and their use cases",aliases=['channel','chan','chans'])
async def chan(ctx):
    await ctx.send(f'''- Here's a list of channels with there uses 
1.	#help  –  For help.
2.	#help_2 – For help, only use if #help is busy.
3.	#devlopment – For development of ursina engine.
4.	#show_off – To show off your games.
5.	#github – To see the commits of ursina engine's github.
6.	#tect – For stuff related to technology.
7.	#general – For general stuff.
''')


@client.command(name="doc", description="Refer you to the ursina documentation", aliases=['documentation', 'docs'])
async def doc(ctx, snippet=""):
    snippet = snippet.lower()
    if snippet:
        entry = cheatsheet.get_doc(snippet)
        if entry:
            await ctx.send(embed=get_cheatsheet_embed(entry))
        else:
            await ctx.send("Snippet not found")
    else:
        await ctx.send(f'``This is the api refrence`` - https://www.ursinaengine.org/cheat_sheet.html')


def get_cheatsheet_embed(entry: dict) -> discord.Embed:
    zws = "\u200b" # zero width space
    description = entry.get("example") or ""
    label = entry.get("label")
    params = entry.get("params")
    if params:
        description = f"```py\n{params}```\nExample:\n```py\n{description}```"

    embed = discord.Embed(
        title=label,
        description= description,
        color=0xf3e6a5
    )
    methods = entry.get("methods")
    if methods:
        methods_string = ""
        row_count = ceil(len(methods)/2.0)
        for m in methods[:row_count]:
            methods_string += f"`{m}`\n"
        embed.add_field(name="Methods:", value=methods_string, inline=True)
        if row_count > 1:
            methods_string = ""
            for m in methods[row_count:]:
                methods_string += f"`{m}`\n"
            embed.add_field(name=zws, value=methods_string, inline=True)

    source_url = entry.get("github_url")
    cheatsheet_url = "https://www.ursinaengine.org/cheat_sheet_dark.html#" + \
        label.split("(")[0]
    embed.add_field(
        name="More information:",
        value=f"[Source code]({source_url} '{source_url}') – [Cheat sheet]({cheatsheet_url} '{cheatsheet_url}')",
        inline=False)
    return embed



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{BOT_PREFIX}help"))
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

client.run(os.getenv("TOKEN"))
