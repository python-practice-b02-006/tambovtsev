import pygame
import numpy as np
import random
from PIL import Image, ImageDraw, ImageOps


WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60
BG_COLOR = pygame.Color('black')
COLORS = [pygame.Color("BLUE"), pygame.Color("YELLOW"), pygame.Color("GREEN"),
          pygame.Color("MAGENTA"), pygame.Color("CYAN")]
GRAV = 0.4


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, v, radius, color=pygame.Color("yellow")):
        super().__init__(all_sprites, balls)
        self.v = v
        self.radius = radius
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.v[1] += GRAV
        self.rect = self.rect.move(self.v[0], self.v[1])


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, length, angle, width=10, color=pygame.Color("coral")):
        super().__init__(all_sprites, walls)
        self.length = length
        self.angle = angle
        self.color = color

        self.image = pygame.Surface((length, width), pygame.SRCALPHA)
        self.image.fill(color)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        pass


class Target(pygame.sprite.Sprite):
    def __init__(self, pos, radius, color=pygame.Color("green")):
        super().__init__(all_sprites, targets)
        self.radius = radius
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        if pygame.sprite.spritecollideany(self, balls):
            self.kill()
            table.add_targets()


class Gun(pygame.sprite.Sprite):
    def __init__(self, width=50, height=20, v_min=7, v_max=30, delta_v=0.7):
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

    def toggle_active(self):
        self.active = not self.active

    def shoot(self):
        Ball(self.rect.center, [self.v * np.cos(self.angle),
                                self.v * np.sin(self.angle)],
             20)
        self.v = self.v_min
        self.original_image.fill(pygame.Color("#e549f8"))

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, -np.degrees(self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)

        if self.active and self.v <= self.v_max:
            self.v += self.delta_v
            pygame.draw.rect(self.original_image, pygame.Color("#588f0a"),
                             (0, 0,
                              self.rect.width * (self.v - self.v_min) / (self.v_max - self.v_min),
                              self.rect.height))


class ScoreTable(pygame.sprite.Sprite):
    def __init__(self, width=300, height=200):
        super().__init__(all_sprites)
        self.width = width
        self.height = height

        self.targets_destr = 0
        self.balls_used = 0
        self.font = pygame.font.Font(None, 50)

        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

    def add_targets(self):
        self.targets_destr += 1

    def add_balls(self):
        self.balls_used += 1

    def score(self):
        return self.targets_destr - self.balls_used

    def update(self):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        text = []
        text.append(self.font.render(f"Destroyed: {self.targets_destr}", True, pygame.Color("WHITE")))
        text.append(self.font.render(f"Balls used: {self.balls_used}", True, pygame.Color("WHITE")))
        text.append(self.font.render(f"Total: {self.score()}", True, pygame.Color("RED")))
        for i in range(len(text)):
            self.image.blit(text[i], (5, 10 + 40 * i))

def add_target():
    maxR = 70
    minR = 30
    r = random.randint(minR, maxR)
    x = random.randint(100, WINDOW_WIDTH - r)
    y = random.randint(r, WINDOW_HEIGHT - r)
    Target((x, y), r, color=random.choice(COLORS))


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(BG_COLOR)

# INIT STUFF
all_sprites = pygame.sprite.Group()
targets = pygame.sprite.Group()
balls = pygame.sprite.Group()
walls = pygame.sprite.Group()

gun = Gun()
Wall((0, WINDOW_HEIGHT // 2), WINDOW_HEIGHT, 90, width=1, color=BG_COLOR)
Wall((WINDOW_WIDTH - 1, WINDOW_HEIGHT // 2), WINDOW_HEIGHT, 90,  width=1, color=BG_COLOR)
Wall((WINDOW_WIDTH // 2, 0), WINDOW_WIDTH, 0, width=1, color=BG_COLOR)
Wall((WINDOW_WIDTH // 2, WINDOW_HEIGHT - 1), WINDOW_WIDTH, 0, width=1, color=BG_COLOR)
table = ScoreTable()
for i in range(4):
    add_target()

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
            table.add_balls()


    screen.fill(BG_COLOR)

    # DO STUFF
    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()