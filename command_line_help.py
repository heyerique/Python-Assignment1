from cmd import Cmd


class help_comm(Cmd):

    def __init__(self):
        Cmd.__init__ (self)
        self.prompt = ">>>"
        self.intro = "WELCOME TO THE HELP CONSOLE!!!"

    def do_help(self, args):
        """Get help on commands
           'help' or '?' with no arguments prints a list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """
        ## The only reason to define this method is for the help text in the doc string
        Cmd.do_help (self, args)

    def do_quit(self,args):
        return -1

    def help_select(self):
        pass

    def help_add(self):
        print ("""*** OPTIONS
                -l : This loads the information from a file. The file is given to the command as a string.
                -m : This is for manual data entry. The user will be prompted for the information in steps after entering this option.
                -d : This loads the information into the system from a database.  ***""")

    def help_save(self):
        print ("""***     OPTIONS     
                -s : This is a standard save. The information is saved to a file in the saves folder in the program files. (object is serialized)
                -d : This saves the current information to the database.
                -f : This saves a file to the specified file location.    ***""")

    def help_show(self):
        print ("""*** OPTIONS
                -b : Shows a bar graph of the total sales made by males verse the total sales made by female.
                -p : Shows a pie chart of the percentage of female workers verse male workers
                -c : Shows a scatter plot graph of peoples age verse their salary.
                -i : Shows a pie chart of the BMI of a set of people.   ***""")

        #   do_q = do_quit

    def do_add(self, s):
        print ('This command adds the person data to the system. ')

    def do_save(self, s):
        print ('This command saves the current person data.')

    def do_show(self, s):
        print ('This displays the current working information in a given manner.')

    def do_quit(self, line):
        print("Quitting ......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))

    # do_q = do_quit

if __name__ == "__main__":
    helpcommand = help_comm ()
    helpcommand.cmdloop ()
