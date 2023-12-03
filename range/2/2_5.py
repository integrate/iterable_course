"""
Ограничьте дорогу кирпичами с двух сторон.
Между дорогами посадите деревья размером 20 пикселей
"""

import wrap, random
wrap.world.create_world(610, 600)

for i in range(0,600, 70):
    b = wrap.sprite.add("battle_city_items",i,30,"block_brick")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b,i)

    b = wrap.sprite.add("battle_city_items",i,30,"block_snow")
    wrap.sprite.set_size(b, 10, 20)
    wrap.sprite.move_left_to(b,i+20)

    b = wrap.sprite.add("battle_city_items", i, 30, "block_brick")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b, i+30)

    b = wrap.sprite.add("battle_city_items", i, 30, "block_bushes")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b, i + 50)



import wrap_py
wrap_py.app.start()