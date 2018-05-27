class FpBlocks(object):
    def __init__(self, pos_x=None, pos_y=None, width=None, height=None, gap=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.gap = gap

    def get_pos_x(self):
        return self.pos_x

    def set_pos_x(self, pos_x):
        self.pos_x = pos_x

    def get_pos_y(self):
        return self.pos_y

    def set_pos_y(self, pos_y):
        self.pos_y = pos_y

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_gap(self, gap):
        self.gap = gap

    def subtract_pos_x(self, value):
        self.pos_x -= value

    def get_block_top_dimensions(self):
        return [self.pos_x, self.pos_y, self.width, self.height]

    def get_block_bottom_dimensions(self, screen_height):
        block_bottom_pos_y = self.pos_y + self.height + self.gap
        block_bottom_height = screen_height - block_bottom_pos_y
        return [self.pos_x, block_bottom_pos_y, self.width, block_bottom_height]

    def draw(self, pygame, screen, block_color, screen_height):
        pygame.draw.rect(screen, block_color, self.get_block_top_dimensions())
        pygame.draw.rect(screen, block_color, self.get_block_bottom_dimensions(screen_height))
