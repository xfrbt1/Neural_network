import matplotlib
import matplotlib.pyplot as plt


class Plot_3D:
    def __init__(self):
        self.figure = plt.figure()
        self.ax = plt.axes(projection='3d')

    def plot(self, x, y, z):
        self.ax.plot3D(x, y, z, color='RED')

    def plot_surface(self, x, y, z):
        self.ax.plot_surface(x, y, z)

    @staticmethod
    def show():
        plt.show()


