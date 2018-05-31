import pygame
from flappyPython.fp_constants import *


class FpMessage(object):
    def __init__(self, text, size, position, align, font_src, color):
        self.text = text
        self.size = size
        self.position = position
        self.align = align
        self.font_src = font_src
        self.color = color

    def get_text_on_screen(self):
        font = pygame.font.Font(self.font_src, self.size)
        return font.render(self.text, True, self.color)

    def draw(self, screen):
        text_on_screen = self.get_text_on_screen()
        text_on_screen_rect = text_on_screen.get_rect()

        if self.align == "center":
            text_on_screen_rect.center = self.position
        elif self.align == "topleft":
            text_on_screen_rect.topleft = self.position


        screen.blit(text_on_screen, text_on_screen_rect)
