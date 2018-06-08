import pygame
# constants
from flappy_python import fp_constants as c


class FpImage(pygame.sprite.Sprite):
    """Creates pygame sprite.

    FpImage inherits from pygames sprite class. This is a simple
    base class for visible game objects.

    Attributes:
        x: An integer for the game objects/image x position.
        y: An integer for the game objects/image y position.
        speed: An integer for the game objects speed.
        image: A pygame Surface object that holds the game objects image.
    """

    def __init__(self, x, y, speed, image):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.image = image
        self.rect = image.get_rect()
        self.pos = self.rect.move(x, y)

    def move(self):
        self.pos = self.pos.move(self.speed, 0)

        if self.pos.right <= 0:
            self.pos.left = c.SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.pos)
