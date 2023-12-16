import sys

import pygame


def run_sky():
    pygame.init()
    screen = pygame.display.set_mode((800, 800),)
    pygame.display.set_caption("天空")

    sky_color=(100, 100, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(sky_color)

        pygame.display.flip()

run_sky()