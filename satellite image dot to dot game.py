import pgzrun
import random

WIDTH=500
HEIGHT=500
total = 12
sats = []
lines = []
next_satellite = 0
for i in range(total):
    satellite=Actor("satellite")
    satellite.x=random.randint(50,450)
    satellite.y=random.randint(50,450)
    sats.append(satellite)
def draw():
    screen.blit("space background", (0,0))
    num=1
    for satellite in sats:
      satellite.draw()
      screen.draw.text( str(num),(satellite.x,satellite.y+20))
      num+=1 
    for line in lines:
       screen.draw.line(line[0],line[1], (255,255,255))
def on_mouse_down(pos):
   global next_satellite,lines
   if next_satellite < total:
      if sats [next_satellite].collidepoint(pos): 
         lines.append((sats[next_satellite-1].pos,sats [next_satellite].pos))
         next_satellite=next_satellite+1
         
pgzrun.go()