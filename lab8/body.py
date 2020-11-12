import pygame

G = 1


class Body(pygame.sprite.Sprite):
    """
    Represents planets and stars.
    """
    def __init__(self, group, mass, pos, vel, radius, color=pygame.Color("#2aff00")):
        """
        Creates a body with given parameters, adds it to the group of bodies.
        """
        super().__init__(group)
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.color = color

        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), radius)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        """
        Calculates forces on the body and moves it.
        """
        pass
