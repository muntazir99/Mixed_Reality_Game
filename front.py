import pygame
import random
pygame.init()

def rand():
    a=random.randrange(100,980)
    b=random.randrange(50,750)
    return a,b

"""a=random.randrange(100,980)
b=random.randrange(50,750)"""

width, height=1080,800
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("AIMING")

##hiii
##score 
score=0
negscore=0

pygame.mixer.music.load('resource/ladyof80.mp3')
pygame.mixer.music.play()

#initialise clock and fps
fps=30
clock=pygame.time.Clock()

ball=pygame.image.load("resource/circle.png").convert_alpha()
ball=pygame.transform.smoothscale(ball,(256,160))
##rball=ball.get_rect()

img= pygame.image.load("resource/scene.jpg").convert()
img=pygame.transform.scale(img,(1080,800))
m,n=rand()
#main loop

start=True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start= False
            pygame.quit()
    
    #window logic
    #window.fill((255, 255, 255))
    



    window.blit(img,(0,0))
    pygame.draw.circle(window,(255,0,0),(m,n),80)


    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==1:
            if (event.pos[0]-m)**2+(event.pos[1]-n)**2<=80**2:
                pygame.draw.circle(window,(0,255,0),(m,n),80)
                window.blit(ball,(m-128,n-80))
                print("HIT")
                score+=1
                pygame.mixer.music.load('resource/punch-a-rock-161647.mp3')
                pygame.mixer.music.play()
                #pygame.time.wait(3000)
                m,n=rand()
                    
            else:
                m,n=rand()
                pygame.draw.circle(window,(255,0,255),(m,n),80)
                print("MISS")
                negscore+=1
                

        
    
    ##rball.x+=5
    ##rball.y+=5
    #pygame.draw.rect(window,(0,0,0),rball)
    ##window.blit(ball,rball)

    clock.tick(fps)
    ""
    pygame.display.update()
#set fps
    


    print("score: ",score)
    print("not hit",negscore)