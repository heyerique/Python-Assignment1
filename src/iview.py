from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    """
    Interface for output implementation
    """
    @staticmethod
    @abstractmethod
    def display(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def display_error(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def display_success(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def plot_pie(data, title=""):
        """
        Plot a pie chart for gender, BMI
        :param data: data dictionary
        :param title: string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def plot_bar(data, title=""):
        """
        Plot a vertical bar chart for sales, salary, age...
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Zhiming Liu
        """
        pass

    @staticmethod
    @abstractmethod
    def plot_barh(data, title=""):
        """
        Plot a horizontal bar chart for sales, salary, age...
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Zhiming Liu
        """
        pass
