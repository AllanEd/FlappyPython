# Setup
from flappy_python.fp_setup import *
# constants
from flappy_python import fp_constants as c
# helper for game over
from flappy_python.helper import fp_game_over


def main():
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
