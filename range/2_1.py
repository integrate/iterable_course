"""
Постройте линию из кирпичей.
Кирпичи должны начинаться четко с начала экрана.
Каждый кирпич должен быть размером 20*20 пикселей.
"""

import wrap, random
wrap.world.create_world(600, 600)

for i in range(0,600, 20):
    b = wrap.sprite.add("battle_city_items",i,30,"block_brick")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b,i)