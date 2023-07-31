import matplotlib
import matplotlib.pyplot as plt


class Plot_3D:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes(projection='3d')

    def plot(self, x, y, z):
        self.ax.plot3D(x, y, z, color='red')

    def plot_surface(self, x, y, z):
        self.ax.plot_surface(x, y, z)

    def set_labels(self, xl, yl, zl):
        self.ax.set_xlabel(xl)
        self.ax.set_ylabel(yl)
        self.ax.set_zlabel(zl)

    @staticmethod
    def show():
        plt.show()


