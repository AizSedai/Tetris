import pygame
from Render import Render
from Field import Field


class Game:
    def __init__(self):
        self.render = None
        self.field = Field()

    def init_param(self):
        pygame.init()
        self.render = Render()
        pygame.display.set_caption('Тетрис')

    def run(self):
        is_running = True
        while is_running:
            pass
