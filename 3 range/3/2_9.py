"""
Сделайте кирпичные ограждения и деревья шириной 15 пикселей. А дорогу 30 пикселей шириной
"""

import wrap, random
wrap.world.create_world(610, 600)


for i in range(0,600, 75):
    for y in range(0, 650, 20):
        b = wrap.sprite.add("battle_city_items",i,30,"block_brick")
        wrap.sprite.set_size(b, 15, 20)
        wrap.sprite.move_left_to(b,i)
        wrap.sprite.move_top_to(b, y)

        b = wrap.sprite.add("battle_city_items", 0, 30, "block_snow")
        wrap.sprite.set_size(b, 30, 20)
        wrap.sprite.move_left_to(b, i+15)
        wrap.sprite.move_top_to(b, y)

        b = wrap.sprite.add("battle_city_items", i, 30, "block_brick")
        wrap.sprite.set_size(b, 15, 20)
        wrap.sprite.move_left_to(b, i+45)
        wrap.sprite.move_top_to(b, y)

        b = wrap.sprite.add("battle_city_items", i, 30, "block_bushes")
        wrap.sprite.set_size(b, 15, 20)
        wrap.sprite.move_left_to(b, i + 60)
        wrap.sprite.move_top_to(b, y)


import wrap_py
wrap_py.app.start()