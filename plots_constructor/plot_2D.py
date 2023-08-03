from plots_constructor.abstract_constructor import AbstractPlotConstructor
from abc import ABC
import matplotlib.pyplot as plt


class Plot2D(AbstractPlotConstructor, ABC):

    @staticmethod
    def set_data(x, y, color='red'):
        plt.plot(x, y, color=color)

    @staticmethod
    def set_scatter_data(x, y, color='red'):
        plt.scatter(x, y, color=color)

    @staticmethod
    def grid_view():
        plt.grid()

    @staticmethod
    def show():
        plt.show()
