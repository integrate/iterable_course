"""
Сделайте между кирпичами пробелы размером 20 пикселей
"""

import wrap, random
wrap.world.create_world(600, 600)

for i in range(0,600, 40):
    b = wrap.sprite.add("battle_city_items",i,30,"block_brick")
    wrap.sprite.set_size(b, 20, 20)
    wrap.sprite.move_left_to(b,i)



import wrap_py
wrap_py.app.start()