import pygame
import numpy as np
import math

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.draw.rect(screen, pygame.Color("#64f3f8"), (0, 0, 800, 300))
pygame.draw.rect(screen, pygame.Color("#38b32b"), (0, 300, 800, 600))

home_tree_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
home_rect = pygame.Rect(90, 250, 200, 150)
pygame.draw.rect(home_tree_surface, pygame.Color("#a06117"), home_rect)
pygame.draw.polygon(home_tree_surface, pygame.Color("#f93838"),
                    [(90, 250), (190, 130), (290, 250)])
window_rect = pygame.Rect((0, 0), (60, 40))
window_rect.center = home_rect.center
pygame.draw.rect(home_tree_surface, pygame.Color("#3790d5"), window_rect)

pygame.draw.rect(home_tree_surface, pygame.Color("black"),
                 (600 - 250, 230, 20, 120))
for coords in [(610 - 250, 205), (560 - 250, 190),
               (600 - 250, 160), (645 - 250, 190),
               (570 - 250, 230), (640 - 250, 230)]:
    pygame.draw.circle(home_tree_surface, pygame.Color("#256927"), coords, 30)
    pygame.draw.circle(home_tree_surface, pygame.Color("black"), coords, 30, 1)

screen.blit(home_tree_surface, (0, 0))
screen.blit(pygame.transform.scale(home_tree_surface,
                                   (int(800 / 1.5), int(600 / 1.5))),
            (400, 100))

cloud_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
for coords in [(350, 80), (480, 80), (410, 70), (450, 120), (390, 130)]:
    pygame.draw.circle(cloud_surface, pygame.Color("white"), coords, 40)
    pygame.draw.circle(cloud_surface, pygame.Color("#484646"), coords, 40, 1)

screen.blit(cloud_surface, (-150, -30))
screen.blit(pygame.transform.scale(cloud_surface,
                                   (int(800 / 1.5), int(600 / 1.5))),
            (200, 50))
screen.blit(pygame.transform.scale(cloud_surface,
                                   (int(800 / 1.25), int(600 / 1.25))),
            (350, 20))


# x0 + r * cos(a)
# y0 + r * sin(a)
a = np.arange(0, 360, 5)
p1_x = 60 + 50 * np.cos(np.radians(a))
p1_y = 80 + 50 * np.sin(np.radians(a))

p2_x = 60 + 53 * np.cos(np.radians(a))
p2_y = 80 + 53 * np.sin(np.radians(a))

coords = [(p1_x[i], p1_y[i]) if i % 2 == 0 else (p2_x[i], p2_y[i])
          for i in range(360 // 5)]
pygame.draw.polygon(screen, pygame.Color("#f77658"), coords)

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
