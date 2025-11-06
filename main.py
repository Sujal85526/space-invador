import pygame
import random 
# initialize
pygame.init()

# game screen
screen = pygame.display.set_mode((800,600))

# background
background = pygame.image.load("background.jpg")

# title and icon 
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 420
playerX_change = 0 

# Enemy 
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

# Bullet

# Ready - You can't see the bullet on screen
# Fire -  The bullet is currenlty moving 

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 420
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" 


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# game loop 
running = True
while running:
    # RGB red, green, blue
    screen.fill((0, 77, 0))
    # background image
    screen.blit(background,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # if keystroke is pressed check whether it's right or left 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # Checking for boundaries so it doesn't get out 
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement 
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Bullet Movement 
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


    