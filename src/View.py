import abc


class View(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def display(text):
        pass

    @staticmethod
    @abc.abstractmethod
    def plot(data):
        pass
