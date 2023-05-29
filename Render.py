import pygame


class Render:
    def __init__(self, win_width, win_height):
        self.win_width = win_width
        self.win_height = win_height
        self.screen = pygame.display.set_mode((self.win_width, self.win_height))
        self.tetris_font = pygame.font.Font(None, 24)
        self.bg_color = (0, 0, 0)  # черный
        self.brd_color = (255, 255, 255)  # белый
        self.title_color = (225, 225, 0)  # желтый
        self.txt_color = (255, 255, 255)  # белый
        self.info_color = (0, 0, 225)  # синий
        self.block = 20
        self.colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0))  # RENDER # синий, зеленый, красный, желтый
        self.side_margin = int((self.win_width - 10 * self.block) / 2)
        self.top_margin = self.win_height - (20 * self.block) - 5

    def fill_bg(self):
        self.screen.fill(self.bg_color)

    def draw_title(self):
        title_surf = self.tetris_font.render('Тетрис', True, self.title_color)
        title_rect = title_surf.get_rect()
        title_rect.topleft = (self.win_width - 325, 30)
        self.screen.blit(title_surf, title_rect)

    def draw_field(self, field):
        pygame.draw.rect(self.screen,
                         self.brd_color, (self.side_margin - 4, self.top_margin - 4, (field.field_width * self.block) + 8,
                                          (field.field_height * self.block) + 8), 5)
        pygame.draw.rect(self.screen, self.bg_color, (self.side_margin, self.top_margin, self.block * field.field_width, self.block * field.field_height))
        for x in range(field.field_width):
            for y in range(field.field_height):
                self.draw_block(x, y, field.field_data[x][y], None)

    def draw_figure(self, figure, pixel_x=None, pixel_y=None):
        figure_to_draw = figure.figures[figure.shape][figure.rotation]
        if pixel_x is None and pixel_y is None:
            pixel_x, pixel_y = self.convert_coordinate(figure.x, figure.y)

        for x in range(figure.figure_width):
            for y in range(figure.figure_height):
                if figure_to_draw[y][x] != 'o':
                    self.draw_block(None, None, figure.color,
                                    pixel_x + (x * self.block), pixel_y + (y * self.block))

    def draw_block(self, block_x, block_y, color,  pixel_x=None, pixel_y=None):
        if color == 'o':
            return
        if pixel_x is None and pixel_y is None:
            pixel_x, pixel_y = self.convert_coordinate(block_x, block_y)
        pygame.draw.rect(self.screen, self.colors[color],
                         (pixel_x + 1, pixel_y + 1, self.block - 1, self.block - 1), 0, 3)

    def draw_next_figure(self, figure):
        next_surf = self.tetris_font.render('Следующая:', True, self.txt_color)
        next_rect = next_surf.get_rect()
        next_rect.topleft = (self.win_width - 150, 180)
        self.screen.blit(next_surf, next_rect)
        self.draw_figure(figure, pixel_x=self.win_width - 150, pixel_y=230)

    def draw_info(self, points, level):
        points_surf = self.tetris_font.render(f'Баллы: {points}', True, self.txt_color)
        points_rect = points_surf.get_rect()
        points_rect.topleft = (self.win_width - 550, 180)
        self.screen.blit(points_surf, points_rect)

        level_surf = self.tetris_font.render(f'Уровень: {level}', True, self.txt_color)
        level_rect = level_surf.get_rect()
        level_rect.topleft = (self.win_width - 550, 250)
        self.screen.blit(level_surf, level_rect)

        pause_surf = self.tetris_font.render('Пауза: пробел', True, self.info_color)
        pause_rect = pause_surf.get_rect()
        pause_rect.topleft = (self.win_width - 550, 420)
        self.screen.blit(pause_surf, pause_rect)

        esc_surf = self.tetris_font.render('Выход: Esc', True, self.info_color)
        esc_rect = esc_surf.get_rect()
        esc_rect.topleft = (self.win_width - 550, 450)
        self.screen.blit(esc_surf, esc_rect)

    def convert_coordinate(self, block_x, block_y):
        return (self.side_margin + (block_x * self.block)), (self.top_margin + (block_y * self.block))
