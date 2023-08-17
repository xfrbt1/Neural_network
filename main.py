import numpy as np

from draw_engine.workspace_state import WorkSpaceState
from plots_constructor.plot_2D import Plot2D
from plots_constructor.plot_3D import Plot3D
from learning_models.learning_models.perceptron import Perceptron
from learning_models.learning_models.neuron import Neuron


if __name__ == '__main__':
    # wss = WorkSpaceState()
    # wss.run()

    w = np.array([
        [2],
        [2],
        [3]
    ])

    y = np.array([
        [10],
        [1],
        [1]
    ])

    matrixlist = [
        [1, 2, 12],
        [-4, 5, -6],
        [1, -7, 8]
    ]

    matrix = np.array(matrixlist)


    neuron = Neuron(w)
    print(neuron.update_mini_batch(matrix, y, learning_rate=1, eps=100))
    neuron.SGD(matrix, y, 1)
















