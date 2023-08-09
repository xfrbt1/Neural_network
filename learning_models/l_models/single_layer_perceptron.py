import numpy as np


class Perceptron:
    def __init__(self):
        self.x_e_matrix = None
        self.y_e_vector = None

        self.weights = None

    def set_example_x_matrix(self, x):
        if self.x_e_matrix is None:
            self.x_e_matrix = np.array(x)
        else:
            self.x_e_matrix = np.vstack((self.x_e_matrix, x))

    def set_example_x_vector(self, x):
        self.x_e_matrix = np.vstack((self.x_e_matrix, x))

    def set_example_y_vector(self, y):
        self.y_e_vector = np.array(y)

    def set_weights(self, weights_vector):
        self.weights = np.array(weights_vector)

    def append_example_y_vector(self, yv):
        self.y_e_vector = np.append(yv)

    def check_dim(self):
        if (self.x_e_matrix is None or self.y_e_vector is None) or (len(self.x_e_matrix) != len(self.y_e_vector)):
            raise Exception('VALUES ERROR Y VECTOR != X MATRIX ROW')

    def get_correct_w(self):
        self.check_dim()

        self.weights = np.array([0.0 for _ in self.x_e_matrix[0]])

        for i, row in enumerate(self.x_e_matrix):

            value = np.dot(self.weights, row)

            if value <= 0 and self.y_e_vector[i] > 0:
                self.weights += row
            elif value >= 0 and self.y_e_vector[i] <= 0:
                self.weights -= row

    def calculate_y(self, x):
        return np.dot(self.weights, np.array(x))

    def activate(self, x):
        return 1 if np.dot(self.weights, np.array(x)) > 0 else 0

    @property
    def get_weights(self):
        return self.weights

    def __str__(self):
        return f"x_e:\n{self.x_e_matrix}\n" \
               f"y_e:\n{self.y_e_vector}\n" \
               f"w:\n{self.weights}\n" \



