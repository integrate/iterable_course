"""
Сделайте между кирпичами пробелы размером 10 пикселей
"""

import wrap, random
wrap.world.create_world(600, 600)

for i in range(0,600, 30):
    b = wrap.sprite.add("battle_city_items",i,30,"block_brick")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b,i)
