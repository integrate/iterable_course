"""создайте на экране много огненных шариков вдоль верхней границы экрана"""

import wrap
wrap.world.create_world(600, 600)

for x in range(15, 600, 20):
    wrap.sprite.add("mario-enemies", x, 20, 'fire_ball')