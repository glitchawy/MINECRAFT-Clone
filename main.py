from ursina import *
from ursina import mouse
from ursina.prefabs.first_person_controller import FirstPersonController

app= Ursina()
grass_tex=load_texture('assets/grass_block.png')
stone_tex = load_texture('assets/stone_block.png')
beick_tex = load_texture('assets/brick_block.png')
dirt_tex = load_texture('assets/dirt_block.png')
sky_tex = load_texture("assets/skybox.png")
arm_tex = load_texture("assets/arm_texture.png")
block_pick=1
def update():
    global block_pick
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1'] : block_pick = 1
    if held_keys['2'] : block_pick = 2
    if held_keys['3'] : block_pick = 3
    if held_keys['4'] : block_pick = 4


class voxel(Button):
    def __init__(self,position=(0,0,0) , texture= grass_tex):
        super().__init__(
            parent =scene ,
            position=position,
            model="assets/block",
            origin_y = 0.5,
            texture= texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                if block_pick==1: hehe = voxel(position=self.position + mouse.normal,texture=grass_tex)
                if block_pick==2: hehe = voxel(position=self.position + mouse.normal,texture=stone_tex)
                if block_pick==3: hehe = voxel(position=self.position + mouse.normal,texture=beick_tex)
                if block_pick==4: hehe = voxel(position=self.position + mouse.normal,texture=dirt_tex)

            if key == "right mouse down":
               destroy(self)

class sky(Entity):
    def __init__(self):
        super().__init__(
            parent= scene ,
            model= "sphere",
            texture = sky_tex,
            scale = 150,
            double_sided = True
        )


class hands(Entity):
    def __init__(self):
        super().__init__(
           parent= camera.ui,
            model= "assets/arm",
            texture=arm_tex,
            scale=0.2,
            rotation= Vec3(150,-10,0),
            position = Vec2(0.4 , -0.6))

    def active(self):
        position = Vec2(0.1, -0.8)

    def passive(self):
        position = Vec2(0.4 , -0.6)



for z in range(30):
    for x in range(30):
        hehe = voxel(position=(x, 0, z))

glitch= FirstPersonController()
sky= sky()
hand= hands()
app .run()
