import random
import numpy as np


class LinearRegression:
    """
    class that implements calculations with an independent vector and a predictable variable
    """
    def __init__(self, x=None, y=None):
        self.x_set = x
        self.y_set = y
        self.data_list = None

    # CALCULATIONS
    def regression_coefficients_avg(self):
        x = np.array(self.x_set)
        y = np.array(self.y_set)

        x_m = np.mean(x)
        y_m = np.mean(y)

        x_df = x - x_m
        y_df = y - y_m

        k = np.sum(x_df * y_df) / np.sum(x_df ** 2)
        b = y_m - x_m * k
        return k, b

    def regression_coefficients_matrix(self):
        x = np.array(self.x_set)
        y = np.array(self.y_set)
        # add ones column and transpose
        xmatrix = np.vstack([np.ones(len(self.x_set)), x]).T
        bmatrix = np.linalg.inv(xmatrix.T.dot(xmatrix)).dot(xmatrix.T).dot(y)

        return bmatrix

    def predict_value(self, x: int) -> (int, int):
        k, b = self.regression_coefficients_avg()
        return x, k * x + b

    def append_predict_value(self, xp: int):
        x, y = self.predict_value(xp)
        self.x_set.append(x)
        self.y_set.append(y)

    @property
    def get_values(self):
        k, b = self.regression_coefficients_avg()
        min_x_index = self.x_set.index(min(self.x_set))
        max_x_index = self.x_set.index(max(self.x_set))
        return (self.x_set[min_x_index], self.x_set[max_x_index]), (self.x_set[min_x_index] * k + b, self.x_set[max_x_index] * k + b)

    @property
    def predicted_values(self):
        k, b = self.regression_coefficients_avg()
        return [k * x + b for x in self.x_set]

    # UPDATE METHODS
    def gen_data(self, n=100):
        k = random.randint(0, n//10)
        self.x_set = [i for i in range(n)]
        self.y_set = []
        for i in range(n):
            if random.randint(0, 1) % 2 == 0:
                self.y_set.append(k * (self.x_set[i] + random.randint(0, random.randint(0, n // 10))))
            else:
                self.y_set.append(k * (self.x_set[i] - random.randint(0, random.randint(0, n // 10))))

    def list_tr(self):
        self.data_list = [(self.x_set[i], self.y_set[i]) for i in range(len(self.x_set))]

    @property
    def get_x_set(self):
        return self.x_set

    @property
    def get_y_set(self):
        return self.y_set

    def new_x_set(self, new):
        self.x_set = new

    def new_y_set(self, new):
        self.y_set = new

    def append_x_y(self, x, y):
        self.x_set.append(x)
        self.y_set.append(y)