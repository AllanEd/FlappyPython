from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FP_TITLE = 'Flappy Python'

PLAYER_IMG_SRC = 'assets/game_objects/player.png'
PLAYER_IMG_WIDTH = 100
PLAYER_IMG_HEIGHT = 100
PLAYER_SPEED_UP = -5
PLAYER_SPEED_DOWN = 5

INIT_PLAYER_POS_X = 100
INIT_PLAYER_POS_Y = 100
INIT_PLAYER_SPEED = 0  # initial speed 0 => no move

PIPES_HEIGHT = SCREEN_HEIGHT
PIPES_WIDTH = 75
PIPES_GAP = PLAYER_IMG_HEIGHT * 2
PIPES_SPEED = -6

PIPE_TOP_SRC = 'assets/game_objects/pipe_top.png'
INIT_PIPE_TOP_Y = randint(0, SCREEN_HEIGHT - PIPES_GAP) - PIPES_HEIGHT
PIPE_BOTTOM_SRC = 'assets/game_objects/pipe_bottom.png'

BG_SKY_SRC = 'assets/bg/sky.jpg'
BG_SKY_POS = (0, 0)
BG_CLOUDS_SRC = 'assets/bg/clouds.png'
BG_CLOUDS_SPEED = -2
BG_GROUND_SRC = 'assets/bg/ground.png'
BG_GROUND_SPEED = -1

FRAMES_PER_SECOND = 60
