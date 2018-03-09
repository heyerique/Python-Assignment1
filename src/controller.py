from cmd import Cmd
from data_validator import DataValidator
from csv_operations import CSVOperations as csvop

class Controller(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.intro = "Welcome to Staff Information System\nEnter a keyword to start. \
                     For help, enter \"help\"."
        self._vld = DataValidator()
        self._data = []
        self._source = None
        self._data_sources = "csv", "database", "web"

    def do_select(self, input):
        """
        Select a data source
        :param input: <String> Source name
        :return: None
        """
        try:
            if input not in self._data_sources:
                raise ValueError("Error: The input value is not valid")
            else:
                if input == "csv":
                    self._source = csvop("staffinfo.csv")
                    print("Data source CSV is selected.")
        except AttributeError as e:
            print(e)
        except Exception as e:
            print(e)


    def do_add(self, input):
        """
        Add a new entry of data
        :param input: <EMPID> <Age> <Gender> <Sales> <BMI> <Salary> <Birthday>
        :return: None
        """
        raw_data = str(input).split()
        washed_data = {}
        try:
            if not len(raw_data) == 7:
                raise AttributeError("Error: Please input correct data.")
            else:
                washed_data = self._vld.check_all(raw_data)
        except AttributeError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            self._data.append(washed_data)
            print("Add succeed.")

    def do_save(self, arg):
        """
        Save data to specified data source
        :param arg: arg
        :return: None
        """
        if self._source == None:
            print("Error: No data source selected.")
        else:
            try:
                self._source.add(self._data)
                self._source.save()
            except (AttributeError, OSError) as e:
                print(e)
            except Exception as e:
                print(e)
            else:
                print("Data is saved.")


    def do_show(self, arg):
        if arg == "newdata":
            print(self._data)
        if arg == "alldata":
            if self._source == None:
                print("Error: No data source selected.")
            else:
                print(self._source.data)


if __name__ == "__main__":
    ctl = Controller()
    ctl.cmdloop()
