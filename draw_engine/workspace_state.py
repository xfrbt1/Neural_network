import pygame as pg

from config import *


class WorkSpaceState:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def update(self):
        pass

    def draw(self):
        pass

    def check_events(self):
        pass
