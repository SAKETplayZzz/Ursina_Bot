import discord
from discord.ext import commands
################
def wake_up_the_bot():
  from flask import Flask
  from threading import Thread
  app = Flask('')
  @app.route('/')
  def home():
      return """<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ?controls=0?autoplay=1" title="Never gonna give you up" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
  def run():
    app.run(host='0.0.0.0',port=8080)
  t = Thread(target=run)
  t.start()
wake_up_the_bot()
client = discord.Client()


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='NOTHING'))
  print('connected {0.user}'.format(client))

from text import *
'''We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye'''
@client.event
async def on_message(message):
  if message.author != client.user:# problem !rule command dosent work u forgot to add the rules
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
    if message.content.startswith(('!commands', '!cmds', '!cmd', '!help')):
      await message.channel.send(commands)
    if message.content.startswith(('!github', '!gh')):
      await message.channel.send('``This is the github`` https://github.com/pokepetter/ursina')
    if message.content.startswith('!api'):
      await message.channel.send('``This is the api refrence`` - https://www.ursinaengine.org/cheat_sheet.html')
    if message.content.startswith(('!info', '!ursina', '!Ursina')):
      await message.channel.send('``Ursina`` makes it easier to develop games, visualizations and other kinds of software,with ``Python!``')
    if message.content.startswith('!msg'):
      await message.channel.send('``This how you post your code``'
                             'https://discord.com/channels/593486730187899041/593501819213316185/815179461711757321')
    if message.content.startswith('!mcclone'):
      await message.channel.send('``Refer this`` - https://github.com/pokepetter/ursina/blob/master/samples/minecraft_clone.py')
    if message.content.startswith(("!shaders", "!shader")):
      await message.channel.send('``Check this out for the type of shaders and an example`` - https://www.ursinaengine.org/cheat_sheet.html#shaders')
    if message.content.startswith("!entity"):
      await message.channel.send('``Check this out for understanding entitys`` - https://www.ursinaengine.org/cheat_sheet.html#Entity')
    if message.content.startswith("!mcinfgen"):
      await message.channel.send('*Procedural generation* can be achieved by using the mesh class wisely or by *creating multiple entities around the player in a chunked manner.*')
    if message.content.startswith("@helper"):
      await message.channel.send('``Please be patient ``')
    if message.content.startswith(("!exitb", "How to remove exit button ?")):
      await message.channel.send('``window.exit_button.enabled = False``')
    if message.content.startswith(("!fpscnt", "How to hide the FPS counter ?")):
      await message.channel.send('``window.fps_counter.enabled = False``')
    if message.content.startswith(("!xhair", "How to hide the change the FirstPersonController crosshair ?")):
      await message.channel.send('``change player.cursor to a different entity``')
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
    await client.process_commands(message)

import os
client.run(os.getenv("TOKEN"))
'''New command Add on opt

    if message.content.lower().startswith(('', '')):
      await message.channel.send(''' ''')
'''