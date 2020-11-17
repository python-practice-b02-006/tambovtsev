import pygame
import os


class Slider(pygame.sprite.Sprite):
    """
    Slider will change the velocity (dt).
    """
    def __init__(self, group):
        super().__init__(group)
        self.width = 20
        self.height = 420
        self.slider_y = self.height // 2
        self.step = 20
        self.color = pygame.Color("#828282")

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(10, 10))
        self.draw_slider()

    def draw_slider(self):
        self.image.fill(self.color)
        rect = pygame.Rect((0, 0, self.width, self.width))
        rect.centery = self.slider_y
        pygame.draw.rect(self.image, pygame.Color("red"), rect)

    def calc_value(self):
        return 0.1 * (1 - self.slider_y / self.height)

    def update(self, event):
        self.draw_slider()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and \
               self.slider_y - self.step - self.width // 2 >= 0:
                self.slider_y -= self.step
            if event.key == pygame.K_DOWN and \
               self.slider_y + self.step + self.width // 2 <= self.height:
                self.slider_y += self.step

            self.draw_slider()


class StartStop(pygame.sprite.Sprite):
    """
    This button will start and stop updating the system.
    """
    def __init__(self, group):
        super().__init__(group)
        self.side = 50
        self.on = False

        self.image = pygame.Surface((self.side, self.side), pygame.SRCALPHA)
        fullname = os.path.join(os.path.dirname(__file__), 'images', "play_pause.png")
        image = pygame.image.load(fullname).convert()
        image = pygame.transform.scale(image, (self.side, self.side))
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(center=(30, 470))
        pygame.draw.rect(self.image, pygame.Color("white"), (0, 0, self.side, self.side), 1)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.on = not self.on
