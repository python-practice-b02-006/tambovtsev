import pygame
import gui
import data

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60
BG_COLOR = pygame.Color('black')

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(BG_COLOR)

# init groups
buttons = pygame.sprite.Group()
bodies = pygame.sprite.Group()

# init bodies
data.read_data(bodies)

# init gui
slider = gui.Slider(buttons)
start_stop = gui.StartStop(buttons)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        buttons.update(event)
        if event.type == pygame.QUIT:
            running = False
            data.write_data()

    screen.fill(BG_COLOR)

    if start_stop.on:
        bodies.update()

    # buttons.draw(screen)
    bodies.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

