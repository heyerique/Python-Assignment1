# Written By Vaishali
import sys
if sys.version_info[0] >= 3:
    import tkinter as tk
else:
    import Tkinter as tk


class App(tk.Frame):

    def __init__(self, employee):
        self.employee = employee
        self.options = [['A001', 'F', '23', '456',
                         'Normal', '23', '30-05-1994'],
                        ['C234', 'M', '5', '676',
                         'Overweight', '300', '1-12-1977'],
                        ['C4', 'Male', 'nine', '66,8',
                         'heavy', '3,00', '1-12-19']]

        self.om_variable = tk.StringVar(self.employee)
        self.om_variable.set(self.options[0])
        self.om_variable.trace('w', self.option_select)

        self.om = tk.OptionMenu(self.employee, self.om_variable, *self.options)
        self.om.grid(column=0, row=0)

        self.label = tk.Label(self.employee, text='Enter new record')
        self.entry = tk.Entry(self.employee)
        self.button = tk.Button(self.employee,
                                text='Add option to list',
                                command=self.add_option)

        self.label.grid(column=1, row=0)
        self.entry.grid(column=1, row=1)
        self.button.grid(column=1, row=2)

        self.update_button = tk.Button(self.employee,
                                       text='Update option menu',
                                       command=self.update_option_menu)
        self.update_button.grid(column=0, row=2)

    def update_option_menu(self):
        menu = self.om["menu"]
        menu.delete(0, "end")
        for string in self.options:
            menu.add_command(label=string,
                             command=lambda value=string:
                             self.om_variable.set(value))

    def add_option(self):
        self.options.append(self.entry.get())
        self.entry.delete(0, 'end')
        self.options

    def option_select(self, *args):
        self.om_variable.get()


root = tk.Tk()
App(root)
root.mainloop()