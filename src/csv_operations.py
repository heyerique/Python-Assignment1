import csv
from os import path
from idata_access import dataAccess

class CSVOperations(dataAccess):
    """
    This is class for reading from a specified CSV file and writing new data to it
    Author:
        Zhiming Liu
    """
    __file_path = ""
    fieldnames = ['empid', 'gender', 'age', 'sales', 'bmi', 'salary', 'birthday']
    data = []

    def __init__(self, file_path):
        """
        This the constructor of the class
        Args:
            file_path: the path of the CSV file
        """
        self.__file_path = file_path
        self.data = self.read()

    def read(self):
        """
        This function return content of the CSV file
        Returns:
            List of the file content
        """
        data = []
        try:
            with open(self.__file_path, newline="") as f:
                try:
                    reader = csv.DictReader(f, fieldnames=self.fieldnames)
                    data = [dict(row) for row in reader][1:]
                except csv.Error as e:
                    print("Read file error: " + str(e))
        except OSError as os_e:
            print(os_e)
        except Exception as e:
            print(e)

        return data

    def add(self, new_data: list):
        try:
            if new_data is not list:
                raise AttributeError("Add data error: Data should be a list")
            for row in new_data:
                self.data.append(row)
        except AttributeError as e:
            print(e)

    def file_exist(self):
        return path.exists(self.__file_path)

    def save(self):
        """
        This function saves new data to the CSV file
        Args:
            new_data: a list of new data in Dictionary with specified keys
        Returns:
            Boolean values. True is success, False if failed
        """
        result = True
        try:
            if not self.file_exist():
                raise OSError("Write data error: The file does not exist.")
            else:
                with open(self.__file_path, 'w', newline="") as f:
                    try:
                        writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                        writer.writeheader()
                        writer.writerows(self.data)
                    except csv.Error as e:
                        result = False
                        print("Write data failed: " + str(e))
        except OSError as os_e:
            result = False
            print(os_e)

        return result


# op = CSVOperations('staffinfo2.csv')
# new_data_2 = 12
# print(op.save())
# new_data_01 = [{"empid": "Y412", "gender": "M", "age": 41, "sales": 200,
# "bmi": "Obesity", "salary": 450, "birthday": "01-09-1977"}]
# op.add(new_data_01)
# op.save()
# print(op.get_data)