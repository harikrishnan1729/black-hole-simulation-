import time
import pygame
import random as r
import math 
pygame.init()

screen = pygame.display.set_mode((1200, 900))
running = True
stars = []

bx, by = 400, 300
dragging = False

last_spawn_time = 0

def createStar():
    x = r.randint(0, 1200)
    y = r.randint(0, 900)
    vx = r.uniform(-0.1, 0.1)
    vy = r.uniform(-0.1, 0.1)
    stars.append([x, y, vx, vy])

for i in range(40):
    createStar()
clock = pygame.time.Clock()
while running:
    screen.fill((0,0,0))
    # vx += 1
    # vy += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if(pygame.time.get_ticks()-last_spawn_time >= 3000):
        last_spawn_time = pygame.time.get_ticks()
        for i in range(2):
            createStar()

    for star in stars:
        star[0] += star[2]   # x += vx
        star[1] += star[3]   # y += vy

        
        
        pygame.draw.circle(screen, "#F7F2EB", (int(star[0]), int(star[1])), r.randint(1, 3)) 
        if(event.type == pygame.MOUSEBUTTONDOWN):
            dragging = True
        if(event.type == pygame.MOUSEBUTTONUP):
            dragging = False

    
    # making the black hole 
    pygame.draw.circle(screen, "#B37012", (bx, by), 25)
    if dragging:
        bx, by = pygame.mouse.get_pos()





    pygame.display.flip()
    clock.tick(200)
        

        


pygame.quit()

