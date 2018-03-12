from cmd import Cmd
from csv import Error as CSVError
from data_validator import DataValidator
from view_console import ViewConsole as v
from staff_data import StaffData
from data import Data

class Controller(Cmd):
    def __init__(self):
        Cmd.__init__(self)

        # The command line indicator
        self.prompt = ">>> "

        # Welcome information
        self.intro = "Welcome to Staff Information System\nEnter a keyword to start. For help, enter \"help\"."

        # Object of DataValidator, for validating data
        self._vld = DataValidator()

        # Available data sources
        self._data_sources = "csv", "database", "web"

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
                raise ValueError("The data resource is not available.")
            else:
                # Code for initialise CSV data source
                if input == "csv":
                    try:
                        self._std.select_source("csv")
                    except (CSVError, OSError) as e:
                        v.error(e)
                    except Exception as e:
                        v.error(e)
                    else:
                        v.success("Data source CSV is selected.")

                # Code for initialise database source
                elif input == "database":
                    pass

                # Code for initialise XXXX data source
                else:
                    pass
        # Catch and display error message
        except AttributeError as e:
            v.error(e)
        except Exception as e:
            v.error(e)


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
            if not len(raw_data) == len(Data):
                raise AttributeError("Please input correct data.")
            else:
                # Check and wash data by check_all() of DataValidator
                result = self._vld.check_all(raw_data)
                # Check if there is any None which stands for invalid input
                if None in result:
                    key = 0
                    # build a list of name list
                    items = list(map(lambda i : i.name, Data))
                    e_str = ""
                    while key < len(result):
                        if result[key] == None:
                            # Left alignment
                            e_str += "{:<10}".format(items[key])
                        key += 1
                    raise ValueError("The following field(s) is invalid:\n%s" % e_str)
                else:
                    self._std.add_data(result)
        except (AttributeError, ValueError, CSVError) as e:
            v.error(e)
        except Exception as e:
            v.error(e)
        else:
            v.success("Add data")

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
            v.error(e)
        except Exception as e:
            v.error(e)
        else:
            v.success("Data is saved")


    def do_show(self, line):
        # Get all instructions
        args = str(line).split()

        # Show data table
        if args[0] == "-a":
            v.display_data(self._std.data)

        # Draw Pies
        if args[0] == "-p":
            # Draw gender
            if args[1].upper() == Data.GENDER.name:
                v.plot_pie(self._std.get_gender(), "Gender Distribution")
            # Draw BMI
            if args[1].upper() == Data.BMI.name:
                v.plot_pie(self._std.get_bmi(), "Body Mass Index (BMI)")

        # Draw Bars
        if args[0] == "-b":
            # Draw gender
            if args[1].upper() == Data.GENDER.name:
                v.plot_bar(self._std.get_gender(), "Gender Distribution")
            # Draw BMI
            if args[1].upper() == Data.BMI.name:
                v.plot_bar(self._std.get_bmi(), "Body Mass Index (BMI)")


    def do_quit(self, line):
        v.display("Bye!")
        return True


if __name__ == "__main__":
    ctl = Controller()
    ctl.cmdloop()
