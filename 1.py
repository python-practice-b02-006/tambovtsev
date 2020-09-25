import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

screen.fill(pygame.Color("#bbbbbb"))
pygame.draw.circle(screen, pygame.Color("#ffde00"), (400, 300), 200)

pygame.draw.circle(screen, pygame.Color("#ff0000"), (320, 230), 30)
pygame.draw.circle(screen, pygame.Color("#ff0000"), (480, 230), 23)

pygame.draw.circle(screen, pygame.Color("black"), (320, 230), 10)
pygame.draw.circle(screen, pygame.Color("black"), (480, 230), 10)

pygame.draw.line(screen, pygame.Color("black"), (250, 150), (350, 200), 20)
pygame.draw.line(screen, pygame.Color("black"), (450, 200), (600, 150), 20)

pygame.draw.rect(screen, pygame.Color("black"), (320, 360, 160, 30))

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()