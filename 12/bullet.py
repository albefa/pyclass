import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        # # 开火标志
        # self.ship_fire = False

    # def fire_bullet(self, ai_settings, screen, ship, bullets):
    #     """如果没有达到限制，就发射一颗子弹"""
    #     # 创建新子弹，并将其加入到编组bullets中
    #     if len(bullets) < ai_settings.bullet_allowed:
    #         new_bullet = Bullet(ai_settings, screen, ship)
    #         bullets.add(new_bullet)

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
        # 连续发射子弹
        # if self.ship_fire:
        #     fire_bullet()

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)