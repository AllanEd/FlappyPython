# constants
from flappy_python import fp_constants as c
# resources
from flappy_python.resources import paths as p
from flappy_python.resources import texts as t
# classes
from flappy_python.classes.fp_player import FpPlayer
from flappy_python.classes.fp_image import FpImage
from flappy_python.classes.fp_events import FpEvents
from flappy_python.classes.fp_pipe import FpPipe
from flappy_python.classes.fp_score import FpScore
# helper for game over
from flappy_python.helper import fp_game_over


class FpSetup:
    """Creates the general setup.

    Sets the pygame setup(1), game backgrounds(2), the pipe obstacles(3),
    the player itself(4), events like input(5), the game score(6) and
    the game over state(7).

    Attributes:
        pygame: A pygame module for the setup of flappy python.
    """

    def __init__(self, pygame):
        # 1. Pygame setup
        self.pygame = pygame
        self.pygame.init()
        self.pygame.display.set_caption(t.TITLE)
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # 2. Background
        self.__set_bg_sky()
        self.__set_bg_clouds()
        self.__set_bg_ground()
        self.bg_moving_objects = self.bg_clouds + self.bg_ground

        # 3. Pipes
        self.__set_pipe_top()
        self.__set_pipe_bottom()

        # 4. Player
        self.player = FpPlayer()

        # 5. Events
        self.events = FpEvents()

        # 6. Score
        self.score = FpScore(c.SCORE_START_POINTS)

        # 7. Game over state
        self.is_game_over = False

    def __set_bg_sky(self):
        bg_sky_img = self.pygame.image.load(p.BG_SKY).convert()
        self.bg_sky = FpImage(0, 0, 0, bg_sky_img)

    def __set_bg_clouds(self):
        bg_clouds_img = self.pygame.image.load(p.BG_CLOUDS).convert_alpha()
        bg_clouds_first = FpImage(0, 0, c.BG_CLOUDS_SPEED, bg_clouds_img)
        bg_clouds_second = FpImage(c.SCREEN_WIDTH, 0, c.BG_CLOUDS_SPEED, bg_clouds_img)

        self.bg_clouds = [
            bg_clouds_first,
            bg_clouds_second
        ]

    def __set_bg_ground(self):
        bg_ground_img = self.pygame.image.load(p.BG_GROUND).convert_alpha()
        bg_ground_first = FpImage(0, 0, c.BG_GROUND_SPEED, bg_ground_img)
        bg_ground_second = FpImage(c.SCREEN_WIDTH, 0, c.BG_GROUND_SPEED, bg_ground_img)

        self.bg_ground = [
            bg_ground_first,
            bg_ground_second
        ]

    def __set_pipe_top(self):
        pipe_top_img = self.pygame.image.load(p.PIPE_TOP).convert_alpha()
        self.pipe_top = FpPipe(
            c.INIT_PIPE_TOP_Y,
            pipe_top_img
        )

    def __set_pipe_bottom(self):
        pipe_bottom_img = self.pygame.image.load(p.PIPE_BOTTOM).convert_alpha()
        self.pipe_bottom = FpPipe(
            FpPipe.calculate_pipe_bottom_y(self.pipe_top),
            pipe_bottom_img
        )

    def game_loop(self):
        return not self.is_game_over

    def set_frames_per_second(self):
        self.clock.tick(c.FRAMES_PER_SECOND)

    def handle_user_input(self):
        self.events.handle_user_input(self.player)

    def draw_bg(self):
        self.bg_sky.draw(self.screen)
        for o in self.bg_moving_objects:
            o.draw(self.screen)

    def move_bg(self):
        for o in self.bg_moving_objects:
            o.move()

    def draw_player(self):
        self.player.draw(self.screen)

    def draw_pipes(self):
        self.pipe_top.draw(self.screen)
        self.pipe_bottom.draw(self.screen)

    def move_pipes(self):
        self.pipe_top.move()
        self.pipe_bottom.move(self.pipe_top)

    def draw_score(self):
        self.score.draw(self.screen)

    def update_display(self):
        self.pygame.display.update()

    def player_passes_pipes(self):
        return self.pipe_top.player_passed_pipes(self.player)

    def increase_score(self):
        self.score.increase(c.SCORE_INCREASE_POINTS)

    def player_hits_boundary_or_pipes(self):
        return self.player.hits_boundary() or self.player.hits_pipes(self.pipe_top)

    def show_game_over_screen(self, main):
        fp_game_over.display_game_over_screen(self.pygame, self.clock, self.screen, main)
