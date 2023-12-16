import sys
import pygame
from juese import Juese

def run_p():
    pygame.init()
    screen = pygame.display.set_mode((1200, 1200))
    pygame.display.set_caption("天空")

    # 增加一张图片
    a_picture = Juese(screen)

    sky_color=(100, 100, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(sky_color)
        a_picture.blitme()

        pygame.display.flip()


run_p()