from random import randint

from flappyPython import fp_constants as c
from flappyPython.fp_image import FpImage


class FpPipe(FpImage):

    def __init__(self, x, y, speed, image):
        FpImage.__init__(self, x, y, speed, image)

    def get_pos_top(self):
        return self.pos.top

    def set_pos_top(self, top):
        self.pos.top = top

    def get_pos_left(self):
        return self.pos.left

    def get_pos_right(self):
        return self.pos.right

    def get_height(self):
        return self.pos.top + c.PIPES_HEIGHT

    def player_passed_pipes(self, player):
        return player.pos_x < self.get_pos_right() and player.pos_x > self.get_pos_right() + c.PIPES_SPEED

    def set_random_pos_top(self):
        self.set_pos_top(randint(0, c.SCREEN_HEIGHT - c.PIPES_GAP) - c.PIPES_HEIGHT)

    def get_recalculated_bottom_y(self, pipe_top):
        return pipe_top.get_pos_top() + c.PIPES_HEIGHT + c.PIPES_GAP

    def set_recalculated_bottom_y(self, pipe_top):
        recalculated_bottom_y = self.get_recalculated_bottom_y(pipe_top)
        self.set_pos_top(recalculated_bottom_y)
