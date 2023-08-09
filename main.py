from draw_engine.workspace_state import WorkSpaceState
from plots_constructor.plot_2D import Plot2D
from plots_constructor.plot_3D import Plot3D
from regression_analysis.linear_regression import LinearRegression
from learning_models.activation_functions.activations_functions import ActivationFunction
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
    # gr.show()

    # pr = Perceptron()
    # pr.set_weights([-1, 1, 1])
    # print(pr.activate([1, 0, 0]))
    # print(pr.activate([1, 0, 1]))
    # print(pr.activate([1, 1, 0]))
    # print(pr.activate([1, 1, 1]))

    af = ActivationFunction()
    af.gen_x(n=1000)
    af.for_fun()

    gr = Plot2D()
    gr.set_data(af.get_x, af.get_y)
    gr.grid_view()
    gr.show()












