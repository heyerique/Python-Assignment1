from cmd import Cmd
from csv import Error as CSVError
from data_validator import DataValidator
from view_console import ViewConsole as v
from staff_data import StaffData

class Controller(Cmd):
    def __init__(self):
        Cmd.__init__(self)

        # The command line indicator
        self.prompt = ">>> "

        # Welcome information
        self.intro = "Welcome to Staff Information System\nEnter a keyword to start. For help, enter \"help\"."

        # Object of DataValidator, for validating data
        self._vld = DataValidator()

        # For saving data temporarily until user finish adding
        # self._data = []

        # The object of the selected data source class
        # self._source = None

        # Available data sources
        self._data_sources = "csv", "database", "web"

        # The flag to mark if the temporary data is saved or not
        # Initially the value is True, set False after a new data is saved successfully
        # self._saved = True

        # Instance of StaffData
        self._std = StaffData()

    def do_select(self, input):
        """
        Select a data source
        :param input: <String> Source name
        :return: None
        """
        try:
            # Check if the input data source is available in this program or not
            if input not in self._data_sources:
                raise ValueError("Error: The input value is not valid")
            else:
                # Code for initialise CSV data source
                if input == "csv":
                    try:
                        self._std.select_source("csv")
                        v.display("Data source CSV is selected.")
                    except (CSVError, OSError) as e:
                        v.display("CSV Initialisation Error: " + e)
                    except Exception as e:
                        v.display("CSV Initialisation Error: " + str(e))

                # Code for initialise database source
                elif input == "database":
                    pass

                # Code for initialise XXXX data source
                else:
                    pass
        # Catch and display error message
        except AttributeError as e:
            v.display(e)
        except Exception as e:
            v.display(e)


    def do_add(self, input):
        """
        Add a new entry of data
        :param input: <EMPID> <Age> <Gender> <Sales> <BMI> <Salary> <Birthday>
        :return: None
        """
        # Split the input argument to obtain the data
        raw_data = str(input).split()

        try:
            # Check if input data has 7 data fields
            if not len(raw_data) == 7:
                raise AttributeError("Error: Please input correct data.")
            else:
                # Check and wash data by check_all() of DataValidator
                self._std.add_data(self._vld.check_all(raw_data))
        except (AttributeError, ValueError, CSVError) as e:
            v.display(e)
        except Exception as e:
            v.display(e)
        else:
            v.display("Add succeed.")

    def do_save(self, arg):
        """
        Save data to specified data source
        :param arg: arg
        :return: None
        """
        # If no data source selected, prompt user to do so.
        try:
            self._std.save_data()
        except (OSError, AttributeError) as e:
            v.display(e)
        except Exception as e:
            v.display(e)
        else:
            v.display("Data is saved successfully.")


    def do_show(self, line):
        if line == "alldata":
             v.display(self._std.data)

    def do_plot(self, line):
        args = str(line).split()
        if args[0] == "pie":
            if args[1] == "gender":
                v.plot_pie(self._std.get_gender())

    def do_quit(self, line):
        v.display("Bye!")
        return True


if __name__ == "__main__":
    ctl = Controller()
    ctl.cmdloop()
