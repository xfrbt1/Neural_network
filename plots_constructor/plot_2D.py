from abc import ABC
import matplotlib.pyplot as plt

from plots_constructor.abstract_constructor import AbstractPlotConstructor


class Plot2D(AbstractPlotConstructor, ABC):

    @staticmethod
    def set_data(x, y, color='red'):
        plt.plot(x, y, color=color)

    @staticmethod
    def set_scatter_data(x, y, color='red'):
        plt.scatter(x, y, color=color)

    @staticmethod
    def set_vector(x, y, color='red'):
        plt.quiver(x, y, color=color, scale=25)
        plt.xlim([-10, 10])
        plt.axhline(0, color='black', linewidth=1)
        plt.ylim([-10, 10])
        plt.axvline(0, color='black', linewidth=1)


    @staticmethod
    def grid_view():
        plt.grid()

    @staticmethod
    def show():
        plt.show()

