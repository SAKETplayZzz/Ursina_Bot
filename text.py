commands = ('''@Ursina-Bot commands 
1.`` !github `` or ``!gh``
2.`` !api ``
3.`` !info ``
4.`` !msg `` this tells how to message code in discord
5.`` !mcclone `` gives the link to minecraft clone in github
6.`` !shaders `` tells all the shaders available in ursina
7.`` !entity `` 
8.`` !proced `` gives a short explaination abt how to use procedual gen to achive infinite generation in an minecraft clone
9.``!exitb`` tells hoe to remove exit button
10.``!fps`` tells how to remove fps button
11.``!xhair`` tells how to remove cross hair the cmd is xhair because x is like a cross so xhair
12.``!tex`` tells all the texture formats u can use
13.``!mod`` tells all the model formats which can be used
14.``!col`` tells all the formats of colliders which can be loaded
15.``!rel`` tells how u can release ur ursina game
16.``!cmd`` or ``!cmds`` or``!commands``
17.``!doc Entity``
18.``!doc Entity``
19.``!doc Button``
20.``!doc Text``
21.``!doc Mouse``
22.``!doc Raycast``
*commands 9 to 15 have automated answers if written in the correct way example-*``What files can I use as models in ursina ?``
`` this bot is online 24/7 ``''')
Entitydoc = ('''``Entity(add_to_scene_entities=True, **kwargs)``
``name = camel_to_snake(self.type) ``
``enabled = True    # disabled entities will not be visible nor run code. ``
``visible = True ``
``ignore = False     # if True, will not try to run code. ``
``eternal = False    # eternal entities does not get destroyed on scene.clear() ``
``for more info vist - ``https://www.ursinaengine.org/cheat_sheet.html#Entity

```e = Entity(model='quad', color=color.orange, position=(0,0,1), scale=1.5, rotation=(0,0,45), texture='brick')

#example of inheriting Entity
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model='cube'
        self.color = color.red
        self.scale_y = 2

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'space':
            self.animate_x(2, duration=1)

    def update(self):
        self.x += held_keys['d'] * time.dt * 10
        self.x -= held_keys['a'] * time.dt * 10

player = Player(x=-1)```''')

textdoc = ('''`` Text(text='', start_tag=start_tag, end_tag=end_tag, ignore=True, **kwargs)

size = Text.size 
parent = camera.ui 
text_nodes = list() 
images = list() 
origin = (-.5, .5)``
``for more info on this topic visit -`` https://www.ursinaengine.org/cheat_sheet.html#Text
```from ursina import *
  app = Ursina()
  descr = dedent(
      #<scale:1.5><orange>Rainstorm<default><scale:1>
      #Summon a <azure>rain storm <default>to deal 5 <azure>water

      #damage <default>to <hsb(0,1,.7)>everyone, #<default><image:file_icon> <red><image:file_icon> test #<default>including <orange>yourself. <default>
      #Lasts for 4 rounds.).strip()

  Text.default_resolution = 1080 * Text.size
  test = Text(text=descr, origin=(0,0), background=True)

  def input(key):
      if key == 'a':
          print('a')
          test.text = '<default><image:file_icon> <red><image:file_icon> test '
          print('by', test.text)

  window.fps_counter.enabled = False
  print('....', Text.get_width('yolo'))
  app.run()```
''')
buttondoc = ('''
``Button(text='', **kwargs)``

``parent = camera.ui`` 
``collider = 'box'`` 
``disabled = False ``
``color = Button.color`` 
``text_entity = None ``
``For more info vist - ``https://www.ursinaengine.org/cheat_sheet.html#Button
Example -
```
b = Button(text='hello world!', color=color.azure, icon='sword', scale=.25, text_origin=(-.5,0))
b.on_click = application.quit # assign a function to the button.
b.tooltip = Tooltip('exit')
```''')
mousedoc = ('''
``enabled = False ``
``visible = True ``
``locked = False ``
``position = Vec3(0,0,0)`` 
``delta = Vec3(0,0,0)``
``For more info visit - ``https://www.ursinaengine.org/cheat_sheet.html#mouse
```Button(parent=scene, text='a')

def update():
    print(mouse.position, mouse.point)

Cursor()
mouse.visible = False```''')
raycastdoc = ('''
``distance(a, b)``   
``raycast(origin, direction=(0,0,1), distance=inf, traverse_target=scene, ignore=list(), debug=False) ``  
``boxcast(origin, direction=(0,0,1), distance=9999, thickness=(1,1), traverse_target=scene, ignore=list(), debug=False)   # similar to raycast, but with width and height``
``for more info visit - ``https://www.ursinaengine.org/cheat_sheet.html#raycaster

```
#Casts a ray from *origin*, in *direction*, with length *distance* and returns
#a HitInfo containing information about what it hit. This ray will only hit entities with a collider.

#Use optional *traverse_target* to only be able to hit a specific entity and its children/descendants.
#Use optional *ignore* list to ignore certain entities.
#Setting debug to True will draw the line on screen.

#Example where we only move if a wall is not hit:


class Player(Entity):

    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()  # get the direction we're trying to walk in.

        origin = self.world_position + (self.up*.5) # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
        hit_info = raycast(origin , self.direction, ignore=(self,), distance=.5, debug=False)
        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt

Player(model='cube', origin_y=-.5, color=color.orange)
wall_left = Entity(model='cube', collider='box', scale_y=3, origin_y=-.5, color=color.azure, x=-4)
wall_right = duplicate(wall_left, x=4)
camera.y = 2
```
''')

RuLe = """Watch this video:
<https://www.youtube.com/watch?v=VrskJbygL7k>"""