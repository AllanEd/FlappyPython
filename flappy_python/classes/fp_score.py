# constants
from flappy_python import fp_constants as c
# resources
from flappy_python.resources import paths as p
from flappy_python.resources import texts as t
# classes
from flappy_python.classes.fp_message import FpMessage


class FpScore:
    """Creates the game score.

    Creates, increases and draws the game score.

    Attributes:
        score: An integer that holds the initial score.
    """
    def __init__(self, score):
        self.score = score

    def increase(self, points):
        self.score += points

    def draw(self, screen):
        score_text = FpMessage(
            str(self.score),
            c.SCORE_FONT_SIZE,
            [c.SCREEN_WIDTH / 2, 50],
            t.CENTER,
            p.SUPER_MARIO_256,
            c.WHITE
        )
        score_text.draw(screen)
