import pygame
from flappyPython.fp_constants import *


class FpImage(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, image):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.image = image
        self.rect = image.get_rect()
        self.pos = self.rect.move(x, y)

    def move(self):
        self.pos = self.pos.move(self.speed, 0)

        if self.pos.right < 0:
            self.pos.left = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.pos)
