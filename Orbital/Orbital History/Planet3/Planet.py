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
ground=pygame.image.load("Images\\ground.png").convert_alpha()
circle=pygame.image.load("Images\\circle.png").convert_alpha()
blue_sky=pygame.image.load("Images\\blue_sky.png").convert_alpha()

#Colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)

#Landscape
size=38
landy=[]
for n in range(size):
    landy.append(n); landy[n]=100




def displayPlanet():
    w=WIDTH/2
    h=HEIGHT/2

    #Sky
    circlesize=pygame.transform.scale(blue_sky,(landy[0]*5,landy[0]*5))
    rect=circlesize.get_rect()
    screen.blit(circlesize,(w-rect[2]/2,h-rect[3]/2))    

    #Center Dark Circle
    circlesize=pygame.transform.scale(circle,(landy[0]*2,landy[0]*2))
    rect=circlesize.get_rect()
    screen.blit(circlesize,(w-rect[2]/2,h-rect[3]/2))
    
    for n in range(-1,size-1):
        angle=((3.14*2)/size)*n
        angle2=((3.14*2)/size)*(n+1)

        #Display Ground
        oldCenter=ground.get_size()
        groundRot=pygame.transform.rotate(ground,angle*57.3)
        rect=groundRot.get_rect()
        rect.center=oldCenter
        screen.blit(groundRot,(w+landy[n]*sin(angle)+rect[0]-oldCenter[0],h+landy[n]*cos(angle)+rect[1]-oldCenter[1]))

    #for n in range(-1,size-1):
        #angle=((3.14*2)/size)*n
        #angle2=((3.14*2)/size)*(n+1)
        #Collision Lines
        #pygame.draw.line(screen, WHITE,(w+landy[n]*sin(angle), h+landy[n]*cos(angle)), (w+landy[n+1]*sin(angle2), h+landy[n+1]*cos(angle2)))





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
