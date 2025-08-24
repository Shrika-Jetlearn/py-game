import pgzrun 
import random
WIDTH=500
HEIGHT=500
cat=Actor("cat")
cat.x=250
cat.y=250
msg="catch the cat"
def draw():
    screen.fill("DarkOrchid3")
    cat.draw()
    screen.draw.text(msg,(50,50))
def on_mouse_down(pos):
    global msg
    if cat.collidepoint(pos):
       cat.x= random.randint(50,450)
       cat.y= random.randint(50,450)
       msg = "Good job!"
    else:
        msg = "oops!"

pgzrun.go()
 