import pgzrun
import random
from time import time 

start_time=0
total_time=0
end_time=0

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
start_time=time()

def draw():
    global total_time
    screen.blit("space background", (0,0))
    num=1
    for satellite in sats:
      satellite.draw()
      screen.draw.text( str(num),(satellite.x,satellite.y+20))
      num+=1 
    for line in lines:
       screen.draw.line(line[0],line[1], (255,255,255))
    if next_satellite < total:
       total_time = time()-start_time 
       total_time=round(total_time,2)
       screen.draw.text(str(total_time),(10,10))
    else:
       screen.draw.text(str(total_time),(10,10))
def on_mouse_down(pos):
   global next_satellite,lines
   if next_satellite < total:
      if sats [next_satellite].collidepoint(pos): 
         lines.append((sats[next_satellite-1].pos,sats [next_satellite].pos))
         next_satellite=next_satellite+1
         
pgzrun.go()