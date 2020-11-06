import pygame

G = 1
class Body(pygame.sprite.Sprite):
    def __init__(self, group, mass, pos, v, radius, color=pygame.Color("#2aff00")):
        super().__init__(group)
        self.mass = mass
        self.pos = pos
        self.v = v
        self.radius = radius

    def update():
        pass