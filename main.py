import numpy as np

from draw_engine.workspace_state import WorkSpaceState
from plots_constructor.plot_2D import Plot2D
from plots_constructor.plot_3D import Plot3D
from regression_analysis.linear_regression import LinearRegression
from learning_models.single_layer_perceptron import Perceptron

if __name__ == '__main__':
    # wss = WorkSpaceState()
    # wss.run()

    # lr = LinearRegression()
    # lr.new_x_set([0, 10, 20, 30, 40, 50, 60])
    # lr.new_y_set([2, 28, 41, 55, 84, 107, 114])
    #
    # gr = Plot2D()
    # gr.set_scatter_data(lr.get_x_set, lr.get_y_set, 'blue')
    # gr.set_scatter_data(lr.get_x_set, lr.predicted_values, 'green')
    # gr.set_data(lr.get_values[0], lr.get_values[1])
    # gr.grid_view()
    #
    # gr.show()
    #
    # gr3d = Plot3D()
    # gr3d.set_scatter_data([1, 2], [2, 4], [4, 8])
    # gr3d.show()

    pr_and = Perceptron()
    pr_and.set_example_x_matrix([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    pr_and.set_example_y_vector([0, 0, 0, 1])
    pr_and.get_correct_w()

    pr_or = Perceptron()
    pr_or.set_example_x_matrix([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    pr_or.set_example_y_vector([0, 1, 1, 1])
    pr_or.get_correct_w()

    pr_orn = Perceptron()
    pr_orn.set_example_x_matrix([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    pr_orn.set_example_y_vector([1, 0, 0, 0])
    pr_orn.get_correct_w()

    pr_andn = Perceptron()
    pr_andn.set_example_x_matrix([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    pr_andn.set_example_y_vector([1, 1, 1, 0])
    pr_andn.get_correct_w()

    print("and:  ", pr_and.get_weights)
    print("or:   ", pr_or.get_weights)
    print("nand: ", pr_andn.get_weights)
    print("nor:  ", pr_orn.get_weights)





