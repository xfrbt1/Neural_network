import time

import pygame as pg
from PIL import Image
from draw_engine.config import *


class DrawingEngine:
    def __init__(self, WSState):
        self.state = WSState

        self.pressed = False
        self.positions = []

        self.picture_counter = 0
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
        if keys[pg.K_0]:
            img = self.create_picture()
            self.save_picture(img)
            time.sleep(1)

    def update_px(self):
        for x, y in self.positions:
            if x < PXAMOUNT * DFSIZE and y < PXAMOUNT * DFSIZE:
                self.field_data[y // PXAMOUNT][x // PXAMOUNT] = 1

    def create_picture(self):
        img = Image.new('L', (len(self.field_data), len(self.field_data)))
        for x in range(len(self.field_data)):
            for y in range(len(self.field_data)):
                if self.field_data[x][y] == 1:
                    pxv = 0
                else:
                    pxv = 255
                img.putpixel((y, x), pxv)

        return img

    def save_picture(self, img):
        img.save(f"/Users/aleksej/Desktop/python/Neural_network/pictures/pic{self.picture_counter}.png", "PNG")
        self.picture_counter += 1

    def update(self):
        self.key_handler()
        self.update_px()



