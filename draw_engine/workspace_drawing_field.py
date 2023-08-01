import pygame as pg

from draw_engine.config import *


class DrawingEngine:
    def __init__(self, WSState):
        self.state = WSState

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

    def mouse_handler(self, pos):
        x, y = pos[0], pos[1]
        if x < PXAMOUNT * DFSIZE and y < PXAMOUNT * DFSIZE:
            self.field_data[y // PXAMOUNT][x // PXAMOUNT] = 1

    def key_handler(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.field_data = self.clear_matrix()

    def update(self):
        self.key_handler()



