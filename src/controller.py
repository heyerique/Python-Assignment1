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

        # Instance of StaffData
        self._std = StaffData()

    def do_select(self, input):
        """
        Select a data source
        :param input: <String> Source name
        :return: None
        """
        # Available data sources
        options = "-csv", "-db"
        try:
            # Check if the input data source is available in this program or not
            if input not in options:
                raise ValueError("The data resource is not available.")
            else:
                # Code for initialise CSV data source
                if input == "-csv":
                    try:
                        self._std.select_source(input[1:])
                    except (CSVError, OSError) as e:
                        v.error(e)
                    except Exception as e:
                        v.error(e)
                    else:
                        v.success("Data source CSV is selected.")

                # Code for initialise database source
                elif input == "-db":
                    try:
                        self._std.select_source(input[1:])
                    except (ConnectionError, TypeError) as e:
                        v.error(e)
                    except Exception as e:
                        v.error(e)
                    else:
                        v.success("Data source Database is selected.")

                # Code for initialise XXXX data source
                else:
                    pass
        # Catch and display error message
        except ValueError as e:
            v.error(str(e) + "\n")
            v.help_select()
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
        except (AttributeError, ValueError) as e:
            v.error(str(e) + "\n")
            v.help_add()
        except CSVError as e:
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
        except ValueError as e:
            v.info(e)
        except (OSError, AttributeError) as e:
            v.error(e)
        except Exception as e:
            v.error(e)
        else:
            v.success("Data is saved")

    def do_show(self, line):
        # Get all instructions
        args = str(line).split()

        # Those commands are required single arguments
        single_commands = ["-a"]
        # Those commands are required two arguments
        plot_commands = ["-p", "-b"]
        all_commands = single_commands + plot_commands

        # Show data table
        if args[0] == "-t":
            if len(self._std.data) == 0 and len(self._std.new_data) == 0:
                v.info("No data to display.")
            if not len(self._std.data) == 0:
                v.display("ORIGINAL DATA:")
                v.display_data(self._std.data, ind = True)
            if not len(self._std.new_data) == 0:
                v.display("\nNEW DATA:")
                v.display_data(self._std.new_data, ind = True)
                v.display("\n(Input command \"save\" to save the new data)")


        elif args[0] in plot_commands:
            try:
                if len(args) == 1:
                    raise IndexError("Incomplete command line.")

                if args[0] == "-p":
                    self.show_pie(args[1])
                if args[0] == "-b":
                    self.show_bar(args[1])

            except IndexError as e:
                v.error(str(e) + "\n")
                v.help_show()
        else:
            v.info("Invalid command line.\n")
            v.help_show()

    def show_pie(self, line):
        # Draw Pies
        try:
            if len(self._std.get_gender()) == 0 or len(self._std.get_bmi()) == 0:
                raise ValueError("No data to display.")
            # Draw gender
            if line.upper() == Data.GENDER.name:
                v.plot_pie(self._std.get_gender(), "Gender Distribution")
            # Draw BMI
            if line.upper() == Data.BMI.name:
                v.plot_pie(self._std.get_bmi(), "Body Mass Index (BMI)")
        except ValueError as e:
            v.info(e)
        except Exception as e:
            v.error(e)

    def show_bar(self, line):
        # Draw Bars
        try:
            if len(self._std.get_gender()) == 0 or len(self._std.get_gender()) == 0:
                raise ValueError("No data to display.")
            # Draw gender
            if line.upper() == Data.GENDER.name:
                v.plot_bar(self._std.get_gender(), "Gender Distribution")
            # Draw BMI
            if line.upper() == Data.BMI.name:
                v.plot_bar(self._std.get_bmi(), "Body Mass Index (BMI)")
        except ValueError as e:
            v.info(e)
        except Exception as e:
            v.error(e)

    def help_show(self):
        v.help_show()

    def help_add(self):
        v.help_add()

    def help_save(self):
        v.help_save()

    def help_select(self):
        v.help_select()

    def do_quit(self, line):
        if not line == "-f" and not len(self._std.new_data) == 0:
            v.warning("The new data hasn't been saved. Enter \"quit -f\" to quit without saving.")
        else:
            v.display("Thanks for using. Bye!")
            return True


if __name__ == "__main__":
    ctl = Controller()
    ctl.cmdloop()
