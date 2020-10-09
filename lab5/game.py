import pygame
from pygame.draw import *
import random

pygame.init()

FPS = 50
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode(WINDOW_SIZE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

VMAX = 5


class Ball(pygame.sprite.Sprite):
    """
        кружок
        за нажатие на него дается 1 балл
    """

    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA)
        pygame.draw.circle(self.image, random.choice(COLORS),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-VMAX, VMAX)
        self.vy = random.randrange(-VMAX, VMAX)

    def update(self, click):
        global points
        self.rect = self.rect.move(self.vx, self.vy)
        if click is not None and (self.rect.centerx - event.pos[0]) ** 2 + \
                                 (self.rect.centery - event.pos[1]) ** 2 <= self.radius ** 2:
            points += 1
            self.kill()
            add_ball()
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Square(pygame.sprite.Sprite):
    """
        второй тип мишени (квадрат)
        за нажатие на нее дается 2 балла
    """
    def __init__(self, width, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((width, width))
        self.image.fill(random.choice(COLORS))
        self.rect = pygame.Rect(x, y, width, width)
        self.vx = random.randint(-VMAX, VMAX)
        self.vy = random.randrange(-VMAX, VMAX)

    def update(self, click):
        global points
        self.rect = self.rect.move(self.vx, self.vy)
        if click is not None and \
                abs(self.rect.centerx - event.pos[0]) <= self.rect.width and \
                abs(self.rect.centery - event.pos[1]) <= self.rect.width:
            points += 2
            self.kill()
            add_square()
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    """
        вертикальная или горизонтальная граница
        нужна чтобы спрайты не разлетались
    """
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def add_ball():
    maxR = 70
    minR = 30
    x = random.randint(0, WINDOW_WIDTH - 2 * maxR)
    y = random.randint(0, WINDOW_HEIGHT - 2 * maxR)
    r = random.randint(minR, maxR)
    Ball(r, x, y)


def add_square():
    maxWidth = 120
    minWidth = 40
    x = random.randint(0, WINDOW_WIDTH - maxWidth)
    y = random.randint(0, WINDOW_HEIGHT - maxWidth)
    width = random.randint(minWidth, maxWidth)
    Square(width, x, y)

def draw_scores():
    with open("record.txt", "r", encoding="utf8") as f:
        scores = [line.strip("\n") for line in f.readlines()]
    text = ["HIGH SCORES"] + scores

    font = pygame.font.Font(None, 30)
    text_coord = 20
    for line in text:
        string_rendered = font.render(line, 1, pygame.Color('#fff500'))
        line_rect = string_rendered.get_rect()
        text_coord += 5
        line_rect.top = text_coord
        line_rect.x = 30
        text_coord += line_rect.height
        screen.blit(string_rendered, line_rect)


def save_score(points):
    with open("record.txt", "r", encoding="utf8") as f:
        scores = [int(line.strip("\n")) for line in f.readlines()]
    scores.append(points)
    scores = sorted(set(scores), reverse=True)[:4]
    with open("record.txt", "w", encoding="utf8") as f:
        f.write("\n".join([str(s) for s in scores]))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0

all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

Border(5, 5, WINDOW_WIDTH - 5, 5)
Border(5, WINDOW_HEIGHT - 5, WINDOW_WIDTH - 5, WINDOW_HEIGHT - 5)
Border(5, 5, 5, WINDOW_HEIGHT - 5)
Border(WINDOW_WIDTH - 5, 5, WINDOW_WIDTH - 5, WINDOW_HEIGHT - 5)

for _ in range(3):
    add_ball()

for _ in range(3):
    add_square()

while not finished:
    click = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            save_score(points)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = event

    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_sprites.update(click)
    draw_scores()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
