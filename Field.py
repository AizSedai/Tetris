class Field:
    def __init__(self):
        self.field_width = 10
        self.field_height = 20
        self.block_size = 20
        self.field_data = [['o'] * self.field_height for _ in range(0, self.field_width)]

    def add_to_field(self, figure):
        for x in range(figure.figure_width):
            for y in range(figure.figure_height):
                if figure.figures[figure.shape][figure.rotation][y][x] != 'o':
                    self.field_data[x + figure.x][y + figure.y] = figure.color

    def create_empty_field(self):
        for i in range(self.field_width):
            self.field_data.append(['o'] * self.field_height)

    def is_in_field(self, x, y):
        return 0 <= x < self.field_width and y < self.field_height

    def clear_completed(self):
        removed_lines = 0
        y = self.field_height - 1
        while y >= 0:
            if self.is_completed(y):
                for push_down_y in range(y, 0, -1):
                    for x in range(self.field_width):
                        self.field_data[x][push_down_y] = self.field_data[x][push_down_y - 1]
                for x in range(self.field_width):
                    self.field_data[x][0] = 'o'
                removed_lines += 1
            else:
                y -= 1
        return removed_lines

    def is_completed(self, y):
        for x in range(self.field_width):
            if self.field_data[x][y] == 'o':
                return False
        return True
