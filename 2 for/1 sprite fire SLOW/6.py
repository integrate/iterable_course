"""
те шарики, которые достигли границы, продолжают двигаться вниз
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

ball_list = []

for s in l:
    y = random.randint(30, 300)
    wrap.sprite.move_to(s, random.randint(30, 300), y)
    wrap.sprite.set_size(s, random.randint(30,130), random.randint(30,130))
    ball = wrap.sprite.add("mario-enemies", 0, y, "fire_ball")
    wrap.sprite.move_left_to(ball, wrap.sprite.get_right(s))
    ball_list.append(ball)

while True:
    for b in ball_list:
        if wrap.sprite.get_right(b)>=600:
            wrap.sprite.move(b, 0,6)
        else:
            wrap.sprite.move(b, 8,0)
