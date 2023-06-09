import random


class Figure:
    def __init__(self, field_width, colors):
        self.field_width = field_width
        self.figure_width = 5
        self.figure_height = 5
        self.colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0))  # RENDER # синий, зеленый, красный, желтый
        self.figures = {'S': [['ooooo',
                               'ooooo',
                               'ooxxo',
                               'oxxoo',
                               'ooooo'],
                              ['ooooo',
                               'ooxoo',
                               'ooxxo',
                               'oooxo',
                               'ooooo']],
                        'Z': [['ooooo',
                               'ooooo',
                               'oxxoo',
                               'ooxxo',
                               'ooooo'],
                              ['ooooo',
                               'ooxoo',
                               'oxxoo',
                               'oxooo',
                               'ooooo']],
                        'J': [['ooooo',
                               'oxooo',
                               'oxxxo',
                               'ooooo',
                               'ooooo'],
                              ['ooooo',
                               'ooxxo',
                               'ooxoo',
                               'ooxoo',
                               'ooooo'],
                              ['ooooo',
                               'ooooo',
                               'oxxxo',
                               'oooxo',
                               'ooooo'],
                              ['ooooo',
                               'ooxoo',
                               'ooxoo',
                               'oxxoo',
                               'ooooo']],
                        'L': [['ooooo',
                               'oooxo',
                               'oxxxo',
                               'ooooo',
                               'ooooo'],
                              ['ooooo',
                               'ooxoo',
                               'ooxoo',
                               'ooxxo',
                               'ooooo'],
                              ['ooooo',
                               'ooooo',
                               'oxxxo',
                               'oxooo',
                               'ooooo'],
                              ['ooooo',
                               'oxxoo',
                               'ooxoo',
                               'ooxoo',
                               'ooooo']],
                        'I': [['ooxoo',
                               'ooxoo',
                               'ooxoo',
                               'ooxoo',
                               'ooooo'],
                              ['ooooo',
                               'ooooo',
                               'xxxxo',
                               'ooooo',
                               'ooooo']],
                        'O': [['ooooo',
                               'ooooo',
                               'oxxoo',
                               'oxxoo',
                               'ooooo']],
                        'T': [['ooooo',
                               'ooxoo',
                               'oxxxo',
                               'ooooo',
                               'ooooo'],
                              ['ooooo',
                               'ooxoo',
                               'ooxxo',
                               'ooxoo',
                               'ooooo'],
                              ['ooooo',
                               'ooooo',
                               'oxxxo',
                               'ooxoo',
                               'ooooo'],
                              ['ooooo',
                               'ooxoo',
                               'oxxoo',
                               'ooxoo',
                               'ooooo']]}
        self.shape = random.choice(list(self.figures.keys()))
        self.rotation = random.randint(0, len(self.figures[self.shape]) - 1)
        self.x = int(self.field_width / 2) - int(self.figure_width / 2)
        self.y = -2
        self.color = random.randint(0, len(colors) - 1)
