# constants
from flappy_python import fp_constants as c
# resources
from flappy_python.resources import paths as p
from flappy_python.resources import texts as t
# classes
from flappy_python.classes.fp_player import FpPlayer
from flappy_python.classes.fp_image import FpImage
from flappy_python.classes.fp_events import FpEvents
from flappy_python.classes.fp_pipe import FpPipe
from flappy_python.classes.fp_score import FpScore


class FpSetup:
    def __init__(self, pygame):
        # general setup
        self.pygame = pygame
        self.pygame.init()
        self.pygame.display.set_caption(t.TITLE)
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # background
        __bg_sky_img = self.pygame.image.load(p.BG_SKY).convert()
        self.bg_sky = FpImage(0, 0, 0, __bg_sky_img)

        __bg_clouds_img = self.pygame.image.load(p.BG_CLOUDS).convert_alpha()
        __bg_clouds_first = FpImage(0, 0, c.BG_CLOUDS_SPEED, __bg_clouds_img)
        __bg_clouds_second = FpImage(c.SCREEN_WIDTH, 0, c.BG_CLOUDS_SPEED, __bg_clouds_img)

        __bg_ground_img = self.pygame.image.load(p.BG_GROUND).convert_alpha()
        __bg_ground_first = FpImage(0, 0, c.BG_GROUND_SPEED, __bg_ground_img)
        __bg_ground_second = FpImage(c.SCREEN_WIDTH, 0, c.BG_GROUND_SPEED, __bg_ground_img)

        self.bg_moving_objects = [
            __bg_clouds_first,
            __bg_clouds_second,
            __bg_ground_first,
            __bg_ground_second,
        ]

        # pipes
        __pipe_top_img = self.pygame.image.load(p.PIPE_TOP).convert_alpha()
        self.pipe_top = FpPipe(
            c.INIT_PIPE_TOP_Y,
            __pipe_top_img
        )

        __pipe_bottom_img = self.pygame.image.load(p.PIPE_BOTTOM).convert_alpha()
        self.pipe_bottom = FpPipe(
            FpPipe.calculate_pipe_bottom_y(self.pipe_top),
            __pipe_bottom_img
        )

        # player
        self.player = FpPlayer()

        # events
        self.events = FpEvents()

        # score
        self.score = FpScore(c.SCORE_START_POINTS)

        # game over state
        self.is_game_over = False
