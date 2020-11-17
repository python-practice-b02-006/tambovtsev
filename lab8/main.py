import pygame
import body
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
bodies = body.System()

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

    # determining how fast is the system drawn based on the position of the slider.
    dt = slider.calc_value()
    if start_stop.on and bodies.size > 0:
        # first we calculate new positions on all bodies
        bodies.new_state(dt)
        # then we move them
        bodies.update(WINDOW_SIZE)

    buttons.draw(screen)
    bodies.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

