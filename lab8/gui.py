import pygame


class Slider(pygame.sprite.Sprite):
    """
    Slider will change the velocity (dt).
    """
    def __init__(self, group):
        super().__init__(group)

    def update(self):
        pass


class StartStop(pygame.sprite.Sprite):
    """
    This button will start and stop updating the system.
    """
    def __init__(self, group):
        super().__init__(group)
        self.on = False

    def update(self):
        pass
