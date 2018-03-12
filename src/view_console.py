from iview import View
import matplotlib.pyplot as plt
import numpy as np


class ViewConsole(View):
    @staticmethod
    def display(text):
        print(text)

    @staticmethod
    def error(text):
        print("Error: %s" % text)

    @staticmethod
    def success(text):
        print("Succeed: %s" % text)

    @staticmethod
    def plot_pie(data, title=""):
        # Get labels and sizes from the data
        labels, values = list(data.keys()), list(data.values())

        # Show numbers on labels
        id = 0
        while id < len(labels):
            labels[id] = "{0} ({1})".format(labels[id], values[id])
            id += 1

        # Create a figure and a set of subplots
        fq, ax = plt.subplots()

        # Set labels, start angle, and the label format (e.g.: 35.0%)
        ax.pie(values, labels=labels, startangle=90, autopct="%0.1f%%")

        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis("equal")

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title(title.upper())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show()

    @staticmethod
    def plot_bar(data, title=""):
        # Get labels and sizes from the data
        labels, y = list(data.keys()), list(data.values())

        # Calculate numbers of items on x axis
        x = np.arange(len(labels))

        # Width of bars
        width = 0.5

        # Set X, Y, bar width and bar colour
        plt.bar(x, y, width, color="#FF55AA")

        # Set labels for X items
        plt.xticks(x, labels)

        # Show diagram grid
        plt.grid(True)

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title(title.upper())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show()

    @staticmethod
    def plot_barh(data, title=""):
        # Get labels and sizes from the data
        labels, x = list(data.keys()), list(data.values())

        # Calculate numbers of items on y axis
        y = np.arange(len(labels))

        # Width of bars
        width = 0.2

        # Set Y, X, bar width and bar colour
        plt.barh(y, x, width, color="#FF55AA")

        # Set labels for Y items
        plt.yticks(y, labels)

        # Show diagram grid
        plt.grid(True)

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title(title.upper())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show()


# new_data = {'Male': 75.0, 'Female': 15.0}
# ViewConsole.plot_pie(new_data, "Gender")
# ViewConsole.plot_bar(new_data, "Gender")
