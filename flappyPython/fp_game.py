import pygame
import time

from flappyPython.fp_constants import *
from flappyPython.fp_player import FpPlayer
from flappyPython.fp_image import FpImage
from flappyPython.fp_message import FpMessage
from flappyPython.fp_events import FpEvents
from flappyPython.fp_score import FpScore


def replay_or_quit_game():
    events = FpEvents()

    if events.is_key_pressed():
        return True

    return False


def draw_game_over_text(screen):
    game_over_text = FpMessage(
        "Game Over",
        80,
        [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2],
        "center",
        FONT_SUPER_MARIO_256_SRC,
        WHITE
    )

    game_over_text.draw(screen)


def draw_continue_text(screen):
    continue_text = FpMessage(
        "Press any key to continue",
        20,
        [SCREEN_WIDTH / 2, ((SCREEN_HEIGHT / 2) + 100)],
        "center",
        FONT_SUPER_MARIO_256_SRC,
        WHITE
    )

    continue_text.draw(screen)


def game_over_screen(clock, screen):
    draw_game_over_text(screen)

    draw_continue_text(screen)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit_game() == False:
        clock.tick()

    main()


def player_hits_boundary(player):
    return player.get_pos_y() > (SCREEN_HEIGHT - PLAYER_IMG_WIDTH) or player.get_pos_y() < 0


def player_hits_pipes(player, pipe_top):
    if player.pos_x + PLAYER_IMG_WIDTH > pipe_top.get_pos_left():
        # Pipe top
        if player.pos_x < pipe_top.get_pos_left() + PIPES_WIDTH:
            if player.pos_y < pipe_top.get_height():
                if player.pos_x - PLAYER_IMG_WIDTH < PIPES_WIDTH + pipe_top.get_pos_left():
                    return True
        # Pipe bottom
        if player.pos_y + PLAYER_IMG_HEIGHT > pipe_top.get_height() + PIPES_GAP:
            if player.pos_x < PIPES_WIDTH + pipe_top.get_pos_left():
                return True

    return False


def player_passed_pipes(player, pipe_top):
    return player.pos_x < pipe_top.get_pos_right() and player.pos_x > pipe_top.get_pos_right() + PIPES_SPEED


def set_pipe_top_random_pos_top(pipe_top):
    pipe_top.set_pos_top(randint(0, SCREEN_HEIGHT - PIPES_GAP) - PIPES_HEIGHT)


def get_pipe_bottom_y(pipe_top_y):
    return pipe_top_y + PIPES_HEIGHT + PIPES_GAP


def adjust_pipe_bottom_y(pipe_bottom, pipe_top):
    pipe_bottom.set_pos_top(get_pipe_bottom_y(pipe_top.get_pos_top()))


def main():
    # -------
    # SETUP
    # -------

    # general setup
    pygame.init()
    pygame.display.set_caption(FP_TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # background
    bg_sky = pygame.image.load(BG_SKY_SRC).convert()

    bg_clouds_img = pygame.image.load(BG_CLOUDS_SRC).convert_alpha()
    bg_clouds_first = FpImage(0, 0, BG_CLOUDS_SPEED, bg_clouds_img)
    bg_clouds_second = FpImage(SCREEN_WIDTH, 0, BG_CLOUDS_SPEED, bg_clouds_img)

    bg_ground_img = pygame.image.load(BG_GROUND_SRC).convert_alpha()
    bg_ground_first = FpImage(0, 0, BG_GROUND_SPEED, bg_ground_img)
    bg_ground_second = FpImage(SCREEN_WIDTH, 0, BG_GROUND_SPEED, bg_ground_img)

    bg_moving_objects = [
        bg_clouds_first,
        bg_clouds_second,
        bg_ground_first,
        bg_ground_second,
    ]

    # pipes
    pipe_top_img = pygame.image.load(PIPE_TOP_SRC).convert_alpha()
    pipe_top = FpImage(SCREEN_WIDTH, INIT_PIPE_TOP_Y, PIPES_SPEED, pipe_top_img)

    pipe_bottom_img = pygame.image.load(PIPE_BOTTOM_SRC).convert_alpha()
    pipe_bottom = FpImage(SCREEN_WIDTH, get_pipe_bottom_y(INIT_PIPE_TOP_Y), PIPES_SPEED, pipe_bottom_img)

    # player
    player = FpPlayer()

    # events
    events = FpEvents()

    # score
    score = FpScore(0)
    score.draw(screen)

    game_over_state = False

    # -------
    # GAME LOOP
    # -------

    while not game_over_state:
        # set to 60 fps
        clock.tick(FRAMES_PER_SECOND)

        # handle user events
        events.handle_user_input(player)

        # -------
        # DRAWING
        # -------

        # background
        screen.blit(bg_sky, BG_SKY_POS)
        for o in bg_moving_objects:
            o.move()
            o.draw(screen)

        # player
        player.draw(screen)

        # pipes
        pipe_top.move()
        pipe_top.draw(screen)
        pipe_bottom.move()
        pipe_bottom.draw(screen)

        # score
        score.draw(screen)

        # scene
        pygame.display.update()

        # -------
        # REPEAT
        # -------

        if pipe_top.pos.left == SCREEN_WIDTH:
            set_pipe_top_random_pos_top(pipe_top)
            adjust_pipe_bottom_y(pipe_bottom, pipe_top)

        # -------
        # INCREASE SCORE
        # -------

        if player_passed_pipes(player, pipe_top):
            score.increase(1)

        # -------
        # GAME OVER
        # -------

        if player_hits_boundary(player) or player_hits_pipes(player, pipe_top):
            game_over_screen(clock, screen)


main()
pygame.quit()
quit()
