import wrap

wrap.world.create_world(600, 600)
wrap.world.set_back_color(98,150,249)

for x in range(16,600, 32):
    wrap.sprite.add("mario-enemies", x, 550, "cloud")

for x in range(16,600, 32):
    if x>100 and x<200:
        continue
    wrap.sprite.add("mario-items", x, 200, "coin")

for y in range(50,400, 32):
    wrap.sprite.add("mario-items", 150, y, "block_bricks")


wrap.sprite.add("mario-1-big", 300, 250, "jump")
wrap.sprite.add("mario-items", 300, 350, "cloud_platform")

import wrap_py
wrap_py.app.start()