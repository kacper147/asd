import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

x, y = 320, 240

# Game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            y += 1

    # Update.

    # Draw.
    screen.fill((255, 255, 255))
    pygame.draw.circle(
        screen,
        (0, 255, 0),
        (x, y),
        20
    )

    pygame.display.flip()
    fpsClock.tick(fps)