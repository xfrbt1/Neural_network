import random
import numpy as np


class LinearRegression:
    def __init__(self, x=None, y=None):
        self.x, self.y = x, y
        self.data_list = None

    def gen_data(self, n=100):
        k = random.randint(0, n//10)
        self.x = [i for i in range(n)]
        self.y = []
        for i in range(n):
            if random.randint(0, 1) % 2 == 0:
                self.y.append(k*(self.x[i] + random.randint(0, random.randint(0, n//10))))
            else:
                self.y.append(k*(self.x[i] - random.randint(0, random.randint(0, n//10))))

    def list_tr(self):
        self.data_list = [(self.x[i], self.y[i]) for i in range(len(self.x))]

    @property
    def get_x(self):
        return self.x

    @property
    def get_y(self):
        return self.y

    def set_x(self, new):
        self.x = new

    def set_y(self, new):
        self.y = new

    def least_square(self):
        pass

    def linear_regression(self):
        x = np.array(self.x)
        y = np.array(self.y)

        x_m = np.mean(x)
        y_m = np.mean(y)

        x_df = x - x_m
        y_df = y - y_m

        k = np.sum(x_df * y_df) / np.sum(x_df ** 2)
        b = y_m - x_m * k
        return k, b

    @property
    def get_lr_values(self):
        k, b = self.linear_regression()
        return [self.x[0], self.x[-1]], [self.x[0] * k + b, self.x[-1] * k + b]

