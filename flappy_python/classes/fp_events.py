import pygame


class FpEvents(object):
    """Handles all pygame events.

    Events in this context are user key inputs.
    """

    def handle_user_input(self, fp_player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if (self.ifKeyUpIsDown(event)):
                fp_player.move_up()

            if (self.ifKeyUpIsUp(event)):
                fp_player.move_down()

    def ifKeyUpIsDown(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return True

    def ifKeyUpIsUp(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                return True

    def is_key_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            elif event.type == pygame.KEYDOWN:
                return True

            return False

    def quit_game(self):
        pygame.quit()
        quit()
