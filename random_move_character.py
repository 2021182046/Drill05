from pico2d import *
import random

open_canvas()
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')
mouse = load_image('hand_arrow.png')
frame = 0

def draw_line(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    for i in range(0, 100+1, 5):
        t = i/100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

while True:
    #clear_canvas()
    #tuk_ground.draw_now(800//2, 600//2)

    points = [ (random.randint(0, 800) , random.randint(0,600)) for i in range(10) ]
    for p in points:
        clear_canvas()
        tuk_ground.draw_now(800//2, 600//2)
        mouse.draw(p[0], p[1])

    for i in range(0, len(points) - 1):
        draw_line(points[i], points[i + 1])

    update_canvas()
    delay(0.1)

