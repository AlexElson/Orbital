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
circle=pygame.image.load("Images\\circle.png").convert_alpha()
blue_sky=pygame.image.load("Images\\blue_sky.png").convert_alpha()

#Colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

#Landscape
size=38
maxdy=15
change=30
ddy=0; dy=0; y=100

rotation=0
landy=[]
for n in range(size):
    #landy.append(n); landy[n]=100
    ddy=random.randint(0,change)-change/2
    dy=dy+ddy
    if (dy<-maxdy): dy=-maxdy
    if (dy>maxdy): dy=maxdy
    y=y+dy
    if (y<100): y=100
    if (y>150): y=150
    landy.append(n); landy[n]=int(y)



def displayPlanet():
    w=WIDTH/2
    h=HEIGHT/2

    #Sky
    highesty=0
    for n in range(-1,size-1):
        if (landy[n]>highesty): highesty=landy[n]
    circlesize=pygame.transform.scale(blue_sky,(highesty*2+500,highesty*2+500))
    rect=circlesize.get_rect()
    screen.blit(circlesize,(w-rect[2]/2,h-rect[3]/2)) 

    for n in range(-1,size-1): #Collision Lines
        angle=((3.14*2)/size)*n+rotation
        angle2=((3.14*2)/size)*(n+1)+rotation
        pygame.draw.line(screen, WHITE,(w+landy[n]*sin(angle), h+landy[n]*cos(angle)), (w+landy[n+1]*sin(angle2), h+landy[n+1]*cos(angle2)))





mainloop=True
while mainloop:
    
    Clock.tick(fps)
    screen.fill(BLACK)

    displayPlanet() #Display Planet
    rotation=rotation-.002
    if (rotation>=3.14*2): rotation=0

    for event in pygame.event.get(): 
        if (event.type==QUIT): #Quitting
            mainloop=False

    pygame.display.set_caption("FPS: "+str(int(Clock.get_fps())))
    pygame.display.flip()
    
pygame.quit()
