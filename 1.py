import pygame
import random
from pygame.locals import *
from sys import exit

size = wight, height =600,600
X=int(wight/10)
Y=int(height/10)
pygame.init()
TrackSize = X,Y
#mapa
tab = [[0,0,4,3,3,3,3,3,4,4],
       [0,0,3,2,2,2,2,2,4,4],
       [4,4,4,3,3,2,4,3,4,4],
       [-1,2,3,3,3,2,4,3,4,4],
       [-2,2,2,2,2,2,2,2,3,4],
       [-3,2,4,3,3,3,2,3,4,4],
       [4,4,4,0,0,3,2,3,0,4],
       [4,4,4,0,0,3,2,3,0,4],
       [4,4,4,0,0,3,2,3,0,4],
       [4,4,4,0,0,4,3,4,0,4]]
#mapa smeci        
tabtrash = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
zapziel=0
zapzol=0
zapnieb=0
#generowanie miejsca smieci
def generatetrash(a,b):
    while a < 5:
        vx=random.randint(0,9)
        vy=random.randint(0,9)
        if tab[vx][vy]==3 and tabtrash[vx][vy]==0:
            tabtrash[vx][vy] = b
            a=a+1;
    a=0;
tabz=1,2,3
for i in tabz:
    num=0
    generatetrash(num,i)

glasfull = pygame.image.load("glasfull.png")
glasfull = pygame.transform.scale(glasfull,(X,Y))
paperfull = pygame.image.load("paperfull.png")
paperfull = pygame.transform.scale(paperfull,(X,Y))
plasticfull = pygame.image.load("plasticfull.png")
plasticfull = pygame.transform.scale(plasticfull,(X,Y))

cursorSrcLeft = pygame.image.load("cursorLeft.png")
cursorSrcLeft = pygame.transform.scale(cursorSrcLeft,(TrackSize))

cursorSrcUp = pygame.image.load("cursorUp.png")
cursorSrcUp = pygame.transform.scale(cursorSrcUp,(TrackSize))

cursorSrcRight = pygame.image.load("cursorRight.png")
cursorSrcRight = pygame.transform.scale(cursorSrcRight,(TrackSize))

cursorSrcDown = pygame.image.load("cursorDown.png")
cursorSrcDown = pygame.transform.scale(cursorSrcDown,(TrackSize))

cursorSrc=cursorSrcLeft
tree = pygame.image.load("tree.png")
tree = pygame.transform.scale(tree,(X,Y))

houseempty = pygame.image.load("houseempty.png")
houseempty = pygame.transform.scale(houseempty,(X,Y))
housefull = pygame.image.load("housefull.png")
housefull = pygame.transform.scale(housefull,(X,Y))
housefull2 = pygame.image.load("housefull2.png")
housefull2 = pygame.transform.scale(housefull2,(X,Y))
housefull3 = pygame.image.load("housefull3.png")
housefull3 = pygame.transform.scale(housefull3,(X,Y))

glass = pygame.image.load("glass.png")
glass = pygame.transform.scale(glass,(X,Y))
paper = pygame.image.load("paper.png")
paper = pygame.transform.scale(paper,(X,Y))
plastic = pygame.image.load("plastic.png")
plastic = pygame.transform.scale(plastic,(X,Y))

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg,(X,Y))
bg2 = pygame.image.load("bg2.png")
bg2 = pygame.transform.scale(bg2,(size))


#pozycja i szybkosc
speed = X
posX = 4*X
posY = 1*Y
screen = pygame.display.set_mode(size)
display = pygame.display.set_mode((size[0],int(size[1]+(size[1]/10)*3)),0,32) #rozmiar ekranu

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        pressedKeys = pygame.key.get_pressed()
        display.fill((255,255,255))##
        screen.blit(glass,(6*X,10*Y))
        screen.blit(paper,(6*X,11*Y))
        screen.blit(plastic,(6*X,12*Y))
        screen.blit(bg2,(0,0))
        #rysowanie mapy
        for z1 in range(10):
            for z2 in range (10):
                if tab[z1][z2] == -1:
                    screen.blit(glass,(z1*X,z2*Y))
                elif tab[z1][z2] == -2:
                    screen.blit(paper,(z1*X,z2*Y))
                elif tab[z1][z2] == -3:
                    screen.blit(plastic,(z1*X,z2*Y))
                elif tab[z1][z2]  == 2:
                    screen.blit(bg,(z1*X,z2*Y))
                elif tab[z1][z2]  == 3 and tabtrash[z1][z2]==0:
                    screen.blit(houseempty,(z1*X,z2*Y))
                elif tab[z1][z2]  == 3 and tabtrash[z1][z2]==1:
                    screen.blit(housefull,(z1*X,z2*Y))
                elif tab[z1][z2]  == 3 and tabtrash[z1][z2]==2:
                    screen.blit(housefull2,(z1*X,z2*Y))
                elif tab[z1][z2]  == 3 and tabtrash[z1][z2]==3:
                    screen.blit(housefull3,(z1*X,z2*Y))
                elif tab[z1][z2]  == 4:
                    screen.blit(tree,(z1*X,z2*Y))


                
            
        display.blit(cursorSrc, (posX, posY))
        #przejscia i kolizje
        if pressedKeys[K_LEFT]:
            if tab[int(posX/X)-1][int(posY/Y)] == 2:
                posX -= speed
            cursorSrc=cursorSrcLeft
        elif pressedKeys[K_RIGHT]:
            if tab[int(posX/X)+1][int(posY/Y)] == 2:
                posX += speed
            cursorSrc=cursorSrcRight
        if pressedKeys[K_UP]:
            if tab[int(posX/X)][int(posY/Y)-1] == 2:
                posY -= speed
            cursorSrc=cursorSrcUp
        elif pressedKeys[K_DOWN]:
            if tab[int(posX/X)][int(posY/Y)+1] == 2:
                posY += speed
            cursorSrc=cursorSrcDown
#########################zbieranie smieci zielonych
        if pressedKeys[K_LEFT]:
            if tab[int(posX/X)-1][int(posY/Y)] == 3:
                if tabtrash[int(posX/X)-1][int(posY/Y)] == 1 and zapziel!=5:
                    tabtrash[int(posX/X)-1][int(posY/Y)] =0
                    zapziel=zapziel+1;
                    num=4;
                    generatetrash(num,1)
        elif pressedKeys[K_RIGHT]:
            if tab[int(posX/X)+1][int(posY/Y)] == 3:
                if tabtrash[int(posX/X)+1][int(posY/Y)] == 1 and zapziel!=5:
                    tabtrash[int(posX/X)+1][int(posY/Y)] =0
                    zapziel=zapziel+1;
                    num=4;
                    generatetrash(num,1)
        if pressedKeys[K_UP]:
            if tab[int(posX/X)][int(posY/Y)-1] == 3:
                if tabtrash[int(posX/X)][int(posY/Y)-1] == 1 and zapziel!=5:
                    tabtrash[int(posX/X)][int(posY/Y)-1] =0
                    zapziel=zapziel+1;
                    num=4;
                    generatetrash(num,1)
        elif pressedKeys[K_DOWN]:
            if tab[int(posX/X)][int(posY/Y)+1] == 3:
                if tabtrash[int(posX/X)][int(posY/Y)+1] == 1 and zapziel!=5:
                    tabtrash[int(posX/X)][int(posY/Y)+1] =0
                    zapziel=zapziel+1;
                    num=4;
                    generatetrash(num,1)
#########################zbieranie smieci nieb
        if pressedKeys[K_LEFT]:
            if tab[int(posX/X)-1][int(posY/Y)] == 3:
                if tabtrash[int(posX/X)-1][int(posY/Y)] == 2 and zapnieb!=5:
                    tabtrash[int(posX/X)-1][int(posY/Y)] =0
                    zapnieb=zapnieb+1;
                    num=4;
                    generatetrash(num,2)
        elif pressedKeys[K_RIGHT]:
            if tab[int(posX/X)+1][int(posY/Y)] == 3:
                if tabtrash[int(posX/X)+1][int(posY/Y)] == 2 and zapnieb!=5:
                    tabtrash[int(posX/X)+1][int(posY/Y)] =0
                    zapnieb=zapnieb+1;
                    num=4;
                    generatetrash(num,2)
        if pressedKeys[K_UP]:
            if tab[int(posX/X)][int(posY/Y)-1] == 3:
                if tabtrash[int(posX/X)][int(posY/Y)-1] == 2 and zapnieb!=5:
                    tabtrash[int(posX/X)][int(posY/Y)-1] =0
                    zapnieb=zapnieb+1;
                    num=4;
                    generatetrash(num,2)
        elif pressedKeys[K_DOWN]:
            if tab[int(posX/X)][int(posY/Y)+1] == 3:
                if tabtrash[int(posX/X)][int(posY/Y)+1] == 2 and zapnieb!=5:
                    tabtrash[int(posX/X)][int(posY/Y)+1] =0
                    zapnieb=zapnieb+1;
                    num=4;
                    generatetrash(num,2)
#########################zbieranie smieci zółty
        if pressedKeys[K_LEFT]:
            if tab[int(posX/X)-1][int(posY/Y)] == 3:
                if tabtrash[int(posX/X)-1][int(posY/Y)] == 3 and zapzol!=5:
                    tabtrash[int(posX/X)-1][int(posY/Y)] =0
                    zapzol=zapzol+1;
                    num=4;
                    generatetrash(num,3)
        elif pressedKeys[K_RIGHT]:
            if tab[int(posX/X)+1][int(posY/Y)] == 3:
                if tabtrash[int(posX/X)+1][int(posY/Y)] == 3 and zapzol!=5:
                    tabtrash[int(posX/X)+1][int(posY/Y)] =0
                    zapzol=zapzol+1;
                    num=4;
                    generatetrash(num,3)
        if pressedKeys[K_UP]:
            if tab[int(posX/X)][int(posY/Y)-1] == 3:
                if tabtrash[int(posX/X)][int(posY/Y)-1] == 3 and zapzol!=5:
                    tabtrash[int(posX/X)][int(posY/Y)-1] =0
                    zapzol=zapzol+1;
                    num=4;
                    generatetrash(num,3)
        elif pressedKeys[K_DOWN]:
            if tab[int(posX/X)][int(posY/Y)+1] == 3:
                if tabtrash[int(posX/X)][int(posY/Y)+1] == 3 and zapzol!=5:
                    tabtrash[int(posX/X)][int(posY/Y)+1] =0
                    zapzol=zapzol+1;
                    num=4;
                    generatetrash(num,3)
##############################3
        screen.blit(glasfull,(zapziel*X,10*Y))
        screen.blit(paperfull,(zapnieb*X,11*Y))
        screen.blit(plasticfull,(zapzol*X,12*Y))
        
        if pressedKeys[K_UP]:
            if tab[int(posX/X)][int(posY/Y)-1] == -1:
                zapziel=0;
            elif tab[int(posX/X)][int(posY/Y)-1] == -2:
                zapnieb=0;
            elif tab[int(posX/X)][int(posY/Y)-1] == -3:
                zapzol=0;
#########################################################
        if posX >wight-X:
            posX=wight-X
        elif posX < 0:
            posX=0
        if posY >height-Y:
            posY=height-Y
        elif posY <0:
            posY=0
        
        

        pygame.display.update()
        
        
