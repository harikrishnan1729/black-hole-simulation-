import time
import pygame
import random as r
import math 
pygame.init()

screen = pygame.display.set_mode((1200, 900))
running = True
stars = []
to_remove = []

color = (225,225,225)
bx, by = 400, 300
dragging = False

dx, dy = 1, 1


last_spawn_time = 0

def createStar():
    intensity = 1
    global rotationIntensity
    x = r.randint(0, 1200)
    y = r.randint(0, 900)
    vx = r.uniform(-1, 1) 
    vy = r.uniform(-0.1, 0.1) 
    
    
    stars.append([x, y, vx, vy, color, intensity])



for i in range(5):
    createStar()

clock = pygame.time.Clock()
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # if(pygame.time.get_ticks()-last_spawn_time >= 10000):
    #     last_spawn_time = pygame.time.get_ticks()
    #     for i in range(2):
    #         createStar()

    for star in stars:
        star[0] += star[2]   # x += vx
        star[1] += star[3]   # y += vy

        
        pygame.draw.circle(screen, star[4], (int(star[0]), int(star[1])), r.randint(1, 2)) 

        distance = math.sqrt((star[0]-bx)**2 + (star[1]-by)**2)
        # print(distance)
        
        if(distance<400):
            dx =  bx - star[0]
            dy = by - star[1]

            # dx and dy are the direction unit vectors from star to BH

            dx /= distance
            dy /= distance
            dx *= star[5]
            dy *= star[5]

            star[2] += dx * 0.05
            star[3] += dy * 0.05
            # star[2]*=0.99
            # star[3]*=0.99 
            
            star[5] += 0.1
            # print(star[5])
        

        if distance < 5:
            to_remove.append(star)
            print(star)

        # for star in to_remove:
        #     stars.remove(star)
        

        if(event.type == pygame.MOUSEBUTTONDOWN):
            dragging = True
        if(event.type == pygame.MOUSEBUTTONUP):
            dragging = False

    
    # making the black hole 
    pygame.draw.circle(screen, "#2C2A27", (bx, by), 25)
    if dragging:
        bx, by = pygame.mouse.get_pos()



    pygame.display.flip()
    clock.tick(100)
        

        


pygame.quit()

