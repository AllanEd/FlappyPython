import pygame
import time

from flappyPython.fp_constants import *
from flappyPython.fp_player import *
from flappyPython.fp_block import *

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


def msg_screen(text, size, position, screen):
    font = pygame.font.Font('freesansbold.ttf', size)
    title_text_screen, title_text_rect = make_text_objs(text, font)
    title_text_rect.center = position

    screen.blit(title_text_screen, title_text_rect)


def game_over_screen(text, clock, screen):
    game_over_text_position = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    msg_screen("Game Over!", 100, game_over_text_position, screen)

    continue_text_position = SCREEN_WIDTH / 2, ((SCREEN_HEIGHT / 2) + 100)
    msg_screen("Press any key to continue", 20, continue_text_position, screen)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit_game():
        clock.tick()

    main()


def game_over(clock, screen):
    game_over_screen("Game Over!", clock, screen)


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


def main():
    # general setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(FP_TITLE)
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

    # game loop
    while not game_over_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_state = True

            if (ifKeyUpIsDown(event)):
                fp_player.move_up()

            if (ifKeyUpIsUp(event)):
                fp_player.move_down()

        # fills background
        screen.fill(BLACK)

        fp_player.draw(screen)

        fp_block_top.draw(screen)
        fp_block_top.move()

        fp_block_bottom.draw(screen)
        fp_block_bottom.move()

        # quits game if user hits bottom or top screen
        if fp_player.get_pos_y() > (SCREEN_HEIGHT - FP_PLAYER_IMG_WIDTH) or fp_player.get_pos_y() < 0:
            game_over(clock, screen)

        # draw the scene
        pygame.display.update()

        # set to 60 fps
        clock.tick(FRAMES_PER_SECOND)


main()
quit_game()
