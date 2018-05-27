class FpBlocks(object):
    def __init__(self, pos_x=None, pos_y=None, width=None, height=None, gap=None, speed=None, bg_color=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.gap = gap
        self.speed = speed

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

    def set_speed(self, speed):
        self.speed = speed

    def get_bg_color(self):
        return self.bg_color

    def set_bg_color(self, bg_color):
        self.bg_color = bg_color

    def move(self):
        self.pos_x -= self.speed

    def get_block_top_dimensions(self):
        return [self.pos_x, self.pos_y, self.width, self.height]

    def get_block_bottom_dimensions(self, screen_height):
        block_bottom_pos_y = self.pos_y + self.height + self.gap
        block_bottom_height = screen_height - block_bottom_pos_y
        return [self.pos_x, block_bottom_pos_y, self.width, block_bottom_height]
