import pygame
import numpy as np

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60
BG_COLOR = pygame.Color('black')
GRAV = 0.15

class Ball(pygame.sprite.Sprite):
    def __init__(self, group, pos, v, radius, color=pygame.Color("red")):
        super().__init__(all_sprites, group)
        self.v = v
        self.radius = radius
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.v[1] += GRAV
        self.rect = self.rect.move(self.v[0], self.v[1])


class Target(pygame.sprite.Sprite):
    def __init__(self, group, pos, radius, color=pygame.Color("green")):
        super().__init__(all_sprites, group)
        self.radius = radius
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = pygame.Rect(pos, (2 * radius, 2 * radius))

    def update(self):
        if pygame.sprite.spritecollideany(ball):
            self.kill()
            table.add_targets()


class Gun(pygame.sprite.Sprite):
    def __init__(self, width, height, v_max, v_min, delta_v=0.2):
        super().__init__(all_sprites)
        self.v_max = v_max
        self.v_min = v_min
        self.v = v_min
        self.delta_v = delta_v

        self.angle = 0
        self.active = False

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(pygame.Color("#e549f8"))
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, WINDOW_HEIGHT // 2)

    def move(self, step):
        self.rect = self.rect.move(0, step)

    def set_angle(self, x, y):
        self.angle = np.arctan2(y - self.rect.y, x - self.rect.x)
        self.image = pygame.transform.rotate(self.original_image, -np.degrees(self.angle))
        pos = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def toggle_active(self):
        self.active = not self.active

    def shoot(self, v=5):
        Ball(balls, self.rect.center, [v * np.cos(self.angle),
                                       v * np.sin(self.angle)],
             30)
        self.v = self.v_min

    def update(self):
        if self.active and self.v <= self.v_max:
            self.v += self.delta_v


class ScoreTable(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__(all_sprites)
        self.targets_destr = 0
        self.balls_used = 0

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)

    def add_targets():
        pass

    def add_balls(self):
        pass

    def update():
        pass


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(BG_COLOR)

# INIT STUFF
all_sprites = pygame.sprite.Group()
targets = pygame.sprite.Group()
balls = pygame.sprite.Group()

gun = Gun(50, 20, 10, 50)
# table = ScoreTable()
# for i in range(2):
#     Target()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gun.move(-20)
            elif event.key == pygame.K_DOWN:
                gun.move(20)

        if event.type == pygame.MOUSEMOTION:
            mouse_coords = pygame.mouse.get_pos()
            gun.set_angle(*mouse_coords)

        if event.type == pygame.MOUSEBUTTONDOWN:
            gun.toggle_active()

        if event.type == pygame.MOUSEBUTTONUP:
            gun.toggle_active()
            gun.shoot()


    screen.fill(BG_COLOR)

    # DO STUFF
    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()