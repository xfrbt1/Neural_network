import pygame as pg

from draw_engine.config import *


class DrawingEngine:
    def __init__(self, WSState):
        self.state = WSState
        self.pressed = False
        self.positions = []

        self.field_data = self.clear_matrix()

    @staticmethod
    def clear_matrix():
        return [[0 for _ in range(DFSIZE)] for _ in range(DFSIZE)]

    def draw(self):
        colors = [(255, 255, 255), (0, 0, 0)]
        [pg.draw.rect(self.state.screen,
                      color=colors[self.field_data[i][j]],
                      rect=(j * PXAMOUNT, PXAMOUNT * i, PXAMOUNT - 1, PXAMOUNT - 1))
         for i in range(DFSIZE)
         for j in range(DFSIZE)]

    def mouse_press(self):
        self.pressed = True

    def mouse_release(self):
        self.pressed = False
        self.positions = []

    def mouse_motion(self):
        if self.pressed:
            self.positions.append(pg.mouse.get_pos())

    def key_handler(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.field_data = self.clear_matrix()

    def update_px(self):
        for x, y in self.positions:
            if x < PXAMOUNT * DFSIZE and y < PXAMOUNT * DFSIZE:
                self.field_data[y // PXAMOUNT][x // PXAMOUNT] = 1

    def update(self):
        self.key_handler()
        self.update_px()



