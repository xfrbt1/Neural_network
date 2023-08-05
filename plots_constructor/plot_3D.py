from abc import ABC
import matplotlib.pyplot as plt

from plots_constructor.abstract_constructor import AbstractPlotConstructor


class Plot3D(AbstractPlotConstructor, ABC):
    def __init__(self):
        plt.axes(projection='3d')

    @staticmethod
    def set_data(x, y, z, color='red'):
        plt.plot(x, y, z, color=color)

    @staticmethod
    def set_scatter_data(x, y, z,  color='red'):
        plt.scatter(x, y, z, color=color)

    @staticmethod
    def grid_view():
        plt.grid()

    @staticmethod
    def show():
        plt.show()


