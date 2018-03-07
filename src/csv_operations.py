import csv
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
        with open(self.__file_path, newline="") as f:
            try:
                reader = csv.DictReader(f, fieldnames=self.fieldnames)
                data = [dict(row) for row in reader][1:]
            except csv.Error as e:
                print("Read file error: " + str(e))
        return data

    def add(self, new_data: list):
        for row in new_data:
            self.data.append(row)

    def save(self):
        """
        This function saves new data to the CSV file

        Args:
            new_data: a list of new data in Dictionary with specified keys

        Returns:
            Boolean values. True is success, False if failed
        """
        with open(self.__file_path, 'w', newline="") as f:
            try:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(self.data)
            except csv.Error as e:
                print("Write CSV file error: " + str(e))
                return False
        return True


# op = CSVOperations('staffinfo.csv')
# new_data_01 = [{"empid": "Y412", "gender": "M", "age": 41, "sales": 200,
# "bmi": "Obesity", "salary": 450, "birthday": "01-09-1977"}]
# op.add(new_data_01)
# op.save()
# print(op.data)
