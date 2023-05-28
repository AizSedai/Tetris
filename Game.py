import sys

import pygame
import time

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
        self.fps_clock = pygame.time.Clock()

    def init_param(self):
        pygame.init()
        self.render = Render()
        pygame.display.set_caption('Тетрис')

    def run(self):
        is_running = True
        self.calc_speed()
        falling_figure = Figure(self.field.field_width)
        next_figure = Figure(self.field.field_width)
        time_last_fall = time.time()
        self.pause()

        while is_running:
            if falling_figure is None:
                falling_figure = next_figure
                next_figure = Figure(self.field.field_width)
                time_last_fall = time.time()

                if not self.check_pos(falling_figure):
                    is_running = False
                    continue
            self.quit_game()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.pause()
                        time_last_fall = time.time()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.check_pos(falling_figure, add_x=-1):
                        falling_figure.x -= 1

                    elif event.key == pygame.K_RIGHT and self.check_pos(falling_figure, add_x=1):
                        falling_figure.x += 1

                    elif event.key == pygame.K_UP:
                        falling_figure.rotation = (falling_figure.rotation + 1) \
                                                  % len(falling_figure.figures[falling_figure.shape])
                        if not self.check_pos(falling_figure):
                            falling_figure.rotation = (falling_figure.rotation - 1) \
                                                      % len(falling_figure.figures[falling_figure.shape])

                    elif event.key == pygame.K_DOWN:
                        if self.check_pos(falling_figure, add_y=1):
                            falling_figure.y += 1

            if time.time() - time_last_fall > self.fall_speed:
                if not self.check_pos(falling_figure, add_y=1):
                    self.field.add_to_field(falling_figure)
                    self.points += self.field.clear_completed()
                    self.calc_speed()
                    falling_figure = None
                else:
                    falling_figure.y += 1
                    time_last_fall = time.time()

    def calc_speed(self):
        self.level = int(self.points / 10) + 1
        self.fall_speed = 0.36 - self.level * 0.02

    def check_pos(self, figure, add_x=0, add_y=0):
        for x in range(figure.figure_width):
            for y in range(figure.figure_height):
                is_negative_y = y + figure.y + add_y < 0
                if is_negative_y or figure.figures[figure.shape][figure.rotation][y][x] == 'o':
                    continue
                if not self.field.is_in_field(x + figure.x + add_x, y + figure.y + add_y):
                    return False
                if self.field.field_data[x + figure.x + add_x][y + figure.y + add_y] != 'o':
                    return False
        return True

    def pause(self):
        while self.check_keys() is None:
            pygame.display.update()
            self.fps_clock.tick()

    def check_keys(self):
        self.quit_game()
        for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP]):
            if event.type == pygame.KEYDOWN:
                continue
            return event.key
        return None

    def quit_game(self):
        for _ in pygame.event.get(pygame.QUIT):
            self.stop_game()
        for event in pygame.event.get(pygame.KEYUP):
            if event.key == pygame.K_ESCAPE:
                self.stop_game()
            pygame.event.post(event)

    @staticmethod
    def stop_game():
        pygame.quit()
        sys.exit()
