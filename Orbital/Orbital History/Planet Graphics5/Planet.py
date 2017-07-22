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
ground1=pygame.image.load("Images\\ground1.png").convert_alpha()
ground2=pygame.image.load("Images\\ground2.png").convert_alpha()
circle=pygame.image.load("Images\\circle.png").convert_alpha()
blue_sky=pygame.image.load("Images\\blue_sky.png").convert_alpha()

#Colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
ORANGE=(234,94,0)

#Landscape
size=38
rotation=0
landy=random.randint(50,200)
if (landy>100): landy=random.randint(150,190)
tile=[]
for n in range(size):
    tile.append(n)
    tile[n]=random.randint(0,1)
w=400
h=400

#Rocketship
rx=0; ry=0
rs=20 #rocket size
rrot=0 #rocket rotation
rw=1 #rocket width
rd=0 #holding d or not
ra=0 #holding a or not
engine=0 #holding w or not (engine on or not)
dx=0 #x rocket movement
dy=0 #y rocket movement




def displaySky():
    global w,h
    #Sky
    circlesize=pygame.transform.scale(blue_sky,(landy*2+500,landy*2+500))
    rect=circlesize.get_rect()
    screen.blit(circlesize,(w-rect[2]/2-rx+WIDTH/2,h-rect[3]/2-ry+HEIGHT/2))    

    #Center Dark Circle
    circlesize=pygame.transform.scale(circle,(landy*2,landy*2))
    rect=circlesize.get_rect()
    screen.blit(circlesize,(w-rect[2]/2-rx+WIDTH/2,h-rect[3]/2-ry+HEIGHT/2))

def displayPlanet():
    global rotation
    global w,h
    for n in range(-1,size-1):
        angle=((3.14*2)/size)*n+rotation
        angle2=((3.14*2)/size)*(n+1)+rotation
        #Display Ground
        if (landy<=100): ground=ground1
        if (landy>100): ground=ground2
        oldCenter=ground.get_size()
        groundRot=pygame.transform.rotate(ground,angle*57.3)
        rect=groundRot.get_rect()
        rect.center=oldCenter
        screen.blit(groundRot,(w+landy*sin(angle)+rect[0]-oldCenter[0]-rx+WIDTH/2,h+landy*cos(angle)+rect[1]-oldCenter[1]-ry+HEIGHT/2))
        
    for n in range(-1,size-1): #Collision Lines
        angle=((3.14*2)/size)*n+rotation
        angle2=((3.14*2)/size)*(n+1)+rotation
        pygame.draw.line(screen, WHITE,(w+landy*sin(angle)-rx+WIDTH/2, h+landy*cos(angle)-ry+HEIGHT/2), (w+landy*sin(angle2)-rx+WIDTH/2, h+landy*cos(angle2)-ry+HEIGHT/2))

    rotation=rotation-.002 #Rotate Planet
    if (rotation>=3.14*2): rotation=0

def displayRocketship():
    pygame.draw.line(screen, WHITE, (WIDTH/2+rs*cos(rrot-3.14/2),HEIGHT/2+rs*sin(rrot-3.14/2)), (WIDTH/2+rs*cos(rrot+rw),HEIGHT/2+rs*sin(rrot+rw)))
    pygame.draw.line(screen, WHITE, (WIDTH/2+rs*cos(rrot-3.14/2),HEIGHT/2+rs*sin(rrot-3.14/2)), (WIDTH/2+rs*cos(rrot-3.14-rw),HEIGHT/2+rs*sin(rrot-3.14-rw)))
    pygame.draw.line(screen, WHITE, (WIDTH/2+rs*cos(rrot+rw),HEIGHT/2+rs*sin(rrot+rw)), (WIDTH/2+rs*cos(rrot-3.14-rw),HEIGHT/2+rs*sin(rrot-3.14-rw)))
    if (engine==1):
        pygame.draw.line(screen, ORANGE, (WIDTH/2+rs*2*cos(rrot+3.14/2),HEIGHT/2+rs*2*sin(rrot+3.14/2)), (WIDTH/2+rs*.9*cos(rrot+rw*1.2),HEIGHT/2+rs*.9*sin(rrot+rw*1.2)))
        pygame.draw.line(screen, ORANGE, (WIDTH/2+rs*2*cos(rrot+3.14/2),HEIGHT/2+rs*2*sin(rrot+3.14/2)), (WIDTH/2+rs*.9*cos(rrot-3.14-rw*1.2),HEIGHT/2+rs*.9*sin(rrot-3.14-rw*1.2)))
        pygame.draw.line(screen, ORANGE, (WIDTH/2+rs*.9*cos(rrot+rw*1.2),HEIGHT/2+rs*.9*sin(rrot+rw*1.2)), (WIDTH/2+rs*.9*cos(rrot-3.14-rw*1.2),HEIGHT/2+rs*.9*sin(rrot-3.14-rw*1.2)))       

def controlRocketship():
    global rrot
    global dy,dx
    global rx,ry
    if (rd==1): rrot=rrot+0.03 #Rotating
    if (ra==1): rrot=rrot-0.03
    if (rrot>=3.14*2 or rrot<=-3.14*2): rrot=0

    a=w-rx #Gravity
    b=h-ry
    c=(a*a+b*b)**.5
    if (c<landy+250):
        d=atan(b/a)
        aa=cos(d)*2
        bb=sin(d)*2
        if (a>0):
            rx=rx+aa
            ry=ry+bb
        if (a<0):
            rx=rx-aa
            ry=ry-bb
        if (dx>0): dx=dx-.03
        if (dx<0): dx=dx+.03
        if (dy>0): dy=dy-.03
        if (dy<0): dy=dy+.03
        
        #aa=a/abs(a); bb=b/abs(b)
        #dx=dx+(aa*(landy+250)-a)/15000
        #dy=dy+(bb*(landy+250)-b)/15000

    #Planet Collision
    if (c<landy+18): dx=0; dy=0
    
    if (engine==1): #Movement
        dy=dy-sin(rrot+3.14/2)*0.05
        dx=dx-cos(rrot+3.14/2)*0.05
        if (dy>5): dy=dy-0.05
        if (dy<-5): dy=dy+0.05
    rx=rx+dx
    ry=ry+dy

    



mainloop=True
while mainloop:
    
    Clock.tick(fps)
    screen.fill(BLACK)

    controlRocketship() #Control Rocketship

    displaySky() #Display Sky and Center
    displayRocketship() #Display Rocketship
    displayPlanet() #Display Planet

    for event in pygame.event.get():
        
        if (event.type==KEYDOWN): #Press Keys
            if (event.key==pygame.K_d): rd=1
            if (event.key==pygame.K_a): ra=1
            if (event.key==pygame.K_w): engine=1
        elif (event.type==KEYUP):
            if (event.key==pygame.K_d): rd=0
            if (event.key==pygame.K_a): ra=0
            if (event.key==pygame.K_w): engine=0

        elif (event.type==QUIT): #Quitting
            mainloop=False

    pygame.display.set_caption("FPS: "+str(int(Clock.get_fps()))+" ")
    pygame.display.flip()
    
pygame.quit()
