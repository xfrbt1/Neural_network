from abc import abstractstaticmethod, ABC


class AbstractPlotConstructor(ABC):

    @abstractstaticmethod
    def set_data(x, y):
        pass

    @abstractstaticmethod
    def set_scatter_data(x, y):
        pass

    @abstractstaticmethod
    def grid_view():
        pass

    @abstractstaticmethod
    def show():
        pass




