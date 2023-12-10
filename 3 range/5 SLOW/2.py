"""на каждом шарике напишите его порядковый номер, начиная с 1"""

import wrap
wrap.world.create_world(600, 600)

balls = []
texts = []

n=1
for x in range(15, 600, 35):
    b=wrap.sprite.add("mario-enemies", x, 20, 'fire_ball')
    wrap.sprite.set_size(b, 30, 30)
    balls.append(b)

    t=wrap.sprite.add_text(str(n), x, 20, text_color=[0,0,255], bold=True)
    texts.append(t)
    n+=1

while True:
    for n in range(len(balls)):
        wrap.sprite.move(balls[n],0, 5)
        wrap.sprite.move(texts[n],0, 5)