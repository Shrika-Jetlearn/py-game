import pgzrun
import random

WIDTH = 500
HEIGHT = 500
maomao=Actor("maomao")
maomao.x=250
maomao.y=250
bottleofpoison=Actor("bottle of poison")
bottleofpoison.x=random.randint(50,450)
bottleofpoison.y=random.randint(50,450)
score =0
game = True
def timeup():
    global game
    game = False
def draw():
    screen.blit("green background", (0,0))
    screen.draw.text(str(score),(20,20))
    maomao.draw()
    bottleofpoison.draw()
    if game == False:
        screen.fill("red")
        screen.draw.text(str(score),(20,20))
def update(): 
    global score
    if keyboard.w:
        maomao.y -= 5
    if keyboard.s:
        maomao.y += 5
    if keyboard.a:
        maomao.x -= 5
    if keyboard.d:
        maomao.x += 5  
    if maomao.colliderect(bottleofpoison):
        bottleofpoison.x=random.randint(50,450)
        bottleofpoison.y=random.randint(50,450)
        score += 1
clock.schedule(timeup,60)
pgzrun.go()