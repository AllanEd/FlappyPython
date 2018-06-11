# setup
from flappy_python.classes.fp_setup import FpSetup


def main(pygame):
    """Runs the game.
    
    Implements the game loops(2), sets the frames per second(2)
    handles the user input(3), draws(4) and moves(5) the elements,
    updates the display(6) increases the score(7) and handles
    game over(8).
    
    Args:
        pygame: The current pygame module instance.
    """

    s = FpSetup(pygame)

    # 1. Game loop
    while s.game_loop():
        # 2. Frames per second
        s.set_frames_per_second()

        # 3. User input
        s.handle_user_input()

        # 4. Drawing
        s.draw_bg()
        s.draw_player()
        s.draw_pipes()
        s.draw_score()

        # 5. Moving
        s.move_bg()
        s.move_pipes()

        # 6. Updating display
        s.update_display()

        # 7. Increase score
        if s.player_passes_pipes():
            s.increase_score()

        # 8. Game over
        if s.player_hits_boundary_or_pipes():
            s.show_game_over_screen(main)
