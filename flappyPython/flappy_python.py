import pygame
import time
from random import randint

from flappyPython.fp_player import *

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

FP_TITLE = 'Flappy Python'

FP_PLAYER_IMG_SRC = 'assets/flappy_python_player.png'
FP_PLAYER_IMG_WIDTH = 100
FP_PLAYER_IMG_HEIGHT = 100

INIT_FP_PLAYER_POS_X = 100
INIT_FP_PLAYER_POS_Y = 100
INIT_FP_PLAYER_SPEED = 0  # initial speed 0 => no move

FP_PLAYER_SPEED_UP = -5
FP_PLAYER_SPEED_DOWN = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FRAMES_PER_SECOND = 60

# flappy python player initial values
fp_player = FpPlayer(
    INIT_FP_PLAYER_POS_X,  # starting position
    INIT_FP_PLAYER_POS_Y,
    INIT_FP_PLAYER_SPEED,
    FP_PLAYER_SPEED_UP,
    FP_PLAYER_SPEED_DOWN,
    pygame.image.load(FP_PLAYER_IMG_SRC)
)

# general setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(FP_TITLE)
clock = pygame.time.Clock()


def draw_blocks(pos_x, pos_y, width, height, gap):
    block_top_dimensions = [pos_x, pos_y, width, height]
    block_bottom_pos_y = pos_y + height + gap
    block_bottom_height = SCREEN_HEIGHT - block_bottom_pos_y
    block_bottom_dimensions = [pos_x, block_bottom_pos_y, width, block_bottom_height]

    pygame.draw.rect(screen, WHITE, block_top_dimensions)
    pygame.draw.rect(screen, WHITE, block_bottom_dimensions)


def replay_or_quit_game():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            quit_game()

        elif event.type == pygame.KEYDOWN:
            continue

    return None


def make_text_objs(text, font):
    text_screen = font.render(text, True, WHITE)
    return text_screen, text_screen.get_rect()


def msg_screen(text, size, position):
    font = pygame.font.Font('freesansbold.ttf', size)
    title_text_screen, title_text_rect = make_text_objs(text, font)
    title_text_rect.center = position

    screen.blit(title_text_screen, title_text_rect)


def game_over_screen(text):
    game_over_text_position = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    msg_screen("Game Over!", 100, game_over_text_position)

    continue_text_position = SCREEN_WIDTH / 2, ((SCREEN_HEIGHT / 2) + 100)
    msg_screen("Press any key to continue", 20, continue_text_position)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit_game():
        clock.tick()

    main()


def game_over():
    game_over_screen("Game Over!")


def quit_game():
    pygame.quit()
    quit()


def fp_player_set(x, y, image):
    screen.blit(fp_player.get_img(), (x, y))


def ifKeyUpIsDown(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            return True


def ifKeyUpIsUp(event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            return True


def main():
    # initial values
    fp_player.set_pos_x(INIT_FP_PLAYER_POS_X)
    fp_player.set_pos_y(INIT_FP_PLAYER_POS_Y)
    fp_player.set_move_now(INIT_FP_PLAYER_SPEED)

    x_block = SCREEN_WIDTH
    y_block = 0
    block_width = 75
    gap = FP_PLAYER_IMG_HEIGHT * 2
    block_height = randint(0, SCREEN_HEIGHT - gap)
    block_move = 3

    game_over_state = False

    # game loop
    while not game_over_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_state = True

            if (ifKeyUpIsDown(event)):
                fp_player.set_move_now(fp_player.get_move_up())

            if (ifKeyUpIsUp(event)):
                fp_player.set_move_now(fp_player.get_move_down())

        fp_player.add_pos_y(fp_player.get_move_now())

        # fills background
        screen.fill(BLACK)
        # add flappy python
        fp_player_set(fp_player.get_pos_x(), fp_player.get_pos_y(), fp_player.get_img())

        draw_blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move

        # quits game if user hits bottom or top screen
        if fp_player.get_pos_y() > (SCREEN_HEIGHT - FP_PLAYER_IMG_WIDTH) or fp_player.get_pos_y() < 0:
            game_over()

        # update() => updates specific areas in the screen
        pygame.display.update()
        # set to 60 fps
        clock.tick(FRAMES_PER_SECOND)


main()
quit_game()
