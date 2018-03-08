from cmd import Cmd
from data_validator import DataValidator

class Controller(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.intro = "Welcome to Staff Information System\nEnter a keyword to start. \
                     For help, enter \"help\"."
        self._vld = DataValidator()
        self._data = []

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

    def do_show(self, arg):
        if arg == "newdata":
            print(self._data)


if __name__ == "__main__":
    ctl = Controller()
    ctl.cmdloop()
