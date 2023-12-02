"""
Постройте первую дорогу из снега сверху до низу.
Возможно тут уже стоит ускорить врап.
"""

import wrap, random
wrap.world.create_world(610, 600)

for y in range(0,650,20):
    b = wrap.sprite.add("battle_city_items", 0, 30, "block_snow")
    wrap.sprite.set_size(b, 10, 20)
    wrap.sprite.move_left_to(b, 0 + 20)
    wrap.sprite.move_top_to(b, y)


for i in range(0,600, 70):
    b = wrap.sprite.add("battle_city_items",i,30,"block_brick")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b,i)

    b = wrap.sprite.add("battle_city_items", i, 30, "block_brick")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b, i+30)

    b = wrap.sprite.add("battle_city_items", i, 30, "block_bushes")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b, i + 50)


import wrap_py
wrap_py.app.start()