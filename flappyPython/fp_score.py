from flappyPython import fp_constants as c
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
            "center",
            c.FONT_SUPER_MARIO_256_SRC,
            c.WHITE
        )
        score_text.draw(screen)
