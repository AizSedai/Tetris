import pygame


class Render:
    def __init__(self):
        self.win_width = 600
        self.win_height = 500
        self.screen = pygame.display.set_mode((self.win_width, self.win_height))
        self.tetris_font = pygame.font.Font(None, 24)
        