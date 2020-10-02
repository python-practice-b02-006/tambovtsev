import pygame
import numpy as np
import math

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)


def blit_with_scale(x, y, scale, surface):
    """
        накладывает поверхность на экран.
        просто не трогай она нужна для работы других функций.
    """
    w, h = surface.get_size()
    surface = pygame.transform.scale(surface,
                                     (int(w * scale), int(h * scale)))
    screen.blit(surface, (x - w * scale // 2,
                          y - h * scale // 2))


def draw_home(x, y, scale):
    """
        Нарисовать дом
        x, y {int} - координаты центра домика
        scale {float} - масштабирование домика. линейные размеры
                        умножаются на эту величину
        по умолчанию размеры домика 200 х 280
    """
    surface = pygame.Surface((200, 280), pygame.SRCALPHA)
    home_rect = pygame.Rect(0, 130, 200, 150)
    pygame.draw.rect(surface, pygame.Color("#a06117"), home_rect)
    pygame.draw.polygon(surface, pygame.Color("#f93838"),
                        [(0, 130), (100, 0), (200, 130)])
    window_rect = pygame.Rect((0, 0), (60, 40))
    window_rect.center = home_rect.center
    pygame.draw.rect(surface, pygame.Color("#3790d5"), window_rect)

    blit_with_scale(x, y, scale, surface)


def draw_tree(x, y, scale):
    """
        Нарисовать дерево
        x, y {int} - координаты центра дерева
        scale {float} - масштабирование дерева. линейные размеры
                        умножаются на эту величину
        по умолчанию размеры дерева 150 х 230
    """
    surface = pygame.Surface((150, 230), pygame.SRCALPHA)

    pygame.draw.rect(surface, pygame.Color("black"), (70, 70, 20, 500))
    for coords in [(610, 205), (560, 190),
                   (600, 160), (645, 190),
                   (570, 230), (640, 230)]:
        coords = (coords[0] - 525, coords[1] - 130)
        pygame.draw.circle(surface, pygame.Color("#256927"), coords, 30)
        pygame.draw.circle(surface, pygame.Color("black"), coords, 30, 1)

    blit_with_scale(x, y, scale, surface)


def draw_clouds(x, y, scale):
    """
        Нарисовать облака
        x, y {int} - координаты центра.
        scale {float} - масштабирование. линейные размеры
                        умножаются на эту величину
        по умолчанию размеры дерева 210 х 140
    """
    surface = pygame.Surface((210, 140), pygame.SRCALPHA)
    for coords in [(350, 80), (480, 80), (410, 70), (450, 120), (390, 130)]:
        coords = (coords[0] - 310, coords[1] - 30)  # немотивированное действие
        pygame.draw.circle(surface, pygame.Color("white"), coords, 40)
        pygame.draw.circle(surface, pygame.Color("#484646"), coords, 40, 1)

    blit_with_scale(x, y, scale, surface)


def draw_sun(x, y, radius):
    """
        Нарисовать солнцк
        x, y {int} - координаты центра.
        radius {int} - радиус
    """
    surface = pygame.Surface((108, 108), pygame.SRCALPHA)

    a = np.arange(0, 360, 5)
    p1_x = x + radius * np.cos(np.radians(a))
    p1_y = y + radius * np.sin(np.radians(a))

    p2_x = x + (radius + radius / 10) * np.cos(np.radians(a))
    p2_y = y + (radius + radius / 10) * np.sin(np.radians(a))

    coords = [(p1_x[i], p1_y[i]) if i % 2 == 0 else (p2_x[i], p2_y[i])
              for i in range(360 // 5)]
    pygame.draw.polygon(screen, pygame.Color("#f77658"), coords)


pygame.draw.rect(screen, pygame.Color("#64f3f8"), (0, 0, 800, 300))
pygame.draw.rect(screen, pygame.Color("#38b32b"), (0, 300, 800, 600))

draw_home(150, 230, 1)
draw_tree(700, 250, 1)
draw_clouds(300, 80, 1)
draw_sun(600, 80, 70)

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
