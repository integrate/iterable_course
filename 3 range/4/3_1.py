"Строим землю, потом строим лестницу перехода в след уровень, потом располагаем облака, потом замок"
import random

import wrap

wrap.world.create_world(600, 600)
wrap.world.set_back_color(98,150,249)

for x in range(32, 600, 128):
    wrap.sprite.add("mario-scenery", x, random.randint(16,200), "cloud1")

for y in range(560, 600, 32):
    for x in range(16, 600, 32):
        wrap.sprite.add("mario-scenery", x, y,"ground")

for y in range(0,8):
    for x in range(0,9-y):
        wrap.sprite.add("mario-scenery", x*32+16+y*32, 528-y*32, "block")




for y in range(528,0,-32):
    wrap.sprite.add("mario-items", 400, y, "vine2")


for x in range(0, 6):
    wrap.sprite.add("mario-items", 300-24-x*48, 250-x*30, "moving_platform1")

wrap.sprite.add("mario-princess", 500, 520, "princess")

wrap.sprite.add("mario-1-big", 390, 200, "climb1")

m = wrap.sprite.add("mario-2-big", 410, 350, "climb2")
wrap.sprite.set_reverse_x(m,True)


m = wrap.sprite.add("mario-3-big", 190, 100, "jump")
wrap.sprite.set_reverse_x(m,True)

wrap.sprite.add("mario-items", 35, 80, "flower1")

import wrap_py
wrap_py.app.start()