import pygame
import time
import random


def snake(screen, snakeSegments, x, y):
    screen.blit(snakeSegments, (x, y))


def circle(screen, snakeGrow, x, y):
    screen.blit(snakeGrow, (x, y))


# Main Menu
def startMenu(screenx, screeny):
    screen = pygame.display.set_mode((screenx, screeny))
    font = pygame.font.Font('freesansbold.ttf', 64)

    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    color = WHITE
    buttonBackColor = GRAY
    gameOverText = font.render("Start Game", True, (color))

    # buttonBack = pygame.draw.rect(screen, buttonBackColor, (screenx/2 - 210, screeny/2 - 65, 375, 75))
    buttonBack = pygame.Rect(screenx / 2 - 210, screeny / 2 - 65, 375, 75)
    screen.blit(gameOverText, (screenx / 2 - 200, screeny / 2 - 60))

    running = True
    while running:

        for event in pygame.event.get():

            pos = pygame.mouse.get_pos()

            if buttonBack.collidepoint(pos):
                color = GRAY
                gameOverText = font.render("Start Game", True, (color))

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    running = False

            else:
                color = WHITE
                gameOverText = font.render("Start Game", True, (color))

        screen.blit(gameOverText, (screenx / 2 - 200, screeny / 2 - 60))
        pygame.display.update()


# Game Loop
def snakeGame(screenx, screeny):
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

    font = pygame.font.Font('freesansbold.ttf', 16)
    score = 0

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
        if screenx - snakeHeadWidth >= snakeSegmentX[0] + snakeHeadChangex >= 0 and screeny - snakeHeadWidth >= \
                snakeSegmentY[0] + snakeHeadChangey >= 0:
            for i in range(snakeLength - 1, 0, -1):
                snakeSegmentX[i] = snakeSegmentX[i - 1]
                snakeSegmentY[i] = snakeSegmentY[i - 1]

            snakeSegmentX[0] += snakeHeadChangex
            snakeSegmentY[0] += snakeHeadChangey

        # If the snake head is out of bounds of the map end game
        else:
            running = False

        for i in range(snakeLength):
            snake(screen, snakeSegments, snakeSegmentX[i], snakeSegmentY[i])

            for j in range(snakeLength):
                if i != j and snakeSegmentX[i] == snakeSegmentX[j] and snakeSegmentY[i] == snakeSegmentY[j]:
                    running = False

        # Check if the snake head touches the circle
        if snakeSegmentX[0] == snakeGrowx and snakeSegmentY[0] == snakeGrowy:
            snakeLength += 1
            snakeGrowx = round(random.randint(0, screenx - snakeHeadWidth) / snakeHeadWidth) * snakeHeadWidth
            snakeGrowy = round(random.randint(0, screeny - snakeHeadWidth) / snakeHeadWidth) * snakeHeadWidth
            snakeSegmentX.append(snakeSegmentX[snakeLength - 2] - snakeHeadChangex)
            snakeSegmentY.append(snakeSegmentY[snakeLength - 2] - snakeHeadChangey)
            score += 1

        circle(screen, snakeGrow, snakeGrowx, snakeGrowy)

        scoreText = font.render("SCORE: " + str(score), True, (255, 255, 255))

        screen.blit(scoreText, (0, 0))

        pygame.display.update()

        time.sleep(0.5)
    gameOver(screenx, screeny)


# Game over screen
def gameOver(screenx, screeny):
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    screen = pygame.display.set_mode((screenx, screeny))
    font = pygame.font.Font('freesansbold.ttf', 64)
    buttonFont = pygame.font.Font('freesansbold.ttf', 32)

    gameOverText = font.render("GAME OVER", True, (255, 255, 255))

    retryButtonColor = WHITE
    quitButtonColor = WHITE

    retryButtonText = buttonFont.render("RETRY", True, retryButtonColor)
    quitButtonText = buttonFont.render("QUIT", True, retryButtonColor)

    retryButtonBack = pygame.Rect(screenx / 2 - 50, screeny / 2, 110, 30)
    quitButtonBack = pygame.Rect(screenx / 2 - 40, screeny / 2 + 40, 80, 30)

    screen.blit(gameOverText, (screenx / 2 - 200, screeny / 2 - 150))

    running = True
    while running:

        for event in pygame.event.get():

            pos = pygame.mouse.get_pos()

            if retryButtonBack.collidepoint(pos):
                retryButtonColor = GRAY
                retryButtonText = buttonFont.render("RETRY", True, retryButtonColor)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    snakeGame(screenx, screeny)

            else:
                retryButtonColor = WHITE
                retryButtonText = buttonFont.render("RETRY", True, retryButtonColor)

            if quitButtonBack.collidepoint(pos):
                quitButtonColor = GRAY
                quitButtonText = buttonFont.render("QUIT", True, quitButtonColor)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pygame.display.quit()
                    pygame.quit()
                    exit()

            else:
                quitButtonColor = WHITE
                quitButtonText = buttonFont.render("QUIT", True, quitButtonColor)

        screen.blit(retryButtonText, (screenx / 2 - 50, screeny / 2))
        screen.blit(quitButtonText, (screenx / 2 - 40, screeny / 2 + 40))
        pygame.display.update()


# Initialize pygame
pygame.init()

screenx = 800
screeny = 600

# Start Menu
startMenu(screenx, screeny)

# Main Loop
snakeGame(screenx, screeny)
