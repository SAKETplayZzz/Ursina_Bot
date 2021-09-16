import os
from math import ceil

import discord
from discord_slash import SlashCommand
from dotenv import load_dotenv

from docs import CheatSheet

load_dotenv()


guild_ids = [int(var) for var in os.getenv("GUILD_IDS").split(" ")]

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(
    client, sync_commands=True
)  # Declares slash commands through the client.


cheatsheet = CheatSheet()


@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")


@slash.slash(
    name="github",
    description="Show the link to the official ursina github",
    guild_ids=guild_ids,
)
async def _github(ctx):
    await ctx.send("https://github.com/pokepetter/ursina")


@slash.slash(
    name="api", description="Link you to the Api reference", guild_ids=guild_ids
)
async def _api(ctx):
    await ctx.send("https://www.ursinaengine.org/cheat_sheet_dark.html")


@slash.slash(
    name="ursina",
    description="Gives you info about what is Ursina",
    guild_ids=guild_ids,
)
async def _ursina(ctx):
    await ctx.send(
        f"``Ursina`` makes it easier to develop games, visualizations and other kinds of software,with ``Python!``"
    )


@slash.slash(
    name="msg",
    description="Show you how an help on how to post code",
    guild_ids=guild_ids,
)
async def _msg(ctx):
    await ctx.send(
        "``This how you post your code``"
        "https://discord.com/channels/593486730187899041/593501819213316185/815179461711757321"
    )


@slash.slash(
    name="mcclone", description="How to make a minecraft clone", guild_ids=guild_ids
)
async def _mcclone(ctx):
    await ctx.send(
        "https://github.com/pokepetter/ursina/blob/master/samples/minecraft_clone.py"
    )


@slash.slash(
    name="shaders",
    description="Quick information about what are shaders and how use them",
    guild_ids=guild_ids,
)
async def _shaders(ctx):
    await ctx.send(
        f"``Check this out for the type of shaders and an example`` - https://www.ursinaengine.org/cheat_sheet.html#shaders"
    )


@slash.slash(
    name="entity",
    description="Show you how an help on how to post code",
    guild_ids=guild_ids,
)
async def _entity(ctx):
    await ctx.send(
        f"``Check this out for understanding entitys`` - https://www.ursinaengine.org/cheat_sheet.html#Entity"
    )


@slash.slash(
    name="mcinfgen",
    description="Show you how an help on how to post code",
    guild_ids=guild_ids,
)
async def _inf_gen(ctx):
    await ctx.send(
        f"*Procedural generation* can be achieved by using the mesh class wisely or by *creating multiple entities around the player in a chunked manner.*"
    )


@slash.slash(
    name="exit-button", description="How to remove exit button", guild_ids=guild_ids
)
async def _exit_b(ctx):
    await ctx.send("```py\nwindow.exit_button.enabled = False```")


@slash.slash(
    name="fps-counter", description="How to hide the FPS counter ?", guild_ids=guild_ids
)
async def _fps_cnt(ctx):
    await ctx.send("```py\nwindow.fps_counter.enabled = False```")


@slash.slash(
    name="crosshair",
    description="How to hide the change the FirstPersonController crosshair ?",
    guild_ids=guild_ids,
)
async def _xhair(ctx):
    await ctx.send("change ``player.cursor`` to a different entity")


@slash.slash(
    name="textures",
    description="What file type can I use as textures",
    guild_ids=guild_ids,
)
async def _tex(ctx):
    await ctx.send(f"``.tif, .jpg, .jpeg, .png, .gif, .mp4``")


@slash.slash(
    name="model", description="What file type can I use as models", guild_ids=guild_ids
)
async def _mod(ctx):
    await ctx.send(f"``.bam, .ursinamesh, .obj, .glb, .gltf, .blend``")


@slash.slash(
    name="collision",
    description="How can I add collisions to my game with ursina ?",
    guild_ids=guild_ids,
)
async def _col(ctx):
    await ctx.send("https://www.ursinaengine.org/collision.html")


@slash.slash(
    name="build",
    description="How can I release my game with ursina ?",
    guild_ids=guild_ids,
)
async def _release(ctx):
    await ctx.send("https://www.ursinaengine.org/building.html``")


@slash.slash(
    name="gif", description="How can I load a `.gif` file ?", guild_ids=guild_ids
)
async def _gif(ctx):
    await ctx.send(f"To load a `.gif` file use `Animation(‘gifName.gif’)`")


@slash.slash(name="mesh", description="How to create a mesh ?", guild_ids=guild_ids)
async def _mesh(ctx):
    await ctx.send(f"To make a mesh use `Mesh(vertices, triangles)`")


@slash.slash(
    name="sound", description="How can play an audio file ?", guild_ids=guild_ids
)
async def _gif(ctx):
    await ctx.send(f"To play a sound use `Audio()`")


@slash.slash(
    name="channels",
    description="List all channels and their use cases",
    guild_ids=guild_ids,
)
async def _chan(ctx):
    await ctx.send(
        f"- Here's a list of channels with their uses \n \
        1.	#help  –  For help.\n \
        2.	#help_2 – For help, only use if #help is busy.\n \
        3.	#devlopment – For development of ursina engine.\n \
        4.	#show_off – To show off your games.\n \
        5.	#github – To see the commits of ursina engine's github.\n \
        6.	#tect – For stuff related to technology.\n \
        7.	#general – For general stuff."
    )


@slash.slash(
    name="doc", description="Refer you to the ursina documentation", guild_ids=guild_ids
)
async def _doc(ctx, label=""):
    label = label.lower()
    if label:
        entry = cheatsheet.get_doc(label)
        if entry:
            await ctx.send(embed=get_cheatsheet_embed(entry))
        else:
            await ctx.send("Snippet not found")
    else:
        await ctx.send(
            f"``Ursina API reference`` - https://www.ursinaengine.org/cheat_sheet_dark.html"
        )


def get_cheatsheet_embed(entry: dict) -> discord.Embed:
    zws = "\u200b"  # zero width space
    description = entry.get("example") or ""
    label = entry.get("label")
    params = entry.get("params")
    if params:
        description = f"```py\n{params}```\nExample:\n```py\n{description}```"

    embed = discord.Embed(title=label, description=description, color=0xF3E6A5)
    methods = entry.get("methods")
    if methods:
        methods_string = ""
        row_count = ceil(len(methods) / 2.0)
        for m in methods[:row_count]:
            methods_string += f"`{m}`\n"
        embed.add_field(name="Methods:", value=methods_string, inline=True)
        if row_count > 1:
            methods_string = ""
            for m in methods[row_count:]:
                methods_string += f"`{m}`\n"
            embed.add_field(name=zws, value=methods_string, inline=True)

    source_url = entry.get("github_url")
    cheatsheet_url = (
        "https://www.ursinaengine.org/cheat_sheet_dark.html#" + label.split("(")[0]
    )
    embed.add_field(
        name="More information:",
        value=f"[Source code]({source_url} '{source_url}') – [Cheat sheet]({cheatsheet_url} '{cheatsheet_url}')",
        inline=False,
    )
    return embed


client.run(os.getenv("TOKEN"))
