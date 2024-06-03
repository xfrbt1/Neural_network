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

        self.field_data = self.clear_matrix()

        self.x_current_data_set = []
        self.y_current_data_set = []

    def draw(self):
        colors = [(0, 0, 0), (255, 255, 255)]
        [
            pg.draw.rect(
                self.state.screen,
                color=colors[self.field_data[i][j]],
                rect=(j * PX_SIZE, i * PX_SIZE, PX_SIZE - 1, PX_SIZE - 1),
            )
            for i in range(PX_AMOUNT)
            for j in range(PX_AMOUNT)
        ]

    def update_px(self):
        for x, y in self.positions:
            if y < PX_SIZE * PX_AMOUNT and x < PX_SIZE * PX_AMOUNT:
                i = y // PX_SIZE
                j = x // PX_SIZE
                self.field_data[i][j] = 1

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
        nums = {
            pg.K_1: 1,
            pg.K_2: 2,
            pg.K_3: 3,
            pg.K_4: 4,
            pg.K_5: 5,
            pg.K_6: 6,
            pg.K_7: 7,
            pg.K_8: 8,
            pg.K_9: 9,
            pg.K_0: 0,
        }

        if keys[pg.K_SPACE]:
            self.state.new_txt("")
            self.field_data = self.clear_matrix()

        if keys[pg.K_MINUS]:
            self.print_field()
            time.sleep(0.5)

        if keys[pg.K_EQUALS]:
            self.save_picture(path=DOWNLOAD_PATH, img=self.create_picture())
            time.sleep(0.5)

        if keys[pg.K_UP]:
            time.sleep(0.5)
            prd_vector = self.state.nn.predict(np.array([self.to_vector()]))[0]
            self.state.new_txt(str(np.argmax(prd_vector)))

        for key, value in nums.items():
            if keys[key]:

                y_vector = np.zeros(10, dtype="int8")
                y_vector[value] = 1
                self.append_current_data_set(self.to_vector(), self.x_current_data_set)
                self.append_current_data_set(y_vector, self.y_current_data_set)
                time.sleep(0.5)

    def update(self):
        self.key_handler()
        self.update_px()

    def to_vector(self):
        return np.array(self.field_data).reshape(
            (PX_AMOUNT * PX_AMOUNT),
        )

    def to_matrix(self):
        return np.array(self.field_data)

    def print_current_data_set(self):
        for i in range(len(self.x_current_data_set)):
            print(
                self.x_current_data_set[i],
                self.y_current_data_set[i],
                sep=":",
                end="\n\n",
            )

    def create_picture(self):
        img = Image.new("L", (len(self.field_data), len(self.field_data)))
        for i in range(len(self.field_data)):
            for j in range(len(self.field_data)):
                if self.field_data[i][j] == 1:
                    img.putpixel((j, i), 255)
                else:
                    img.putpixel((j, i), 0)
        return img

    def print_field(self):
        [print(*row, sep="  ") for row in self.field_data]

    @property
    def get_cur_x(self):
        return np.array(self.x_current_data_set)

    @property
    def get_cur_y(self):
        return np.array(self.y_current_data_set)

    @staticmethod
    def save_picture(path, img):
        img.save(
            f"{path}/picture{datetime.datetime.now().strftime('%H_%M_%S')}.png", "PNG"
        )

    @staticmethod
    def clear_matrix():
        return [[0 for _ in range(PX_AMOUNT)] for _ in range(PX_AMOUNT)]

    @staticmethod
    def append_current_data_set(vector, dataset):
        dataset.append(vector)
