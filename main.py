import math

from plots_constructor.plot_3D import Plot_3D
import numpy as np

if __name__ == '__main__':

    plot = Plot_3D()

    z_v = []
    x_v = []
    y_v = []

    for x in range(100):
        for y in range(100):
            z_v.append(x*y)
            x_v.append(x)
            y_v.append(y)

    plot.plot(x_v, y_v, z_v)
    plot.set_labels('x', 'y', 'Z')
    
    plot.show()


