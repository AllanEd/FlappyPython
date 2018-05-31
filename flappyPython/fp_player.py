import pygame
from flappyPython.fp_constants import *


class FpPlayer(object):
    def __init__(self):
        self.pos_x = INIT_PLAYER_POS_X
        self.pos_y = INIT_PLAYER_POS_Y
        self.move_now = INIT_PLAYER_SPEED
        self.move_up_speed = PLAYER_SPEED_UP
        self.move_down_speed = PLAYER_SPEED_DOWN
        self.img = pygame.image.load(PLAYER_IMG_SRC).convert_alpha()

    def move_up(self):
        self.move_now = self.move_up_speed

    def move_down(self):
        self.move_now = self.move_down_speed

    def draw(self, screen):
        self.pos_y += self.move_now
        screen.blit(self.img, (self.pos_x, self.pos_y))

    def hits_boundary(self):
        return self.pos_y > (SCREEN_HEIGHT - PLAYER_IMG_WIDTH) or self.pos_y < 0

    def hits_pipes(self, pipe_top):
        if self.pos_x + PLAYER_IMG_WIDTH > pipe_top.get_pos_left():
            # Pipe top
            if self.pos_x < pipe_top.get_pos_left() + PIPES_WIDTH:
                if self.pos_y < pipe_top.get_height():
                    if self.pos_x - PLAYER_IMG_WIDTH < PIPES_WIDTH + pipe_top.get_pos_left():
                        return True
            # Pipe bottom
            if self.pos_y + PLAYER_IMG_HEIGHT > pipe_top.get_height() + PIPES_GAP:
                if self.pos_x < PIPES_WIDTH + pipe_top.get_pos_left():
                    return True

        return False