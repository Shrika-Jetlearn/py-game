import pgzrun
import random

WIDTH = 500
HEIGHT = 500
cat=Actor("cat")
cat.x=250
cat.y=250
rat=Actor("rat")
rat.x=random.randint(50,450)
rat.y=random.randint(50,450)
score =0
game = True
def timeup():
    global game
    game = False
def draw():
    screen.blit("green background", (0,0))
    screen.draw.text(str(score),(20,20))
    cat.draw()
    rat.draw()
    if game == False:
        screen.fill("red")
        screen.draw.text(str(score),(20,20))
def update(): 
    global score
    if keyboard.w:
        cat.y -= 5
    if keyboard.s:
        cat.y += 5
    if keyboard.a:
        cat.x -= 5
    if keyboard.d:
        cat.x += 5  
    if cat.colliderect(rat):
        rat.x=random.randint(50,450)
        rat.y=random.randint(50,450)
        score += 1
clock.schedule(timeup,60)
pgzrun.go()