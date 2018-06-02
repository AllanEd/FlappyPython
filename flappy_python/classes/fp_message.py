import pygame


class FpMessage(object):
    def __init__(self, text, font_size, position, align, font_src, color):
        self.text = text
        self.font_size = font_size
        self.position = position
        self.align = align
        self.font_src = font_src
        self.color = color

    def get_text_on_screen(self):
        font = pygame.font.Font(self.font_src, self.font_size)
        return font.render(self.text, True, self.color)

    def draw(self, screen):
        text_on_screen = self.get_text_on_screen()
        text_on_screen_rect = text_on_screen.get_rect()

        text_on_screen_rect.center = self.position

        screen.blit(text_on_screen, text_on_screen_rect)
