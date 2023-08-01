import matplotlib
import matplotlib.pyplot as plt


class Plot_2D:
    def __init__(self):
        self.figure = plt.figure()
        self.ax = plt.axes()

    def plot(self, x, y, color='BLUE'):
        self.ax.plot(x, y, color=color)

    def set_labels(self, xl, yl):
        pass

    def grid(self):
        plt.grid()

    def scatter_plot(self, x, y, color='BLUE'):
        plt.scatter(x, y, color=color)

    @staticmethod
    def show():
        plt.show()

