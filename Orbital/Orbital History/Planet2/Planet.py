import pygame, sys
import time
import random
import math
from math import *
from pygame.locals import *
pygame.init()
fps=48

WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
Clock=pygame.time.Clock()

#Load Files
tileset=pygame.image.load("Images\\tileset.png").convert_alpha()

#Colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

#Landscape
size=20
landy=[]
for n in range(size):
    landy.append(n); landy[n]=100


def displayPlanet():
    for n in range(size-1):
        angle=((3.14*2)/size)*n
        angle2=((3.14*2)/size)*(n+1)
        w=WIDTH/2
        h=HEIGHT/2
        pygame.draw.line(screen, WHITE,(w+landy[n]*sin(angle), h+landy[n]*cos(angle)), (w+landy[n+1]*sin(angle2), h+landy[n+1]*cos(angle2)))
        screen.blit(tileset,(w+landy[n]*sin(angle),h+landy[n]*cos(angle)),(0,0,48,16)) 
    pygame.draw.line(screen, WHITE,(w+landy[0]*sin(0), h+landy[0]*cos(0)), (w+landy[size-1]*sin(angle2), h+landy[size-1]*cos(angle2)))
    #pygame.draw.line(screen, WHITE,(w,h),(w,h))







mainloop=True
while mainloop:
    
    Clock.tick(fps)
    screen.fill(BLACK)

    displayPlanet()

    for event in pygame.event.get(): 
        if (event.type==QUIT): #Quitting
            mainloop=False

    pygame.display.set_caption("FPS: "+str(int(Clock.get_fps())))
    pygame.display.flip()
    
pygame.quit()
