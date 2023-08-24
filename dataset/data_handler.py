import numpy as np
import matplotlib.pyplot as plt

from draw_engine.config import *


class DataHandler:
    def __init__(self):
        self.x_set = None
        self.y_set = None

    def load_x_data(self):
        self.x_set = np.load('dataset/xdataset.npy')

    def load_y_data(self):
        self.y_set = np.load('dataset/ydataset.npy')

    def save_x(self):
        np.save('dataset/xdataset.npy', self.x_set)

    def save_y(self):
        np.save('dataset/ydataset.npy', self.y_set)

    def append_x_data(self, new_x):
        self.load_x_data()
        self.x_set = np.concatenate((self.x_set, new_x))

    def append_y_data(self, new_y):
        self.load_y_data()
        self.y_set = np.concatenate((self.y_set, new_y))

    def img_print(self):
        fig, axs = plt.subplots(1, 50)
        for i, vector in enumerate(self.x_set[:50]):
            matrix = vector.reshape(PX_AMOUNT, PX_AMOUNT)
            axs[i].imshow(matrix, cmap='gray')
        plt.show()

    def print_data(self):

        self.load_x_data()
        self.load_y_data()

        for i in range(len(self.x_set)):
            print(i, self.x_set[i], self.y_set[i], sep='\n')
            print('_______________________________')

    @staticmethod
    def save_x_data(x_set):
        np.save('dataset/xdataset.npy', x_set)

    @staticmethod
    def save_y_data(y_set):
        np.save('dataset/ydataset.npy', y_set)




