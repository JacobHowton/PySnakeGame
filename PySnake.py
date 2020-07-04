import pygame
import time

# initialize pygame
pygame.init()

# create the screen with height and width

screenx = 800
screeny = 600
snakeHeadWidth = 50
screen = pygame.display.set_mode((screenx, screeny))

pygame.display.set_caption("Snake")

snakeHead = pygame.image.load("healthcare-and-medical.png")
snakeHeadx = 350
snakeHeady = 450
snakeHeadChangeAmount = 50
snakeHeadChangex = 0
snakeHeadChangey = 0


def player(x, y):
    screen.blit(snakeHead, (x, y))


# Game Loop
running = True

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If Keystroke check right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
                snakeHeadChangex = -snakeHeadChangeAmount
                snakeHeadChangey = 0

            elif event.key == pygame.K_RIGHT:
                print("Right")
                snakeHeadChangex = snakeHeadChangeAmount
                snakeHeadChangey = 0

            elif event.key == pygame.K_UP:
                print("Up")
                snakeHeadChangex = 0
                snakeHeadChangey = -snakeHeadChangeAmount

            elif event.key == pygame.K_DOWN:
                print("Down")
                snakeHeadChangex = 0
                snakeHeadChangey = snakeHeadChangeAmount

    if screenx - snakeHeadWidth >= snakeHeadx + snakeHeadChangex >= 0:
        if screeny - snakeHeadWidth >= snakeHeady + snakeHeadChangey >= 0:
            snakeHeadx += snakeHeadChangex
            snakeHeady += snakeHeadChangey

    player(snakeHeadx, snakeHeady)

    pygame.display.update()

    time.sleep(0.5)
