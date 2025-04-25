from ctypes import pydll
from random import random

import pygame
import random
#import sleep

pygame.init()

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision")

#creat main rectangle & obstacle rectangle
rect_1 = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)

obstacles = []
for _ in range(16):
    obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
    obstacles.append(obstacle_rect)

#define colour
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0,)
BLUE = (0, 0, 255)

#HIDE MOUSE CURSOR
pygame.mouse.set_visible(False)

run = True
while run:

    screen.fill(BG)

    #set colour
    col = GREEN
    if rect_1.collidelist(obstacles) >= 0:
        print(rect_1.collidelist(obstacles))
        col = RED
        print("haha loser")
   # else:



    pos = pygame.mouse.get_pos()
    rect_1.center = pos

    pygame.draw.rect(screen, col, rect_1)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLUE, obstacle)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()