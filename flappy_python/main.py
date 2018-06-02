# Setup
from flappy_python.classes.fp_setup import FpSetup
# constants
from flappy_python import fp_constants as c
# helper for game over
from flappy_python.helper import fp_game_over


def main(pygame):
    # create a new setup instance
    s = FpSetup(pygame)

    # -------
    # GAME LOOP
    # -------

    while not s.is_game_over:
        # set the fps
        s.clock.tick(c.FRAMES_PER_SECOND)

        # handle user events
        s.events.handle_user_input(s.player)

        # -------
        # DRAWING
        # -------

        # background
        s.bg_sky.draw(s.screen)
        for o in s.bg_moving_objects:
            o.move()
            o.draw(s.screen)

        # player
        s.player.draw(s.screen)

        # pipes
        s.pipe_top.move()
        s.pipe_top.draw(s.screen)
        s.pipe_bottom.move()
        s.pipe_bottom.draw(s.screen)

        # score
        s.score.draw(s.screen)

        # scene
        s.pygame.display.update()

        # -------
        # REPEAT
        # -------

        if s.pipe_top.pos.left == c.SCREEN_WIDTH:
            s.pipe_top.set_random_pos_top()
            s.pipe_bottom.set_recalculated_pipe_bottom_y(s.pipe_top)

        # -------
        # INCREASE SCORE
        # -------

        if s.pipe_top.player_passed_pipes(s.player):
            s.score.increase(c.SCORE_INCREASE_POINTS)

        # -------
        # GAME OVER
        # -------

        if s.player.hits_boundary() or s.player.hits_pipes(s.pipe_top):
            fp_game_over.display_game_over_screen(s.pygame, s.clock, s.screen, main)
