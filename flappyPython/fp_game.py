import pygame
import time

from flappyPython.fp_constants import *
from flappyPython.fp_player import FpPlayer
from flappyPython.fp_block import FpBlock
from flappyPython.fp_message import FpMessage
from flappyPython.fp_events import FpEvents


def replay_or_quit_game():
    fp_events = FpEvents()

    if fp_events.is_key_pressed():
        return True

    return False


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

    while replay_or_quit_game() == False:
        clock.tick()

    main()


def fp_player_hits_boundary(fp_player):
    return fp_player.get_pos_y() > (SCREEN_HEIGHT - FP_PLAYER_IMG_WIDTH) or fp_player.get_pos_y() < 0


def fp_player_hits_blocks(fp_player, fp_block_top):
    if fp_player.pos_x + FP_PLAYER_IMG_WIDTH > fp_block_top.rect.x:
        # Block top
        if fp_player.pos_x < fp_block_top.rect.x + fp_block_top.rect.width:
            if fp_player.pos_y < fp_block_top.rect.height:
                if fp_player.pos_x - FP_PLAYER_IMG_WIDTH < FP_BLOCKS_WIDTH + fp_block_top.rect.x:
                    return True
        # Block bottom
        if fp_player.pos_y + FP_PLAYER_IMG_HEIGHT > fp_block_top.rect.height + FP_BLOCKS_GAP:
            if fp_player.pos_x < FP_BLOCKS_WIDTH + fp_block_top.rect.x:
                return True

    return False


def fp_block_should_repeat(fp_block_top):
    return fp_block_top.rect.x < (0 - FP_BLOCKS_WIDTH)


def get_block_bottom_y(fp_block_top_height):
    return FP_BLOCKS_POS_Y + fp_block_top_height + FP_BLOCKS_GAP


def get_block_bottom_height(fp_block_top_height):
    return SCREEN_HEIGHT - get_block_bottom_y(fp_block_top_height)


def repeat_block_top(fp_block_top):
    fp_block_top.rect.x = SCREEN_WIDTH
    fp_block_top.rect.height = randint(0, SCREEN_HEIGHT - FP_BLOCKS_GAP)


def repeat_block_bottom(fp_block_bottom, fp_block_top):
    fp_block_bottom.rect.x = SCREEN_WIDTH
    fp_block_bottom.rect.y = get_block_bottom_y(fp_block_top.rect.height)
    fp_block_bottom.rect.height = get_block_bottom_height(fp_block_top.rect.height)


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
    fp_block_bottom = FpBlock(get_block_bottom_y(fp_block_top.rect.height),
                              get_block_bottom_height(fp_block_top.rect.height))
    fp_block_bottom.draw(screen)

    fp_events = FpEvents()

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
        fp_events.handle_user_input(fp_player)
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
        # REPEAT
        # -------

        if fp_block_should_repeat(fp_block_top):
            # block top
            repeat_block_top(fp_block_top)
            # block bottom
            repeat_block_bottom(fp_block_bottom, fp_block_top)

        # -------
        # GAME OVER
        # -------

        if fp_player_hits_boundary(fp_player) or fp_player_hits_blocks(fp_player, fp_block_top):
            game_over_screen("Game Over!", clock, screen)


main()
pygame.quit()
quit()
