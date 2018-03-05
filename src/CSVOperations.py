import csv


class CSVOperations:
    """
    This is class for reading from a specified CSV file and writing new data to it

    Author:
        Zhiming Liu
    """
    file_path = ""
    fieldnames = ['empid', 'gender', 'age', 'sales', 'bmi', 'salary', 'birthday']
    data = []

    def __init__(self, file_path):
        """
        This the constructor of the class

        Args:
            file_path: the path of the CSV file
        """
        self.file_path = file_path
        self.data = self.read_data

    @property
    def read_data(self):
        """
        This function return content of the CSV file

        Returns:
            List of the file content
        """
        with open(self.file_path, newline="") as f:
            try:
                reader = csv.DictReader(f, fieldnames=self.fieldnames)
                data = [dict(row) for row in reader][1:]
            except csv.Error as e:
                print("Read file error: " + e)
        return data

    def save_data(self, new_data: list = []):
        """
        This function saves new data to the CSV file

        Args:
            new_data: a list of new data in Dictionary with specified keys

        Returns:
            Boolean values. True is success, False if failed
        """
        for row in new_data:
            self.data.append(row)
        with open(self.file_path, 'w', newline="") as f:
            try:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(self.data)
            except csv.Error as e:
                print("Write CSV file error: " + e)
                return False
        return True


op = CSVOperations('staffinfo.csv')
print(op.data)
# new_data_01 = {"empid": 4, "gender": "M", "age": 41, "sales": 200,
# "bmi": "Obesity", "salary": 450, "birthday": "01-09-1977"}
# op.save_data(new_data_01)
# print(op.data)
