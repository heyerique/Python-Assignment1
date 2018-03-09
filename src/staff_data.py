from data import Data
from csv_operations import CSVOperations

class StaffData:
    """
    For data related operations
    """
    data = []
    _source = None

    def select_source(self, source):
        """
        Initialise the data source
        :param source: <String> source
        :return: None
        :Author: Zhiming Liu
        """
        # Set _self as an object of data operation when it hasn't been set
        if source == "csv" and self._source == None:
            self._source = CSVOperations("staffinfo.csv")
            self.load_data()

    def load_data(self):
        """
        Fetch all data from the specified data source
        :return: None
        :Author: Zhiming Liu
        """
        # When fetch data from the data source
        # Move existed data in self.data to the end of the list
        if len(self.data) == 0:
            self.data = self._source.read()
        else:
            old_data = self.data
            self.data = self._source.read()
            self.data.append(old_data)

    def add_data(self, data):
        """
        Add data to self.data
        :param data: <List> data
        :return: None
        :Author: Zhiming Liu
        """
        if not self.data_exist(data):
            staff = {}
            for d in Data:
                staff[d.name] = data[d.value]

            # Append to the temporary data
            self.data.append(staff)
        else:
            # If the EMPID is exists, raise an exception
            raise AttributeError("Add data error: The EMPID already exists.")

    def data_exist(self, data):
        """
        Check if the data with same empid exists.
        :param data: <List> data
        :return: Boolean
        :Author: Zhiming Liu
        """
        for staff in self.data:
            if data[Data.EMPID.value] == staff[Data.EMPID.name]:
                return True
        return

    def save_data(self):
        """
        Save data
        :return: None
        :Author: Zhiming Liu
        """
        if not self._source == None:
            self._source.save(self.data)
        else:
            raise OSError("Error: No data source specified.")

    def get_gender(self):
        """
        Get gender statistics
        :return: <Dictionary> gender
        :Author: Zhiming Liu
        """
        male = 0
        female = 0
        if not self._source == None:
            for row in self.data:
                # Calculate sum of male
                if row[Data.GENDER.name] == "M":
                    male += 1
                # Calculate sum of female
                else:
                    female += 1
        return {"Male": male, "Female": female}
