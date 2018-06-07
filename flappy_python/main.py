# setup
from flappy_python.classes.fp_setup import FpSetup


def main(pygame):
    """Runs the game.
    
    Implements the game loops(2), sets the frames per second(2)
    handles the user input(3), draws and moves the elements(4),
    updates the display(5) increases the score(6) and handles
    game over(7).
    
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

        # 4. Drawing/moving
        s.draw_and_move_bg()
        s.draw_player()
        s.draw_and_move_pipes()
        s.draw_score()

        # 5. Updating display
        s.update_display()

        # 6. Increase score
        if s.player_passes_pipes():
            s.increase_score()

        # 7. Game over
        if s.player_hits_boundary_or_pipes():
            s.show_game_over_screen(main)
