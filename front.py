import pygame
import random
import cv2
import numpy as np
import math
import hit_detection

pygame.init()
event_type = "Hit"
event_type2 = "Miss"


def rand():
    a = random.randrange(100, 980)
    b = random.randrange(50, 750)
    return a, b


"""a=random.randrange(100,980)
b=random.randrange(50,750)"""

width, height = 1080, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("AIMING")

##hiii
##score
score = 0
negscore = 0

<<<<<<< HEAD
# path = C:\Users\Sahil Sahu\Desktop\Mixed_reality_game\resource
pygame.mixer.music.load(
    r"C:\Users\Sahil Sahu\Desktop\Mixed_reality_game\resource\ladyof80.mp3"
)
=======
pygame.mixer.music.load('resource/ladyof80.mp3')
>>>>>>> 0b6310b15c7cf6edbe6b496cb9012e978c21f7c2
pygame.mixer.music.play()

# initialise clock and fps
fps = 30
clock = pygame.time.Clock()

<<<<<<< HEAD
ball = pygame.image.load(
    r"C:\Users\Sahil Sahu\Desktop\Mixed_reality_game\resource\circle.png"
).convert_alpha()
ball = pygame.transform.smoothscale(ball, (256, 160))
=======
ball=pygame.image.load("resource/circle.png").convert_alpha()
ball=pygame.transform.smoothscale(ball,(256,160))
>>>>>>> 0b6310b15c7cf6edbe6b496cb9012e978c21f7c2
##rball=ball.get_rect()

img = pygame.image.load("resource/Background.png").convert()
img = pygame.transform.scale(img, (1080, 800))
m, n = rand()
# main loop

start = True
while start:
    status = hit_detection.hit_detect()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # window logic
    # window.fill((255, 255, 255))

    window.blit(img, (0, 0))
    pygame.draw.circle(window, (255, 0, 0), (m, n), 80)

    if event_type == status:  # pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(window, (0, 255, 0), (m, n), 80)
        window.blit(ball, (m - 128, n - 80))
        print("HIT")
        score += 1
        pygame.mixer.music.load(
            r"C:\Users\Sahil Sahu\Desktop\Mixed_reality_game\resource\punch-a-rock-161647.mp3"
        )
        pygame.mixer.music.play()
        # pygame.time.wait(3000)
        m, n = rand()

    else:
        m, n = rand()
        pygame.draw.circle(window, (255, 0, 255), (m, n), 80)
        print("MISS")
        negscore += 1
    
    
    # x = "Hit"

    # def scoreq(x):
    #     if x == "Hit":
    #         global score
    #         print("HIT")
    #         score += 1
    #     else:
    #         print("MISS")

<<<<<<< HEAD
=======

    window.blit(img,(0,0))
    pygame.draw.circle(window,(255,0,0),(m,n),80)


  
    # if event.type==pygame.MOUSEBUTTONDOWN:
    #     if event.button==1:
    #         if (event.pos[0]-m)**2+(event.pos[1]-n)**2<=80**2:
    #             pygame.draw.circle(window,(0,255,0),(m,n),80)
    #             window.blit(ball,(m-128,n-80))
    #             print("HIT")
    #             score+=1
    #             pygame.mixer.music.load(r'C:\Users\Sahil Sahu\Desktop\Mixed_reality_game\resource\punch-a-rock-161647.mp3')
    #             pygame.mixer.music.play()
    #             #pygame.time.wait(3000)
    #             m,n=rand()
                    
    #         else:
    #             m,n=rand()
    #             pygame.draw.circle(window,(255,0,255),(m,n),80)
    #             print("MISS")
    #             negscore+=1
    x="Hit"         
    def scoreq(x):
        if x=="Hit":
            global score
            print("HIT")
            score += 1
        else:
            print("MISS")

         
        
    
>>>>>>> 0b6310b15c7cf6edbe6b496cb9012e978c21f7c2
    ##rball.x+=5
    ##rball.y+=5
    # pygame.draw.rect(window,(0,0,0),rball)
    ##window.blit(ball,rball)

    clock.tick(fps)
    pygame.display.update()
    # set fps

    print("score: ", score)
    print("not hit", negscore)
