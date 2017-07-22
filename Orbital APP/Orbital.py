import pygame, sys, os
import time
import random
import math
from math import *
from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
fps=48

WIDTH=int(800)
HEIGHT=int(600)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
Clock=pygame.time.Clock()

#Load Files
ground1=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/ground1.png")).convert_alpha()
ground2=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/ground2.png")).convert_alpha()
hot1=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/hot1.png")).convert_alpha()
hot2=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/hot2.png")).convert_alpha()
cold1=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/cold1.png")).convert_alpha()
cold2=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/cold2.png")).convert_alpha()
circle=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/circle.png")).convert_alpha()
blue_sky=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/blue_sky.png")).convert_alpha()
blue_sky2=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/blue_sky2.png")).convert_alpha()
sunlight=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/sunlight.png")).convert()
background=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/background.png")).convert_alpha()
arrow=pygame.image.load(os.path.abspath("/Volumes/Orbital/Images/arrow.png")).convert_alpha()
thrusters=pygame.mixer.Sound(os.path.abspath("/Volumes/Orbital/Images/thrusters.wav"))
thrusters.set_volume(.25)


#Colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
ORANGE=(234,94,0)

#Landscape
size=38
rotation=[]
landy=[]
w=[]
h=[]
spin=[]
way=random.randint(0,2)
for n in range(10):
    w.append(n); h.append(n)
w[0]=-100; h[0]=0
for n in range(10):
    if (n>=1):
        if (way==0):
            w[n]=w[n-1]+random.randint(1000,2500)
            h[n]=h[n-1]+random.randint(-800,800)
        if (way==1):
            w[n]=w[n-1]+random.randint(0,500)
            h[n]=h[n-1]+random.randint(1000,2500)
        if (way==2):
            w[n]=w[n-1]+random.randint(0,500)
            h[n]=h[n-1]-random.randint(1000,2500)
    spin.append(n); spin[n]=random.randint(-300,300)/100000.00
    if (abs(spin[n])<50): spin[n]=spin[n]*2.00
    
    rotation.append(n); rotation[n]=0.00
    landy.append(n); landy[n]=random.randint(50,200)
    if (landy[n]>100): landy[n]=random.randint(150,190)

def create():
    global size,rotation,landy,w,h,spin,way
    size=38
    rotation=[]
    landy=[]
    w=[]
    h=[]
    spin=[]
    way=random.randint(0,2)
    for n in range(10):
        w.append(n); h.append(n)
    w[0]=-100; h[0]=0
    for n in range(10):
        if (n>=1):
            if (way==0):
                w[n]=w[n-1]+random.randint(1000,2500)
                h[n]=h[n-1]+random.randint(-800,800)
            if (way==1):
                w[n]=w[n-1]+random.randint(0,500)
                h[n]=h[n-1]+random.randint(1000,2500)
            if (way==2):
                w[n]=w[n-1]+random.randint(0,500)
                h[n]=h[n-1]-random.randint(1000,2500)
        spin.append(n); spin[n]=random.randint(-300,300)/100000.00
        if (abs(spin[n])<50): spin[n]=spin[n]*2.0
        
        rotation.append(n); rotation[n]=0
        landy.append(n); landy[n]=random.randint(50,200)
        if (landy[n]>100): landy[n]=random.randint(150,190)   
    

#Rocketship
rx=w[2]-1; ry=h[2]-10 #x and y coordinates
rs=20 #rocket size
rrot=0.00 #rocket rotation
rw=1 #rocket width
rd=0 #holding d or not
ra=0 #holding a or not
engine=0 #holding w or not (engine on or not)
dx=0.0 #x rocket movement
dy=0.0 #y rocket movement
landed=1 #if landed on planet
crashed=0 #if crashed
gravpull=1.00 #pulled in to planet
finish=random.randint(1,9) #land on winning planet
if (finish<=2): finish=finish-1
won=0.0
thrust=0.0


explodex=[] #crash particles
explodey=[]
explodedx=[]
explodedy=[]
for n in range(30):
    explodex.append(n); explodex[n]=WIDTH/2.00
    explodey.append(n); explodey[n]=HEIGHT/2.00
    explodedx.append(n); explodedx[n]=random.randint(-80,80)/100.00
    explodedy.append(n); explodedy[n]=random.randint(-80,80)/100.00
    
def setup():
    global rx,ry,rs,rrot,rw,rd,ra,engine,dx,dy,landed,crashed,gravpull,finish,explodex,explodey,explodedx,explodedy,won
    rx=w[2]-1; ry=h[2]-10 #x and y coordinates
    rs=20 #rocket size
    rrot=0.00 #rocket rotation
    rw=1 #rocket width
    rd=0 #holding d or not
    ra=0 #holding a or not
    engine=0 #holding w or not (engine on or not)
    dx=0.0 #x rocket movement
    dy=0.0 #y rocket movement
    landed=1 #if landed on planet
    crashed=0 #if crashed
    gravpull=1.00 #pulled in to planet
    finish=random.randint(1,9) #land on winning planet
    if (finish<=2): finish=finish-1
    won=0.0
    thrust=0.0

    explodex=[] #crash particles
    explodey=[]
    explodedx=[]
    explodedy=[]
    for n in range(30):
        explodex.append(n); explodex[n]=WIDTH/2.00
        explodey.append(n); explodey[n]=HEIGHT/2.00
        explodedx.append(n); explodedx[n]=random.randint(-80,80)/100.00
        explodedy.append(n); explodedy[n]=random.randint(-80,80)/100.00



def displaySky():
    global w,h

    #Background Stars
    backgroundsize=pygame.transform.scale(background, (WIDTH,HEIGHT))
    screen.blit(backgroundsize,(0-rx/25.00,0-ry/25.00))
    screen.blit(backgroundsize,(WIDTH/2-rx/25.00,0-ry/25.00))
    screen.blit(backgroundsize,(-WIDTH/2-rx/25.00,0-ry/25.00))
    screen.blit(backgroundsize,(0-rx/25.00,HEIGHT/2-ry/25.00))
    screen.blit(backgroundsize,(0-rx/25.00,-HEIGHT/2-ry/25.00))

    for n in range(10):
        if (w[n]>rx-WIDTH*2 and w[n]<rx+WIDTH*2 and h[n]>ry-HEIGHT*2 and h[n]<ry+HEIGHT*2):
            #Sky
            circlesize=pygame.transform.scale(blue_sky,(landy[n]*2+500+100,landy[n]*2+500+100))
            if (n<=1): circlesize=pygame.transform.scale(blue_sky2,(landy[n]*2+500+100,landy[n]*2+500+100))
            if (n>=4): circlesize=pygame.transform.scale(blue_sky2,(landy[n]*2+500+100,landy[n]*2+500+100))
            rect=circlesize.get_rect()
            screen.blit(circlesize,(w[n]-rect[2]/2.0-rx+WIDTH/2.0,h[n]-rect[3]/2.0-ry+HEIGHT/2.0))    

            #Center Dark Circle
            circlesize=pygame.transform.scale(circle,(landy[n]*2,landy[n]*2))
            rect=circlesize.get_rect()
            screen.blit(circlesize,(w[n]-rect[2]/2.0-rx+WIDTH/2.0,h[n]-rect[3]/2.0-ry+HEIGHT/2.0))

def displaySun():
    global crashed, won
    a=-1000-rx; a=-a
    if (a<255*4):
        sunlight.set_alpha((255*4-a)/4.0)
        screen.blit(sunlight,(0,0))
    if (a<0 and crashed==0): crashed=1

    #Arrow to Destination
    aaa=rx-w[finish]; bbb=ry-h[finish]; ccc=(aaa*aaa+bbb*bbb)**.5
    if (ccc>500): 
        ddd=atan(bbb/aaa)
        point=arrow
        oldCenter=point.get_size()
        if (aaa<0): dddd=atan(bbb/-aaa)-3.14/2.0
        if (aaa>=0): dddd=atan(-bbb/aaa)+3.14/2.0
        point=pygame.transform.rotate(point,dddd*57.3)
        rect=point.get_rect()
        rect.center=oldCenter
        if (aaa<0): screen.blit(point,(WIDTH/2+cos(ddd)*200+rect[0],HEIGHT/2+sin(ddd)*200+rect[1]))
        if (aaa>=0): screen.blit(point,(WIDTH/2-cos(ddd)*200+rect[0],HEIGHT/2-sin(ddd)*200+rect[1]))
        
        myfont = pygame.font.Font(None, 20)
        text = myfont.render(str(int(ccc/10.0)), 0, WHITE)
        if (aaa<0): screen.blit(text,(WIDTH/2+cos(ddd)*200+rect[0]+40,HEIGHT/2+sin(ddd)*200+rect[1]))
        if (aaa>=0): screen.blit(text,(WIDTH/2-cos(ddd)*200+rect[0]+40,HEIGHT/2-sin(ddd)*200+rect[1]))
        
    if (ccc<landy[finish]+50 and landed==1): won=1
    if (won==1):
        myfont = pygame.font.Font(None, 20)
        text = myfont.render("You Landed and Won!", 0, WHITE)
        screen.blit(text,(WIDTH/2-80,HEIGHT/2-50))
    

def displayPlanet():
    global rotation
    global w,h

    for nn in range(10):
        if (w[nn]>rx-WIDTH*2 and w[nn]<rx+WIDTH*2 and h[nn]>ry-HEIGHT*2 and h[nn]<ry+HEIGHT*2):
            for n in range(-1,size-1):
                angle=((3.14*2.0)/size)*n+rotation[nn]
                angle2=((3.14*2.0)/size)*(n+1)+rotation[nn]
                #Display Ground
                if (nn<=1):
                    if (landy[nn]<=100): ground=hot1
                    if (landy[nn]>100): ground=hot2
                if (nn>=2):
                    if (landy[nn]<=100): ground=ground1
                    if (landy[nn]>100): ground=ground2
                if (nn>=4):
                    if (landy[nn]<=100): ground=cold1
                    if (landy[nn]>100): ground=cold2
                oldCenter=ground.get_size()
                groundRot=pygame.transform.rotate(ground,angle*57.3)
                rect=groundRot.get_rect()
                rect.center=oldCenter
                screen.blit(groundRot,(w[nn]+landy[nn]*sin(angle)+rect[0]-oldCenter[0]-rx+WIDTH/2,h[nn]+landy[nn]*cos(angle)+rect[1]-oldCenter[1]-ry+HEIGHT/2))
              
        rotation[nn]=rotation[nn]+spin[nn] #Rotate Planet
        if (rotation[nn]>=3.14*2): rotation[nn]=0

def displayRocketship():
    pygame.draw.line(screen, WHITE, (WIDTH/2+rs*cos(rrot-3.14/2),HEIGHT/2+rs*sin(rrot-3.14/2)), (WIDTH/2+rs*cos(rrot+rw),HEIGHT/2+rs*sin(rrot+rw)))
    pygame.draw.line(screen, WHITE, (WIDTH/2+rs*cos(rrot-3.14/2),HEIGHT/2+rs*sin(rrot-3.14/2)), (WIDTH/2+rs*cos(rrot-3.14-rw),HEIGHT/2+rs*sin(rrot-3.14-rw)))
    pygame.draw.line(screen, WHITE, (WIDTH/2+rs*cos(rrot+rw),HEIGHT/2+rs*sin(rrot+rw)), (WIDTH/2+rs*cos(rrot-3.14-rw),HEIGHT/2+rs*sin(rrot-3.14-rw)))
    if (engine==1):
        pygame.draw.line(screen, ORANGE, (WIDTH/2+rs*2*cos(rrot+3.14/2),HEIGHT/2+rs*2*sin(rrot+3.14/2)), (WIDTH/2+rs*.9*cos(rrot+rw*1.2),HEIGHT/2+rs*.9*sin(rrot+rw*1.2)))
        pygame.draw.line(screen, ORANGE, (WIDTH/2+rs*2*cos(rrot+3.14/2),HEIGHT/2+rs*2*sin(rrot+3.14/2)), (WIDTH/2+rs*.9*cos(rrot-3.14-rw*1.2),HEIGHT/2+rs*.9*sin(rrot-3.14-rw*1.2)))
        pygame.draw.line(screen, ORANGE, (WIDTH/2+rs*.9*cos(rrot+rw*1.2),HEIGHT/2+rs*.9*sin(rrot+rw*1.2)), (WIDTH/2+rs*.9*cos(rrot-3.14-rw*1.2),HEIGHT/2+rs*.9*sin(rrot-3.14-rw*1.2)))       

def crashedRocketship():
    for n in range(30):
        if (explodex[n]==WIDTH/2): explodex[n]=WIDTH/2+explodedx[n]
        if (explodey[n]==HEIGHT/2): explodey[n]=HEIGHT/2+explodedy[n]
        explodex[n]=explodex[n]+explodedx[n]
        explodey[n]=explodey[n]+explodedy[n]
        explodedx[n]=explodedx[n]*.995
        explodedy[n]=explodedy[n]*.995
        pygame.draw.line(screen, WHITE, (explodex[n],explodey[n]), (explodex[n]+explodedx[n]*25,explodey[n]+explodedy[n]*25))

def controlRocketship():
    global rrot
    global dy,dx
    global rx,ry
    global landed, crashed, gravpull

    if (landed==0): #Rotating
        if (rd==1): rrot=rrot+0.04
        if (ra==1): rrot=rrot-0.04
    if (rrot>=3.14 or rrot<=-3.14): rrot=-rrot
    if (rrot>3.14): rrot=3.1
    if (rrot<-3.14): rrot=-3.1
    if (engine==1): #Movement
        dy=dy-sin(rrot+3.14/2.0)*0.06
        dx=dx-cos(rrot+3.14/2.0)*0.06
        if (dy>5): dy=dy-0.06
        if (dy<-5): dy=dy+0.06

    for n in range(10):
        if (w[n]>rx-WIDTH and w[n]<rx+WIDTH and h[n]>ry-HEIGHT and h[n]<ry+HEIGHT):
            a=w[n]-rx #Gravity
            b=h[n]-ry
            c=(a*a+b*b)**.5
            if (c>landy[n]+250):
                if (gravpull>0): gravpull=gravpull-0.01
            if (c<landy[n]+500 and c>=landy[n]+250):
                d=atan(b/a); aa=cos(d)*.3; bb=sin(d)*.3
                if (c<landy[n]+350): d=atan(b/a); aa=cos(d)*.7; bb=sin(d)*.7
                if (a>0): dx=dx+aa/30; dy=dy+bb/30
                if (a<0): dx=dx-aa/30; dy=dy-bb/30
            if (c<landy[n]+250):
                d=atan(b/a); aa=cos(d)*1.3; bb=sin(d)*1.3
                if (a>0): dx=dx+aa/30; dy=dy+bb/30
                if (a<0): dx=dx-aa/30; dy=dy-bb/30
                if (dx>0): dx=dx-.01
                if (dx<0): dx=dx+.01
                if (dy>0): dy=dy-.01
                if (dy<0): dy=dy+.01
                if (gravpull<1): gravpull=gravpull+0.01
                rrot=rrot-spin[n]
            if (c<landy[n]+500): 
                d=d-spin[n]*gravpull
                if (a<0): rx=w[n]+cos(d)*c; ry=h[n]+sin(d)*c
                if (a>=0): rx=w[n]-cos(d)*c; ry=h[n]-sin(d)*c
                
            #Planet Collision
            if (c<landy[n]+38): #Crashes
                d=atan(b/a)
                d=d-spin[n]
                ang=abs(rrot-d)
                if (ang>3.14): ang=ang-3.14
                if (abs(dx)+abs(dy)>4 or ang<1.57-.8 or ang>1.57+.8): crashed=1
                if (abs(dx)+abs(dy)>.7): dx=-dx; dy=-dy
                
                if (abs(dx)+abs(dy)<=.7):
                    if ((c<landy[n]+38) and (engine==0 or landed==0)): #Landed
                        landed=1
                        dx=0; dy=0
                        if (a>=0):
                            if (ang<1.57-.05): rrot=rrot-.03
                            if (ang>1.57+.05): rrot=rrot+.03
                        if (a<0):
                            if (ang<1.57-.05): rrot=rrot+.03
                            if (ang>1.57+.05): rrot=rrot-.03
                        if (a<0): rx=w[n]+cos(d)*(landy[n]+18+20); ry=h[n]+sin(d)*(landy[n]+18+20)
                        if (a>=0): rx=w[n]-cos(d)*(landy[n]+18+20); ry=h[n]-sin(d)*(landy[n]+18+20)     
            if (c>landy[n]+38): landed=0

    rx=rx+dx
    ry=ry+dy    

def sounds():
    global engine,thrust
    if (won==1): engine=0
    if (engine==1 and won==0 and crashed==0):
        if (thrust==0): thrusters.play(-1); thrust=1
    if (engine==0 or won==1 or crashed==1):
        if (thrust==1): thrusters.fadeout(500); thrust=0











mainloop=True 
while mainloop:
    
    Clock.tick(fps)
    screen.fill(BLACK)

    if (crashed==0): controlRocketship() #Control Rocketship
    displaySky() #Display Sky and Center
    if (crashed==0): displayRocketship() #Display Rocketship
    displayPlanet() #Display Planet
    displaySun() #Display Sun and Arrow
    if (crashed==1): crashedRocketship() #Crashed Rocketship
    sounds() #Play Sounds

    for event in pygame.event.get():
        
        if (event.type==KEYDOWN and won==0 and crashed==0): #Press Keys
            if (event.key==pygame.K_d or event.key==pygame.K_RIGHT): rd=1
            if (event.key==pygame.K_a or event.key==pygame.K_LEFT): ra=1
            if (event.key==pygame.K_w or event.key==pygame.K_UP): engine=1
        elif (event.type==KEYUP):
            if (event.key==pygame.K_d or event.key==pygame.K_RIGHT): rd=0
            if (event.key==pygame.K_a or event.key==pygame.K_LEFT): ra=0
            if (event.key==pygame.K_w or event.key==pygame.K_UP): engine=0
            if (event.key==pygame.K_r): create(); setup()

        elif (event.type==QUIT): #Quitting
            mainloop=False

    pygame.display.set_caption("FPS: "+str(int(Clock.get_fps()))+" - Press r to Reset Anytime")
    pygame.display.flip()
    
pygame.quit()
