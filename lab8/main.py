import pygame
import body
import gui
import io

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60
BG_COLOR = pygame.Color('black')

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(BG_COLOR)


# INIT STUFF
all_sprites = pygame.sprite.Group()
bodies = pygame.sprite.Group()

# bodies
for body in io.read_data():
    pass

# gui
slider = gui.Slider(all_sprites)
start_stop = gui.StartStop(all_sprites)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            io.write_data()

    screen.fill(BG_COLOR)

    # DO STUFF
    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

