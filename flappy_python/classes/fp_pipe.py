from random import randint

from flappy_python import fp_constants as c
from flappy_python.classes.fp_image import FpImage


class FpPipe(FpImage):
    x = c.SCREEN_WIDTH
    speed = c.PIPES_SPEED

    def __init__(self, y, image):
        FpImage.__init__(self, FpPipe.x, y, FpPipe.speed, image)

    def get_pos_top(self):
        return self.pos.top

    def get_pos_left(self):
        return self.pos.left

    def get_height(self):
        return self.pos.top + c.PIPES_HEIGHT

    def player_passed_pipes(self, player):
        return player.get_pos_x() < self.pos.right and player.get_pos_x() > self.pos.right + c.PIPES_SPEED

    def set_random_pos_top(self):
        self.pos.top = randint(0, c.SCREEN_HEIGHT - c.PIPES_GAP) - c.PIPES_HEIGHT

    @staticmethod
    def calculate_pipe_bottom_y(pipe_top):
        return pipe_top.get_pos_top() + c.PIPES_HEIGHT + c.PIPES_GAP

    def set_recalculated_pipe_bottom_y(self, pipe_top):
        recalculated_bottom_y = self.calculate_pipe_bottom_y(pipe_top)
        self.pos.top = recalculated_bottom_y
