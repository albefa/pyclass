import sys

import pygame


# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = True
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = True
#             elif event.key == pygame.K_UP:
#                 ship.moving_up = True
#             elif event.key ==pygame.K_DOWN:
#                 ship.moving_down = True
#
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False
#             elif event.key == pygame.K_UP:
#                 ship.moving_up = False
#             elif event.key == pygame.K_DOWN:
#                 ship.moving_down = False
def check_key_down_event(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def check_key_up_event(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_key_up_event(event, ship)


def update_screen(ai_setting, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()