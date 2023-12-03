"""
Постройте все дороги из снега сверху до низу.
"""

import wrap, random
wrap.world.create_world(610, 600)


for i in range(0,600, 70):
    for y in range(0, 650, 20):
        b = wrap.sprite.add("battle_city_items",i,30,"block_brick")
        wrap.sprite.set_size(b, 20, 20)
        wrap.sprite.move_left_to(b,i)
        wrap.sprite.move_top_to(b, y)


        b = wrap.sprite.add("battle_city_items", 0, 30, "block_snow")
        wrap.sprite.set_size(b, 10, 20)
        wrap.sprite.move_left_to(b, i+20)
        wrap.sprite.move_top_to(b, y)

        b = wrap.sprite.add("battle_city_items", i, 30, "block_brick")
        wrap.sprite.set_size(b, 20, 20)
        wrap.sprite.move_left_to(b, i+30)
        wrap.sprite.move_top_to(b, y)

        b = wrap.sprite.add("battle_city_items", i, 30, "block_bushes")
        wrap.sprite.set_size(b, 20, 20)
        wrap.sprite.move_left_to(b, i + 50)
        wrap.sprite.move_top_to(b, y)


import wrap_py
wrap_py.app.start()