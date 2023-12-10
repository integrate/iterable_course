"""
Создать на экране в случайных местах 10 маленьких танков, 20, 150
Попробовать создавать разноцветные танки, используя в коде только одну команду add
"""
import wrap, random

screen=wrap.world.create_world(700, 700)

for i in range(0,150):
    color = random.choice(["green", "purple","white","yellow"])
    t = wrap.sprite.add("battle_city_tanks",random.randint(10,650), random.randint(10,650), "tank_enemy_size1_"+color+"1")

import wrap_py
wrap_py.app.start()