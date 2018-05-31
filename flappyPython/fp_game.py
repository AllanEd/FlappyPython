import pygame

from flappyPython import fp_constants as c
from flappyPython import fp_game_over
from flappyPython.fp_player import FpPlayer
from flappyPython.fp_image import FpImage
from flappyPython.fp_events import FpEvents
from flappyPython.fp_pipe import FpPipe
from flappyPython.fp_score import FpScore


def main():
    # -------
    # SETUP
    # -------

    # general setup
    pygame.init()
    pygame.display.set_caption(c.FP_TITLE)
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # background
    bg_sky = pygame.image.load(c.BG_SKY_SRC).convert()

    bg_clouds_img = pygame.image.load(c.BG_CLOUDS_SRC).convert_alpha()
    bg_clouds_first = FpImage(0, 0, c.BG_CLOUDS_SPEED, bg_clouds_img)
    bg_clouds_second = FpImage(c.SCREEN_WIDTH, 0, c.BG_CLOUDS_SPEED, bg_clouds_img)

    bg_ground_img = pygame.image.load(c.BG_GROUND_SRC).convert_alpha()
    bg_ground_first = FpImage(0, 0, c.BG_GROUND_SPEED, bg_ground_img)
    bg_ground_second = FpImage(c.SCREEN_WIDTH, 0, c.BG_GROUND_SPEED, bg_ground_img)

    bg_moving_objects = [
        bg_clouds_first,
        bg_clouds_second,
        bg_ground_first,
        bg_ground_second,
    ]

    # pipes
    pipe_top_img = pygame.image.load(c.PIPE_TOP_SRC).convert_alpha()
    pipe_top = FpPipe(c.SCREEN_WIDTH, c.INIT_PIPE_TOP_Y, c.PIPES_SPEED, pipe_top_img)

    pipe_bottom_img = pygame.image.load(c.PIPE_BOTTOM_SRC).convert_alpha()
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

    # -------
    # GAME LOOP
    # -------

    while not game_over_state:
        # set to 60 fps
        clock.tick(c.FRAMES_PER_SECOND)

        # handle user events
        events.handle_user_input(player)

        # -------
        # DRAWING
        # -------

        # background
        screen.blit(bg_sky, c.BG_SKY_POS)
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

        if pipe_top.pos.left == c.SCREEN_WIDTH:
            pipe_top.set_random_pos_top()
            pipe_bottom.set_recalculated_bottom_y(pipe_top)

        # -------
        # INCREASE SCORE
        # -------

        if pipe_top.player_passed_pipes(player):
            score.increase(1)

        # -------
        # GAME OVER
        # -------

        if player.hits_boundary() or player.hits_pipes(pipe_top):
            fp_game_over.game_over_screen(pygame, clock, screen, main)


main()
pygame.quit()
quit()
