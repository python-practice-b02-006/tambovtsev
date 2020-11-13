import pygame
import numpy as np

G = 1


class Body(pygame.sprite.Sprite):
    """
    Represents planets and stars.
    """
    def __init__(self, group, mass, pos, vel, radius, color="#2aff00"):
        """
        Creates a body with given parameters, adds it to the group of bodies.
        """
        super().__init__(group)
        self.mass = mass
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.accel = np.zeros(2, dtype=float)
        self.radius = radius
        self.color = pygame.Color(color)

        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), radius)
        self.rect = self.image.get_rect(center=self.pos)

    def calculate_acceleration(self, bodies):
        """
        Calculates acceleration of the body.
        """
        self.accel = np.zeros(2, dtype=float)

        for body in bodies:
            distance = (np.sum((self.pos - body.pos) ** 2)) ** 0.5

            # the ball doesn't act on itself and infinite force is bad.
            if distance == 0:
                continue

            self.accel += G * body.mass * (body.pos - self.pos) / (np.linalg.norm(body.pos - self.pos) * distance**2)

    def update(self, window_size, dt=1.):
        """
        Moves the body.
        """
        self.pos += self.vel * dt
        self.vel += self.accel * dt

        self.rect = self.image.get_rect(center=self.pos.astype(int))

        if self.pos[0] > 2 * window_size[0] or self.pos[0] < - window_size[0] or\
                self.pos[1] > 2 * window_size[1] or self.pos[1] < - window_size[1]:
            self.kill()
