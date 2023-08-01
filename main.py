from draw_engine.workspace_state import WorkSpaceState
from plots_constructor.plot_2D import Plot_2D
from regression_analysis.least_square_method import LeastSquareMethod

if __name__ == '__main__':
    xy = ((0, -0.5), (1, 0), (0, 0.5), (0, 1.5), (1, 2.5), (2, 3))
    x = [i[1] for i in xy]
    y = [i[0] for i in xy]
    lsm = LeastSquareMethod(x, y)
    lsm.gen_data()

    gr = Plot_2D()
    gr.scatter_plot(lsm.get_x, lsm.get_y)
    gr.grid()
    gr.show()

