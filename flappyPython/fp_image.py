import pygame
from flappyPython.fp_constants import *


class FpImage(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, x, y, speed, image):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.image = image
        self.rect = image.get_rect()
        self.pos = self.rect.move(x, y)

    def get_pos_top(self):
        return self.pos.top

    def set_pos_top(self, top):
        self.pos.top = top

    def get_pos_left(self):
        return self.pos.left

    def get_pos_right(self):
        return self.pos.right

    def get_height(self):
        return self.pos.top + PIPES_HEIGHT

    def move(self):
        self.pos = self.pos.move(self.speed, 0)

        if self.pos.right < 0:
            self.pos.left = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.pos)
