"""поместите все номера спрайтов в список.
с помощью for поместите каждый спрайт в случайное место на экране,
используйте только левую сторону экрана
"""
import random

import wrap
wrap.world.create_world(600, 600)


a= wrap.sprite.add("battle_city_tanks", 100, 100, "tank_enemy_size1_green1")
b= wrap.sprite.add("mario-1-big", 100, 100, "duck")
c= wrap.sprite.add("pacman", 100, 100, "enemy_blue_down1")
d= wrap.sprite.add("mario-princess", 100, 100, "princess")
e= wrap.sprite.add("mario-enemies", 100, 100, "beetle_blue_go")

l = [a,b,c,d,e]

for s in l:
    wrap.sprite.move_to(s, random.randint(30, 300), random.randint(30, 570))


import wrap_py
wrap_py.app.start()