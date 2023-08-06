import datetime
import time
import numpy as np
import pygame as pg
from PIL import Image

from draw_engine.config import *


class DrawingEngine:
    def __init__(self, WSState):
        self.state = WSState

        self.pressed = False
        self.positions = []

        self.brush_thickness = 1
        self.field_data = self.clear_matrix()

    def draw(self):
        colors = [(255, 255, 255), (0, 0, 0)]
        [pg.draw.rect(self.state.screen,
                      color=colors[self.field_data[i][j]],
                      rect=(j * PX_SIZE, i * PX_SIZE, PX_SIZE - 1, PX_SIZE - 1))
         for i in range(PX_AMOUNT)
         for j in range(PX_AMOUNT)]

    def update_px(self):
        for x, y in self.positions:
            if y < PX_SIZE * PX_AMOUNT and x < PX_SIZE * PX_AMOUNT:
                i = y // PX_SIZE
                j = x // PX_SIZE
                self.field_data[i][j] = 1

    def set_new_brush_thickness(self, value):
        self.brush_thickness += value

    def mouse_press(self):
        self.pressed = True
        self.positions.append(pg.mouse.get_pos())

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

        if keys[pg.K_1]:
            self.print_field()
            time.sleep(0.5)

        if keys[pg.K_EQUALS]:
            self.save_picture(path=DOWNLOAD_PATH, img=self.create_picture())
            time.sleep(1)

    def create_picture(self):
        img = Image.new('L', (len(self.field_data), len(self.field_data)))
        for i in range(len(self.field_data)):
            for j in range(len(self.field_data)):
                if self.field_data[i][j] == 1:
                    img.putpixel((j, i), 0)
                else:
                    img.putpixel((j, i), 255)

        return img

    def interpolate(self):
        pass

    def extrapolate(self):
        pass

    def update(self):
        self.key_handler()
        self.update_px()

    def to_vector(self):
        return np.array(self.field_data).reshape((PX_AMOUNT*PX_AMOUNT), )

    def print_field(self):
        [print(*row, sep='  ') for row in self.field_data]

    @staticmethod
    def save_picture(path, img):
        img.save(f"{path}/picture{datetime.datetime.now().strftime('%H_%M_%S')}.png", "PNG")

    @staticmethod
    def clear_matrix():
        return [[0 for _ in range(PX_AMOUNT)] for _ in range(PX_AMOUNT)]





