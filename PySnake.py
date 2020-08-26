import pygame
import time
import random


def snake(screen, snakeSegments, x, y):
    screen.blit(snakeSegments, (x, y))


def circle(screen, snakeGrow, x, y):
    screen.blit(snakeGrow, (x, y))


# Main Menu
def startMenu(screenx, screeny, totalScores):
    screen = pygame.display.set_mode((screenx, screeny))
    font = pygame.font.Font('freesansbold.ttf', 64)

    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    color = WHITE
    startGameText = font.render("Start Game", True, (color))

    buttonBack = pygame.Rect(screenx / 2 - 210, screeny / 2 - 65, 375, 75)
    screen.blit(startGameText, (screenx / 2 - 200, screeny / 2 - 60))

    running = True
    while running:

        for event in pygame.event.get():

            # Store the position of the mouse for checking collisions
            pos = pygame.mouse.get_pos()

            # If the button is hovered, change the color of the text
            if buttonBack.collidepoint(pos):
                color = GRAY
                startGameText = font.render("Start Game", True, (color))

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    running = False

            else:
                color = WHITE
                startGameText = font.render("Start Game", True, (color))

        screen.blit(startGameText, (screenx / 2 - 200, screeny / 2 - 60))
        pygame.display.update()


# Main Game Loop
def snakeGame(screenx, screeny, totalScores):
    # Width of all the snake parts in a square's edge's pixles
    snakeHeadWidth = 50

    # Time between movements
    gameTickTime = 0.5

    screen = pygame.display.set_mode((screenx, screeny))

    pygame.display.set_caption("Snake")

    snakeSegments = pygame.image.load("WhiteSquare48x48.png")
    snakeHeadChangeAmount = 50
    snakeHeadChangex = snakeHeadChangeAmount
    snakeHeadChangey = 0

    snakeLength = 1

    # Arrays of all of the x and y coordinates of each segment
    snakeSegmentX = []
    snakeSegmentY = []

    snakeSegmentX.append(round((screenx - snakeHeadWidth) / snakeHeadWidth / 2) * snakeHeadWidth)
    snakeSegmentY.append(round((screeny - snakeHeadWidth) / snakeHeadWidth / 2) * snakeHeadWidth)

    snakeGrow = pygame.image.load("WhiteCircle50x50.png")
    snakeGrowx = round(random.randint(0, screenx - snakeHeadWidth) / snakeHeadWidth) * snakeHeadWidth
    snakeGrowy = round(random.randint(0, screeny - snakeHeadWidth) / snakeHeadWidth) * snakeHeadWidth

    font = pygame.font.Font('freesansbold.ttf', 32)

    score = 0

    running = True
    while running:

        time.sleep(gameTickTime)

        # Fill the screen black
        screen.fill((0, 0, 0))

        hasMoved = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # If Keystroke check for directional change but not more than one direction change per timetick
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snakeHeadChangey != 0 and hasMoved is False:
                    hasMoved = True
                    snakeHeadChangex = -snakeHeadChangeAmount
                    snakeHeadChangey = 0

                elif event.key == pygame.K_RIGHT and snakeHeadChangey != 0 and hasMoved is False:
                    hasMoved = True
                    snakeHeadChangex = snakeHeadChangeAmount
                    snakeHeadChangey = 0

                elif event.key == pygame.K_UP and snakeHeadChangex != 0 and hasMoved is False:
                    hasMoved = True
                    snakeHeadChangex = 0
                    snakeHeadChangey = -snakeHeadChangeAmount

                elif event.key == pygame.K_DOWN and snakeHeadChangex != 0 and hasMoved is False:
                    snakeHeadChangex = 0
                    snakeHeadChangey = snakeHeadChangeAmount

        # Checking the bounds for the snake head vs the edges of the screen
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

            # Check if the snake's head is colliding with any body segments
            for j in range(snakeLength):
                if i != j and snakeSegmentX[i] == snakeSegmentX[j] and snakeSegmentY[i] == snakeSegmentY[j]:
                    running = False

        # Check if the snake head touches the 'grow' and if so add another segment and increment score
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

    totalScores.append(score)
    gameOver(screenx, screeny, totalScores)


# Game over screen
def gameOver(screenx, screeny, totalScores):
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    screen = pygame.display.set_mode((screenx, screeny))
    font = pygame.font.Font('freesansbold.ttf', 64)
    buttonFont = pygame.font.Font('freesansbold.ttf', 32)

    gameOverText = font.render("GAME OVER", True, (255, 255, 255))

    retryButtonColor = WHITE
    quitButtonColor = WHITE

    retryButtonText = buttonFont.render("RETRY", True, retryButtonColor)
    quitButtonText = buttonFont.render("QUIT", True, quitButtonColor)

    retryButtonBack = pygame.Rect(screenx / 2 - 50, screeny / 2, 110, 30)
    quitButtonBack = pygame.Rect(screenx / 2 - 40, screeny / 2 + 40, 80, 30)

    scoreText = buttonFont.render("SCORE: " + str(totalScores[len(totalScores) - 1]), True, (255, 255, 255))
    scoreTextHighest = buttonFont.render("HIGH SCORE: " + str(max(totalScores)), True, (255, 255, 255))

    screen.blit(gameOverText, (screenx / 2 - 200, screeny / 2 - 150))
    screen.blit(scoreText, (0, 0))
    screen.blit(scoreTextHighest, (0, 25))

    running = True
    while running:

        for event in pygame.event.get():

            pos = pygame.mouse.get_pos()

            if retryButtonBack.collidepoint(pos):
                retryButtonColor = GRAY
                retryButtonText = buttonFont.render("RETRY", True, retryButtonColor)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    snakeGame(screenx, screeny, totalScores)

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

# X and Y dimmensions of the screen
screenx = 800
screeny = 600

# An array to hold the scores
totalScores = []

# Start Menu
startMenu(screenx, screeny, totalScores)

# Main Loop
snakeGame(screenx, screeny, totalScores)
