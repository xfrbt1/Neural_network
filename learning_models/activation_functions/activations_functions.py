import math

import numpy as np


class ActivationFunction:
    def __init__(self):
        self.x = None
        self.y = None

    def set_x(self, x):
        self.x = np.array(x)

    def gen_x(self, start=-10, end=10, n=100):
        self.x = np.linspace(start, end, n)

    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    @staticmethod
    def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))

    def sigmoid_activation(self):
        self.y = np.array([self.sigmoid(x) for x in self.x])

    def tanh_activation(self):
        self.y = np.array([math.tanh(x) for x in self.x])

    def relu_activation(self):
        self.y = np.array([x if x >= 0 else 0 for x in self.x])


