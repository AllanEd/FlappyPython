import pygame


class FpMessage:
    """Creates pygame text messages.

    Creates text messages and displays it to the users screen.

    Attributes:
        text: A string that holds the text that will be displayed.
        font_size: An integer for the font size of the text.
        position: A list with the x and y coordinates of the texts position on the screen.
        align: A string that holds the alignment, e.g. 'center'.
        font_src: A string that holds the path to the font.
        color: A tupel with the (r, g, b) values.
    """

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
