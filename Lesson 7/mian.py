import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = 'Satilite game'

satilite_num = 8
satilites = []
nxt_satilite = 0
lines = []

starttime = 0
totaltime = 0
endtime = 0


def start():
    global starttime
    for i in range(0,satilite_num):
        sat = Actor('sat')
        sat.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        satilites.append(sat)
    
    starttime = time()


def draw():
    global totaltime

    screen.blit('background',(0,0))

    num = 1

    for sat in satilites:
        sat.draw()
        screen.draw.text(str(num),(sat.pos[0],sat.pos[1]+20))
        num = num + 1
    
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,254))

    if nxt_satilite < satilite_num:
        totaltime = time() - starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize = 30)

    else:
       screen.draw.text(str(round(totaltime,1)),(10,10),fontsize = 30)

    if nxt_satilite == 8:
        screen.draw.text("Good Job",(300,300), fontsize = 55)

def update():
    pass
        
def on_mouse_down(pos):
    global nxt_satilite, lines
    if nxt_satilite < satilite_num:
        if satilites[nxt_satilite].collidepoint(pos):
            if nxt_satilite:
                lines.append((satilites[nxt_satilite-1].pos, satilites[nxt_satilite].pos))
            nxt_satilite= nxt_satilite + 1
        else:
            lines = []
            nxt_satilite = 0








start()
pgzrun.go()

