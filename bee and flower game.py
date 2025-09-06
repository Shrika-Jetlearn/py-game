import pgzrun
import random

WIDTH = 500
HEIGHT = 500
bee=Actor("bee")
bee.x=250
bee.y=250
flower=Actor("flower")
flower.x=random.randint(50,450)
flower.y=random.randint(50,450)
score =0
game = True
def timeup():
    global game
    game = False
def draw():
    screen.blit("green background", (0,0))
    screen.draw.text(str(score),(20,20))
    bee.draw()
    flower.draw()
    if game == False:
        screen.fill("red")
        screen.draw.text(str(score),(20,20))
def update(): 
    global score
    if keyboard.w:
        bee.y -= 5
    if keyboard.s:
        bee.y += 5
    if keyboard.a:
        bee.x -= 5
    if keyboard.d:
        bee.x += 5  
    if bee.colliderect(flower):
        flower.x=random.randint(50,450)
        flower.y=random.randint(50,450)
        score += 1
clock.schedule(timeup,60)
pgzrun.go()