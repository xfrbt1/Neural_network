from abc import abstractstaticmethod, ABC


class AbstractPlotConstructor(ABC):

    @abstractstaticmethod
    def set_data(*data):
        pass

    @abstractstaticmethod
    def set_scatter_data(*data):
        pass

    @abstractstaticmethod
    def grid_view():
        pass

    @abstractstaticmethod
    def show():
        pass




