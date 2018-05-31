# constants
from flappyPython import fp_constants as c
# resources
from flappyPython.resources import paths as p
from flappyPython.resources import texts as t
# classes
from flappyPython.fp_message import FpMessage


class FpScore(object):
    def __init__(self, score):
        self.score = score

    def increase(self, points):
        self.score += points

    def draw(self, screen):
        score_text = FpMessage(
            str(self.score),
            50,
            [c.SCREEN_WIDTH / 2, 50],
            t.CENTER,
            p.SUPER_MARIO_256,
            c.WHITE
        )
        score_text.draw(screen)
