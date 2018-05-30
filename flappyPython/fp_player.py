import pygame
from flappyPython.fp_constants import *


class FpPlayer(object):
    def __init__(self):
        self.pos_x = INIT_FP_PLAYER_POS_X
        self.pos_y = INIT_FP_PLAYER_POS_Y
        self.move_now = INIT_FP_PLAYER_SPEED
        self.move_up_speed = FP_PLAYER_SPEED_UP
        self.move_down_speed = FP_PLAYER_SPEED_DOWN
        self.img = pygame.image.load(FP_PLAYER_IMG_SRC).convert_alpha()

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def move_up(self):
        self.move_now = self.move_up_speed

    def move_down(self):
        self.move_now = self.move_down_speed

    def draw(self, screen):
        self.pos_y += self.move_now
        screen.blit(self.img, (self.pos_x, self.pos_y))
