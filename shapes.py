import pgzrun
import random
WIDTH = 500
HEIGHT = 500
def draw():
    screen.fill("black")
    w=400
    h=50
    for i in range(50):
        red=random.randint(0,255)
        blue=random.randint(0,255)
        green=random.randint(0,255)
        r= Rect((150,150),(w,h))
        r.center= 250,250
        screen.draw.rect(r,(red,blue,green))
        w-=10
        h+= 10
pgzrun.go()

