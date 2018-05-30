from flappyPython.fp_message import FpMessage


class FpScore(object):
    def __init__(self, score):
        self.score = score

    def increase(self, points):
        self.score += points

    def draw(self, screen):
        score_text = FpMessage(
            "Score:" + str(self.score),
            20,
            [0, 0],
            "topleft"
        )
        score_text.draw(screen)
