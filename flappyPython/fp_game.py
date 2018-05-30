import pygame
import time

from flappyPython.fp_constants import *
from flappyPython.fp_player import *
from flappyPython.fp_block import *
from flappyPython.fp_message import *


def replay_or_quit_game():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            quit_game()

        elif event.type == pygame.KEYDOWN:
            continue

    return None


def draw_game_over_text(screen):
    game_over_text_position = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    game_over_text = FpMessage(
        "Game Over!",
        100,
        game_over_text_position
    )
    game_over_text.draw(screen)


def draw_continue_text(screen):
    continue_text_position = SCREEN_WIDTH / 2, ((SCREEN_HEIGHT / 2) + 100)
    continue_text = FpMessage(
        "Press any key to continue",
        20,
        continue_text_position
    )
    continue_text.draw(screen)


def game_over_screen(text, clock, screen):
    draw_game_over_text(screen)

    draw_continue_text(screen)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit_game():
        clock.tick()

    main()


def quit_game():
    pygame.quit()
    quit()


def ifKeyUpIsDown(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            return True


def ifKeyUpIsUp(event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            return True


def handle_user_events(fp_player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if (ifKeyUpIsDown(event)):
            fp_player.move_up()

        if (ifKeyUpIsUp(event)):
            fp_player.move_down()

        return True


def fp_player_hits_boundary(fp_player):
    return fp_player.get_pos_y() > (SCREEN_HEIGHT - FP_PLAYER_IMG_WIDTH) or fp_player.get_pos_y() < 0


def main():
    # -------
    # SETUP
    # -------

    # general setup
    pygame.init()
    pygame.display.set_caption(FP_TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # player
    fp_player = FpPlayer()
    # block top
    fp_block_top = FpBlock(FP_BLOCKS_POS_Y, FP_BLOCKS_HEIGHT)
    fp_block_top.draw(screen)
    # block bottom
    block_bottom_pos_y = FP_BLOCKS_POS_Y + FP_BLOCKS_HEIGHT + FP_BLOCKS_GAP
    block_bottom_height = SCREEN_HEIGHT - block_bottom_pos_y
    fp_block_bottom = FpBlock(block_bottom_pos_y, block_bottom_height)
    fp_block_bottom.draw(screen)

    game_over_state = False

    # -------
    # GAME LOOP
    # -------

    while not game_over_state:
        # set to 60 fps
        clock.tick(FRAMES_PER_SECOND)

        # -------
        # MOVING
        # -------

        # handle user events
        if handle_user_events(fp_player) == False:
            game_over_state = True
        # block top
        fp_block_top.move()
        # block bottom
        fp_block_bottom.move()

        # -------
        # DRAWING
        # -------

        # background
        screen.fill(BLACK)
        # player
        fp_player.draw(screen)
        # block top
        fp_block_top.draw(screen)
        # block bottom
        fp_block_bottom.draw(screen)
        # scene
        pygame.display.update()

        # -------
        # QUIT
        # -------

        if fp_player_hits_boundary(fp_player):
            game_over_screen("Game Over!", clock, screen)


main()
quit_game()
