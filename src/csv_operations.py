import csv
from os import path
from idata_access import dataAccess

class CSVOperations(dataAccess):
    """
    This is class for reading from a specified CSV file and writing new data to it
    :Author: Zhiming Liu
    """
    # CSV file path
    __file_path = ""

    # The header of data field in the CSV file. Also for data dictionaries
    fieldnames = ['empid', 'gender', 'age', 'sales', 'bmi', 'salary', 'birthday']

    # For saving data
    # data = []

    def __init__(self, file_path):
        # Initialise the file path
        self.__file_path = file_path

        # Call read() to retrieve existed data
        # self.data = self.read()

    def read(self):
        """
        This function return content of the CSV file
        :return: None
        """
        # Try to open the file for read. newline to avoid different newline signs
        with open(self.__file_path, newline="") as f:
            # Try to read data with given fieldnames
            reader = csv.DictReader(f, fieldnames=self.fieldnames)
            # Save data in an array, but ignore the first line
            data = [dict(row) for row in reader][1:]

        return data

    #def add(self, new_data: list):
        #"""
        #Add new items to self.data
        #:param new_data: list of dictionaries. The keys of the dictionaries must match self.fieldnames
        #:return: None
        #"""
        # If the data type of new_data is not List, raise an exception
        # Those exceptions need to be caught when the function is called
        #if not type(new_data) == list:
        #    raise AttributeError("Add data error: Data should be a list")
        # Append new data to the temporary data list
        #for row in new_data:
        #    self.data.append(row)

    def file_exist(self):
        """
        Check if the giving file/path exists
        :return:
        """
        return path.exists(self.__file_path)

    def save(self, data: list):
        """
        This function saves new data to the CSV file
        """
        # If the data type of data is not List, raise an exception
        # Those exceptions need to be caught when the function is called
        if not type(data) == list:
            raise AttributeError("Add data error: Data should be a list")
        # Raise an exception if the file/path doesn't exist
        # Those exceptions need to be caught when the function is called
        elif not self.file_exist():
            raise OSError("Write data error: The file does not exist.")
        else:
            # Open the file to write
            with open(self.__file_path, 'w', newline="") as f:
                # Write all temporary data list to the file
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(data)


# op = CSVOperations('staffinfo.csv')
# print(op.read())
# new_data_2 = 12
# print(op.save())
# new_data_01 = [{"empid": "Y413", "gender": "M", "age": 41, "sales": 200,
# "bmi": "Obesity", "salary": 450, "birthday": "01-09-1977"}]
# op.add(new_data_01)
# op.save(new_data_01)
# print(op.data)
