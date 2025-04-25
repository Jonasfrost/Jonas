import pygame
import random
import math

# initialize the pygame
pygame.init()
from pygame import mixer

# create screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('bg_space2.png')

# bg sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load('001-battleship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('001-battleship.png.')
playerX = 370
playerY = 480
playerX_change = 0

# how many enemies are there
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 25
for i in range(num_of_enemy):
    # enemy
    enemyImg.append(pygame.image.load('001-ufo.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.8)
    enemyY_change.append(40)

# bullet

# ready no bullet
# fire bullet is there
bulletImg = pygame.image.load('001-laser.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

# score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

#draw score
def show_score(x, y):
    score = font.render("score :" + str(score_value),True, (255, 255, 255,))
    screen.blit(score, (x, y))

# draw game over text
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255,))
    screen.blit(over_text, (200, 250))

# draw player
def player(x, y):
    screen.blit(playerImg, (x, y))

# draw enemy
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# draw laser
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
run = True
while run:

    # bg colour
    screen.fill((0, 0, 0))

    # background img
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.2
            if event.key == pygame.K_UP:
                playerY_change = -1.2
            if event.key == pygame.K_DOWN:
                playerY_change = 1.2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound ('laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # stop movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # checking border
    playerX += playerX_change

    # BORDER PLAYER
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    for i in range(num_of_enemy):

        # game over
        if enemyY[i] > 480:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            death_sound = mixer.Sound('035e7412e61aeb2e796c6ed513ab-orig.wav')
            death_sound.play()
            break

        # enemy movement
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # collision check
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i]= random.randint(50, 150)
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()

        enemy(enemyX[i], enemyY[i], i)

            # bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()