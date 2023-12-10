"""создайте на экране 5 спрайтов в одном и томже месте"""

import wrap
wrap.world.create_world(600, 600)


wrap.sprite.add("battle_city_tanks", 100, 100, "tank_enemy_size1_green1")
wrap.sprite.add("mario-1-big", 100, 100, "duck")
wrap.sprite.add("pacman", 100, 100, "enemy_blue_down1")
wrap.sprite.add("mario-princess", 100, 100, "princess")
wrap.sprite.add("mario-enemies", 100, 100, "beetle_blue_go")


import wrap_py
wrap_py.app.start()