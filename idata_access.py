from abc import ABCMeta, abstractmethod


class dataAccess(metaclass=ABCMeta):
    """
    Interface for data access implementation
    :Author: Zhiming Liu
    """
    @abstractmethod
    def read(self):
        """
        Read data from local files or databases
        :return: list of existed Data
        """
        pass

    #@abstractmethod
    #def add(self, new_data: list):
    #    """
    #    Add a list of new data to the property data
    #    :param new_data: Dictionary list
    #    :return: None
    #    """
    #    pass

    @abstractmethod
    def save(self, data: list):
        """
        Save data to local files or database
        :return: Boolean
        """
        pass
