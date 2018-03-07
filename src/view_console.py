from iview import View
import matplotlib.pyplot as plt
import numpy as np


class ViewConsole(View):
    @staticmethod
    def display(text):
        print(text)

    @staticmethod
    def plot_pie(data, title=""):
        labels, sizes = list(data.keys()), list(data.values())
        fq, ax = plt.subplots() # Create a figure and a set of subplots
        ax.pie(sizes, labels=labels, startangle=90, autopct="%0.1f%%")
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

        if not title == "":
            plt.title(title.upper())

        plt.interactive(True)
        plt.show()

    @staticmethod
    def plot_bar(data, title=""):
        labels, y = list(data.keys()), list(data.values())
        x = np.arange(len(labels))
        width = 0.5
        plt.bar(x, y, width, color="#8FFF51")
        plt.xticks(x, labels)
        plt.grid(True)

        if not title == "":
            plt.title(title.upper())

        plt.interactive(True)
        plt.show()

    @staticmethod
    def plot_barh(data, title=""):
        labels, x = list(data.keys()), list(data.values())
        y = np.arange(len(labels))
        width = 0.2
        plt.barh(y, x, width, color="#8FFF51")
        plt.yticks(y, labels)
        plt.grid(True)

        if not title == "":
            plt.title(title.upper())

        plt.interactive(True)
        plt.show()


# new_data = {'Male': 75.0, 'Female': 15.0}
# ViewConsole.plot_pie(new_data, "Gender")
# ViewConsole.plot_bar(new_data, "Gender")
