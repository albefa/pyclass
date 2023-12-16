import pygame
class Juese():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('aline.png')
        self.rect = self.image.get_rect()
        self.screen.rect = screen.get.rect()

        self.rect.centerx =self.screen_rect.centerx

    def blitme(self):
        """绘制图片"""
        self.screen.bilt(self.image, self.rect)