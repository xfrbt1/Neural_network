import pygame as pg
from draw_engine.config import *
from draw_engine.workspace_drawing_field import DrawingEngine
from dataset.data_handler import DataHandler


class WorkSpaceState:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.running = True

        self.drawing_engine = DrawingEngine(self)
        self.data_handler = DataHandler()

    def update(self):
        pg.display.flip()
        pg.display.set_caption(CAPTION)

        self.clock.tick(FPS)
        self.drawing_engine.update()

    def draw(self):
        self.screen.fill(GRAY)

        self.drawing_engine.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.drawing_engine.mouse_press()
            elif event.type == pg.MOUSEBUTTONUP:
                self.drawing_engine.mouse_release()
            elif event.type == pg.MOUSEMOTION:
                self.drawing_engine.mouse_motion()

    def run(self):
        while self.running:
            self.update()
            self.draw()
            self.check_events()

        self.drawing_engine.print_current_data_set()

        self.data_handler.append_x_data(self.drawing_engine.get_cur_x)
        self.data_handler.append_y_data(self.drawing_engine.get_cur_y)

        self.data_handler.save_x()
        self.data_handler.save_y()






