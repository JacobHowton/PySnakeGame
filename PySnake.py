import pygame
import time
import random

# initialize pygame
pygame.init()

# create the screen with height and width

screenx = 800
screeny = 600
snakeHeadWidth = 50
screen = pygame.display.set_mode((screenx, screeny))

pygame.display.set_caption("Snake")

snakeSegments = pygame.image.load("WhiteSquare48x48.png")
snakeHeadChangeAmount = 50
snakeHeadChangex = snakeHeadChangeAmount
snakeHeadChangey = 0

snakeLength = 1

snakeSegmentX = []
snakeSegmentY = []

snakeSegmentX.append(round((screenx - snakeHeadWidth) / snakeHeadWidth / 2) * snakeHeadWidth)
snakeSegmentY.append(round((screeny - snakeHeadWidth) / snakeHeadWidth / 2) * snakeHeadWidth)

snakeGrow = pygame.image.load("WhiteCircle50x50.png")
snakeGrowx = round(random.randint(0, screenx - snakeHeadWidth) / snakeHeadWidth) * snakeHeadWidth
snakeGrowy = round(random.randint(0, screeny - snakeHeadWidth) / snakeHeadWidth) * snakeHeadWidth


def snake(x, y):
    screen.blit(snakeSegments, (x, y))


def circle(x, y):
    screen.blit(snakeGrow, (x, y))


# Game Loop
running = True

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If Keystroke check right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snakeHeadChangey != 0:
                print("Left")
                snakeHeadChangex = -snakeHeadChangeAmount
                snakeHeadChangey = 0

            elif event.key == pygame.K_RIGHT and snakeHeadChangey != 0:
                print("Right")
                snakeHeadChangex = snakeHeadChangeAmount
                snakeHeadChangey = 0

            elif event.key == pygame.K_UP and snakeHeadChangex != 0:
                print("Up")
                snakeHeadChangex = 0
                snakeHeadChangey = -snakeHeadChangeAmount

            elif event.key == pygame.K_DOWN and snakeHeadChangex != 0:
                print("Down")
                snakeHeadChangex = 0
                snakeHeadChangey = snakeHeadChangeAmount

    # Checking the bounds for the snake head
    if screenx - snakeHeadWidth >= snakeSegmentX[0] + snakeHeadChangex >= 0:
        if screeny - snakeHeadWidth >= snakeSegmentY[0] + snakeHeadChangey >= 0:
            for i in range(snakeLength - 1, 0, -1):
                snakeSegmentX[i] = snakeSegmentX[i - 1]
                snakeSegmentY[i] = snakeSegmentY[i - 1]

            snakeSegmentX[0] += snakeHeadChangex
            snakeSegmentY[0] += snakeHeadChangey

    for i in range(snakeLength):
        snake(snakeSegmentX[i], snakeSegmentY[i])

    # Check if the snake head touches the circle
    if snakeSegmentX[0] == snakeGrowx and snakeSegmentY[0] == snakeGrowy:
        snakeLength += 1
        snakeGrowx = round(random.randint(0, screenx - snakeHeadWidth) / snakeHeadWidth) * snakeHeadWidth
        snakeGrowy = round(random.randint(0, screeny - snakeHeadWidth) / snakeHeadWidth) * snakeHeadWidth
        snakeSegmentX.append(snakeSegmentX[snakeLength - 2] - snakeHeadChangex)
        snakeSegmentY.append(snakeSegmentY[snakeLength - 2] - snakeHeadChangey)

    circle(snakeGrowx, snakeGrowy)

    pygame.display.update()

    time.sleep(0.5)
