import pygame

# constants
from flappyPython import fp_constants as c
# resources
from flappyPython.resources import paths as p


class FpPlayer(object):
    def __init__(self):
        self.pos_x = c.INIT_PLAYER_POS_X
        self.pos_y = c.INIT_PLAYER_POS_Y
        self.move_now = c.INIT_PLAYER_SPEED
        self.move_up_speed = c.PLAYER_SPEED_UP
        self.move_down_speed = c.PLAYER_SPEED_DOWN
        self.img = pygame.image.load(p.PLAYER_IMG).convert_alpha()

    def move_up(self):
        self.move_now = self.move_up_speed

    def move_down(self):
        self.move_now = self.move_down_speed

    def draw(self, screen):
        self.pos_y += self.move_now
        screen.blit(self.img, (self.pos_x, self.pos_y))

    def hits_boundary(self):
        return self.pos_y > (c.SCREEN_HEIGHT - c.PLAYER_IMG_WIDTH) or self.pos_y < 0

    def hits_pipes(self, pipe_top):
        if self.pos_x + c.PLAYER_IMG_WIDTH > pipe_top.get_pos_left():
            # Pipe top
            if self.pos_x < pipe_top.get_pos_left() + c.PIPES_WIDTH:
                if self.pos_y < pipe_top.get_height():
                    if self.pos_x - c.PLAYER_IMG_WIDTH < c.PIPES_WIDTH + pipe_top.get_pos_left():
                        return True
            # Pipe bottom
            if self.pos_y + c.PLAYER_IMG_HEIGHT > pipe_top.get_height() + c.PIPES_GAP:
                if self.pos_x < c.PIPES_WIDTH + pipe_top.get_pos_left():
                    return True

        return False
