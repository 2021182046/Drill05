from pico2d import *
import random

open_canvas()
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')
mouse = load_image('hand_arrow.png')

while True:
    #clear_canvas()
    #tuk_ground.draw_now(800//2, 600//2)

    points = [ (random.randint(0, 800) , random.randint(0,600)) for i in range(10) ]
    for p in points:
        clear_canvas()
        tuk_ground.draw_now(800//2, 600//2)
        mouse.draw(p[0], p[1])
    update_canvas()
    delay(0.1)

