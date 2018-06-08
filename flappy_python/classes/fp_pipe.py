from random import randint

from flappy_python import fp_constants as c
from flappy_python.classes.fp_image import FpImage


class FpPipe(FpImage):
    """Creates a flappy python pipe.

    A pipe is an obstacle that inherits from an flappy python image.

    Attributes:
        y: An integer for the pipes y position.
        image: A pygame Surface object that holds the image.
    """

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

    def set_recalculated_pipe_bottom_y(self, pipe_top):
        recalculated_bottom_y = self.calculate_pipe_bottom_y(pipe_top)
        self.pos.top = recalculated_bottom_y

    def move(self, pipe_top=None):
        self.pos = self.pos.move(self.speed, 0)

        if self.pos.right <= 0:
            self.pos.left = c.SCREEN_WIDTH

            if (pipe_top):
                self.set_recalculated_pipe_bottom_y(pipe_top)
            else:
                self.set_random_pos_top()

    @staticmethod
    def calculate_pipe_bottom_y(pipe_top):
        return pipe_top.get_pos_top() + c.PIPES_HEIGHT + c.PIPES_GAP
