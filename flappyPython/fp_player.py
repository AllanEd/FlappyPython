class FpPlayer(object):
    def __init__(self, pos_x, pos_y, move_now, move_up, move_down, img):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.move_now = move_now
        self.move_up = move_up
        self.move_down = move_down
        self.img = img

    def get_pos_x(self):
        return self.pos_x

    def set_pos_x(self, pos_x):
        self.pos_x = pos_x

    def get_pos_y(self):
        return self.pos_y

    def set_pos_y(self, pos_y):
        self.pos_y = pos_y

    def get_move_now(self):
        return self.move_now

    def set_move_now(self, move_now):
        self.move_now = move_now

    def get_move_up(self):
        return self.move_up

    def get_move_down(self):
        return self.move_down

    def get_img(self):
        return self.img

    def add_pos_y(self, value):
        self.pos_y += value
