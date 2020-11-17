import pygame
import numpy as np

G = 1


class Body(pygame.sprite.Sprite):
    """
    Represents a planet or a star.
    """

    def __init__(self, group, mass, pos, vel, radius, color="#2aff00"):
        """
        Creates a body with given parameters, adds it to the group of bodies.
        """
        self.mass = mass
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        super().__init__(group)
        self.radius = radius
        self.color = pygame.Color(color)

        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), radius)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, window_size):
        """
        Moves the image of the body.
        """
        self.rect = self.image.get_rect(center=self.pos.astype(int))

        if self.pos[0] > 2 * window_size[0] or self.pos[0] < - window_size[0] or \
                self.pos[1] > 2 * window_size[1] or self.pos[1] < - window_size[1]:
            self.kill()


class System(pygame.sprite.Group):
    """
    Represents the system of bodies.
    """
    def __init__(self, *bodies):
        """
        Creates a system from existing bodies.
        size - number of bodies in the system.
        pos, vel, mass - numpy arrays of positions, velocities and masses of all bodies in the system.
        """
        super().__init__(bodies)
        self.size = 0
        self.pos = np.zeros(1)
        self.vel = np.zeros(1)
        self.mass = np.zeros(1)
        self.get_state()

    def add_internal(self, body):
        """
        Adds a body to the system.
        """
        super().add_internal(body)
        self.get_state()

    def remove_internal(self, body):
        """
        Removes a body from the system.
        """
        super(System, self).remove_internal(body)
        self.get_state()

    def get_state(self):
        """
        Updates the size, position, velocities and masses of the system when bodies are added or removed.
        """
        self.size = len(self.sprites())
        self.pos = np.array([self.sprites()[i].pos for i in range(self.size)], dtype=float)
        self.vel = np.array([self.sprites()[i].vel for i in range(self.size)], dtype=float)
        self.mass = np.array([self.sprites()[i].mass for i in range(self.size)], dtype=float)

    def set_state(self):
        """
        Updates the states of each body in the system.
        """
        for i in range(self.size):
            self.sprites()[i].pos = self.pos[i]
            self.sprites()[i].vel = self.vel[i]

    def new_state(self, dt):
        """
        Uses Runge–Kutta method to calculate new state of the system as described here:
        https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods

        In our case:
         y = [*self.vel, *self.pos] - an array, containing velocities and positions of all bodies in the
        system.
         dy/dt = f(t, y) = f(y) = [self.calculate_acceleration(np.zeros(self.size)), self.vel], the first part of the
        array contains accelerations, the second part contains velocities.
        """
        k_1_vel = self.calculate_acceleration(np.zeros(self.size))
        k_1_pos = self.vel

        k_2_vel = self.calculate_acceleration(dt/2 * k_1_pos)
        k_2_pos = self.vel + dt/2 * k_1_vel

        k_3_vel = self.calculate_acceleration(dt/2 * k_2_pos)
        k_3_pos = self.vel + dt/2 * k_2_vel

        k_4_vel = self.calculate_acceleration(dt * k_3_pos)
        k_4_pos = self.vel + dt * k_3_vel

        self.pos += dt/6 * (k_1_pos + 2*k_2_pos + 2*k_3_pos + k_4_pos)
        self.vel += dt/6 * (k_1_vel + 2 * k_2_vel + 2 * k_3_vel + k_4_vel)

        self.set_state()

    def calculate_acceleration(self, dy):
        """
        Calculates acceleration using Newton's law.

        dy - a little change of y vector of the system (here only change of positions is used), it's needed for
         Runge-Kutta method.
        """
        accel = np.zeros((self.size, 2), dtype=float)

        for i in range(self.size):
            for j in range(self.size):
                # body doesn't act on itself
                if i == j:
                    continue
                r = self.pos[j] + dy[j] - (self.pos[i] + dy[i])
                accel[i] += G * self.mass[j] * r / np.linalg.norm(r)**3

        return accel
