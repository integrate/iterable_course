"""
каждому спрайту установите случайную высоту и ширину
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
    wrap.sprite.set_size(s, random.randint(30,130), random.randint(30,130))
