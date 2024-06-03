import pygame as pg

from draw_engine.config import *
from draw_engine.data_handler import DataHandler
from draw_engine.workspace_drawing_field import DrawingEngine
from learning_models.keras_models.keras_model import NeuralNetwork


class WorkSpaceState:
    def __init__(self):
        pg.init()
        pg.font.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.font1 = pg.font.Font(None, TXT_SIZE_1)
        self.font2 = pg.font.Font(None, TXT_SIZE_2)

        self.running = True
        self.txt = ""

        self.drawing_engine = DrawingEngine(self)
        self.data_handler = DataHandler()
        self.nn = NeuralNetwork()
        self.nn.load_model(MODEL_NAME)

    def update(self):
        pg.display.flip()
        pg.display.set_caption(CAPTION)

        self.clock.tick(FPS)
        self.drawing_engine.update()

    def draw(self):
        self.screen.fill(GRAY)
        self.drawing_engine.draw()

    def txt_blit(self):
        self.screen.blit(
            self.font1.render("MODEL RECOGNIZED:", True, BLACK), (HEIGHT, 0)
        )
        self.screen.blit(self.font2.render(self.txt, True, BLACK), (HEIGHT + 70, 20))

    def new_txt(self, string):
        self.txt = string

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                self.end()
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.drawing_engine.mouse_press()
            elif event.type == pg.MOUSEBUTTONUP:
                self.drawing_engine.mouse_release()
            elif event.type == pg.MOUSEMOTION:
                self.drawing_engine.mouse_motion()

    def run(self):
        while self.running:
            self.txt_blit()
            self.update()
            self.draw()
            self.check_events()

    def end(self):
        if len(self.drawing_engine.get_cur_x):
            self.data_handler.new_x(self.drawing_engine.get_cur_x)
            self.data_handler.new_y(self.drawing_engine.get_cur_y)

            self.data_handler.save_x(TEST_SETX)
            self.data_handler.save_y(TEST_SETY)
