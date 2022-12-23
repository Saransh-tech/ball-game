from processing_py import *
p = App(400, 400)

y = p.height/2
speed = 3
while True:

    p.background(255)
    p.fill(0, 0, 255)
    p.ellipse(p.width/2, y, 60, 60)
    y = y + speed
    speed = speed + 0.2
    if y >= p.height:
        speed = speed * -1
    p.redraw()