class Field:
    def __init__(self):
        self.field_width = 10
        self.field_height = 20
        self.block_size = 20
        self.field_data = [['o'] * self.field_height for _ in range(0, self.field_width)]

    def add_to_field(self, fig):
        for x in range(fig.fig_w):
            for y in range(fig.fig_h):
                if fig.figures[fig.shape][fig.rotation][y][x] != 'o':
                    self.field_data[x + fig.x][y + fig.y] = fig.color

    def create_empty_field(self):
        for i in range(self.field_width):
            self.field_data.append(['o'] * self.field_height)

    def is_in_field(self, x, y):
        return 0 <= x < self.field_width and y < self.field_height
