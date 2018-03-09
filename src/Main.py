# Written By Vaishali
#
# This is the main file.
# This file handles all the dependent injections
# And the cmdloop is started.
#
#

from src.controller.Controller import *
from src.iView.View import *
from src.controller import *
from src.database_conn.Database import *
from src.data_validator.DataValidator import *
from src.view_console.ViewConsole import *
import sys


if __name__ == '__main__':
    Controller(ViewConsole(), controller(
                            DataValidator(),
                            Database(),
                            Controller.check_set_file_path(sys.argv)
                            )
                          ).cmdloop()
