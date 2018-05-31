import pygame
from flappyPython.fp_constants import *


class FpBlock(object):
    def __init__(self, pos_y, height):
        self.rect = pygame.rect.Rect((
            INIT_FP_BLOCKS_POS_X,
            pos_y,
            FP_BLOCKS_WIDTH,
            height
        ))
        self.color = FP_BLOCKS_BG_COLOR
        self.speed = FP_BLOCKS_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        self.rect.move_ip(-self.speed, 0)
