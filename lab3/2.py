import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.draw.rect(screen, pygame.Color("#64f3f8"), (0, 0, 800, 300))
pygame.draw.rect(screen, pygame.Color("#38b32b"), (0, 300, 800, 600))

pygame.draw.

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()