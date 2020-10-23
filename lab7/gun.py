import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60
BG_COLOR = pygame.Color('black')

class Ball(pygame.sprite.Sprite):
    def __init__(self, group, pos, v, radius, color=pygame.Color("red")):
        super().__init__(all_sprites, group)
        self.pos = pos
        self.v = v
        self.radius = radius
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)

    def update():
        pass


class Target(pygame.sprite.Sprite):
    def __init__(self, group, coord, radius, color=pygame.Color("green")):
        super().__init__(all_sprites, group)
        self.coord = coord
        self.radius = radius
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)

    def update():
        pass


class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.coord = coord
        self.angle = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.active = False
        self.pow = min_pow

    def update():
        pass


class ScoreTable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.targets_destr = 0
        self.balls_used = 0

    def update():
        pass


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(BG_COLOR)

# INIT STUFF
all_sprites = pygame.sprite.Group()
targets = pygame.sprite.Group()
balls = pygame.sprite.Group()

gun = Gun()
table = ScoreTable()
for i in range(2):
    Target()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pass

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.MOUSEBUTTONUP:
            pass

    screen.fill(BG_COLOR)

    # DO STUFF
    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()