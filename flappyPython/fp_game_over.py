import time

from flappyPython import fp_constants as c
from flappyPython.fp_message import FpMessage
from flappyPython.fp_events import FpEvents


def replay_or_quit_game():
    events = FpEvents()

    if events.is_key_pressed():
        return True

    return False


def draw_game_over_text(screen):
    game_over_text = FpMessage(
        "Game Over",
        80,
        [c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2],
        "center",
        c.FONT_SUPER_MARIO_256_SRC,
        c.WHITE
    )

    game_over_text.draw(screen)


def draw_continue_text(screen):
    continue_text = FpMessage(
        "Press any key to continue",
        20,
        [c.SCREEN_WIDTH / 2, ((c.SCREEN_HEIGHT / 2) + 100)],
        "center",
        c.FONT_SUPER_MARIO_256_SRC,
        c.WHITE
    )

    continue_text.draw(screen)


def game_over_screen(pygame, clock, screen, main):
    draw_game_over_text(screen)
    draw_continue_text(screen)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit_game() == False:
        clock.tick()

    main()
