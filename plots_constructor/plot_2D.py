import matplotlib
import matplotlib.pyplot as plt


class Plot_2D:
    def __init__(self):
        self.figure = plt.figure()
        self.ax = plt.axes()

    def load_data(self, x, y, color='red'):
        self.ax.plot(x, y, color=color)

    def set_labels(self, xl, yl):
        pass

    @staticmethod
    def grid_view():
        plt.grid()

    @staticmethod
    def load_data_scatter(x, y, color='blue'):
        plt.scatter(x, y, color=color)

    @staticmethod
    def show():
        plt.show()

