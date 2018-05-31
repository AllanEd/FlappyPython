import time

# constants
import flappy_python.fp_constants as c
# resources
from flappy_python.resources import paths as p
from flappy_python.resources import texts as t
# classes
from flappy_python.classes.fp_message import FpMessage
from flappy_python.classes.fp_events import FpEvents


def replay_or_quit_game():
    events = FpEvents()

    if events.is_key_pressed():
        return True

    return False


def draw_game_over_text(screen):
    game_over_text = FpMessage(
        t.GAME_OVER,
        80,
        [c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2],
        t.CENTER,
        p.SUPER_MARIO_256,
        c.WHITE
    )

    game_over_text.draw(screen)


def draw_continue_text(screen):
    continue_text = FpMessage(
        t.CONTINUE,
        20,
        [c.SCREEN_WIDTH / 2, ((c.SCREEN_HEIGHT / 2) + 100)],
        t.CENTER,
        p.SUPER_MARIO_256,
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

    main(pygame)
