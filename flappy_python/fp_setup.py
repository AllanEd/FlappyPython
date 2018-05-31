import pygame

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

# -------
# SETUP
# -------

# general setup
pygame.init()
pygame.display.set_caption(t.TITLE)
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
clock = pygame.time.Clock()

# background
bg_sky = pygame.image.load(p.BG_SKY).convert()

bg_clouds_img = pygame.image.load(p.BG_CLOUDS).convert_alpha()
bg_clouds_first = FpImage(0, 0, c.BG_CLOUDS_SPEED, bg_clouds_img)
bg_clouds_second = FpImage(c.SCREEN_WIDTH, 0, c.BG_CLOUDS_SPEED, bg_clouds_img)

bg_ground_img = pygame.image.load(p.BG_GROUND).convert_alpha()
bg_ground_first = FpImage(0, 0, c.BG_GROUND_SPEED, bg_ground_img)
bg_ground_second = FpImage(c.SCREEN_WIDTH, 0, c.BG_GROUND_SPEED, bg_ground_img)

bg_moving_objects = [
    bg_clouds_first,
    bg_clouds_second,
    bg_ground_first,
    bg_ground_second,
]

# pipes
pipe_top_img = pygame.image.load(p.PIPE_TOP).convert_alpha()
pipe_top = FpPipe(c.SCREEN_WIDTH, c.INIT_PIPE_TOP_Y, c.PIPES_SPEED, pipe_top_img)

pipe_bottom_img = pygame.image.load(p.PIPE_BOTTOM).convert_alpha()
pipe_bottom = FpPipe(
    c.SCREEN_WIDTH,
    pipe_top.get_recalculated_bottom_y(pipe_top),
    c.PIPES_SPEED, pipe_bottom_img
)

# player
player = FpPlayer()

# events
events = FpEvents()

# score
score = FpScore(0)
score.draw(screen)

game_over_state = False
