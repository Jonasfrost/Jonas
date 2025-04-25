

import pygame
import random

pygame.init()

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision")

obstacles = []
for i in range(16):
    obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
    obstacles.append(obstacle_rect)

    line_start = (screen_width / 2, screen_height / 2)

#define colour
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0,)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


run = True
while run:

    screen.fill(BG)

    pos = pygame.mouse.get_pos()
    pygame.draw.line(screen, WHITE, line_start, pos, 5)

    for obstacle in obstacles:
        if obstacle.clipline((line_start, pos)):
            pygame.draw.rect(screen, RED, obstacle)
        else:
            pygame.draw.rect(screen, GREEN, obstacle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()