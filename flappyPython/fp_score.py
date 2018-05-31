from flappyPython.fp_message import FpMessage
from flappyPython.fp_constants import *


class FpScore(object):
    def __init__(self, score):
        self.score = score

    def increase(self, points):
        self.score += points

    def draw(self, screen):
        score_text = FpMessage(
            str(self.score),
            50,
            [SCREEN_WIDTH / 2, 50],
            "center",
            FONT_SUPER_MARIO_256_SRC,
            WHITE
        )
        score_text.draw(screen)
