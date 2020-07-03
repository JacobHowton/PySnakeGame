import pygame

# initialize pygame
pygame.init()

# create the screen with height and width
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Snake")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.update()