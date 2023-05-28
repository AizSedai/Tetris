import pygame

from Field import Field
from Render import Render
from Figure import Figure


class Game:
    def __init__(self):
        self.render = None
        self.field = Field()
        self.points = 0
        self.level = 1
        self.fall_speed = None

    def init_param(self):
        pygame.init()
        self.render = Render()
        pygame.display.set_caption('Тетрис')

    def run(self):
        is_running = True

        self.calc_speed()
        field = Field()
        falling_figure = Figure(field.field_width)
        next_figure = Figure(field.field_width)

        while is_running:
            pass

    def calc_speed(self):
        self.level = int(self.points / 10) + 1
        self.fall_speed = 0.36 - self.level * 0.02

