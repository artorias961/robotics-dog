from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
import numpy as np
import cv2
import pyqtgraph as pg
import os


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("3D Geometry Reconstruction of Medical Images Application (PyQt6)")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # Calls the user interface
        self.user_interface()

        # showing all the widgets
        self.show()

        # Setting the drag file status to True (To allow the option to drop a file)
        self.setAcceptDrops(True)

        # Setting up a few parameters for the toggle switch logic state (or external window)
        self.win_help = None
        self.win_about_us = None
        self.win_plot = None

    def user_interface(self):
        # Calling the help button
        self.help_button()

        # Calling the about us button
        self.about_us_button()

        # Testing plot button function
        self.test_plot_function_button()

        # Dragging in a file
        self.drag_file_event()

    def drag_file_event(self):
        pass

    def test_plot_function_button(self):
        # Creating the push button
        button = QPushButton("Test Plot", self)

        # Setting the coordinates and the size of the button
        button.setGeometry(380, 360, 100, 30)

        # When the button is pressed then call the function to execute
        button.clicked.connect(self.test_plot_function_button_pressed)

    def test_plot_function_button_pressed(self):
        # Toggle switch: checking if the user closed or still on the new window
        if self.win_plot is None:
            self.win_plot = TestPlotFunction()
        self.win_plot.show()

    def about_us_button(self):
        # Creating the push button
        button = QPushButton("About Us", self)

        # Setting the coordinates and the size of the button
        button.setGeometry(120, 360, 100, 30)

        # When the button is pressed then call the function to execute
        button.clicked.connect(self.about_us_button_pressed)

    def about_us_button_pressed(self):
        # Toggle switch: checking if the user closed or still on the new window
        if self.win_help is None:
            self.win_help = AboutUsWindow()
        self.win_help.show()

    def help_button(self):
        # Creating a push button
        button = QPushButton("Help", self)

        # Setting geometry of button
        button.setGeometry(250, 360, 100, 30)

        # When the button is pressed then call the function to execute
        button.clicked.connect(self.help_button_pressed)

    def help_button_pressed(self):
        # Toggle switch: checking if the user closed or still on the new window
        if self.win_about_us is None:
            self.win_about_us = HelpWindow()
        self.win_about_us.show()


class TestPlotFunction(QWidget):
    def __init__(self):
        super().__init__()
        # Creating a window for plotting
        self.graph_window = pg.PlotWidget()

        # Initializing random data points
        self.x = np.random.normal(size=1000)
        self.y = np.random.normal(size=1000)

        # Plotting the result
        pg.plot(self.x, self.y, pen=None, symbol='o')

        #self.graph_window.plot(self.x, self.y)


class HelpWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        # The text of the information
        self.text = "Hello this is the 3D Geometry Reconstruction of Medical Images, this application is to help \n" \
                    "and get an understanding of applying Computer Vision to Medical Images. Also, this mini version of the \n" \
                    "application is to help understand how to create an application using Tkinter. Hope you enjoy this\n" \
                    "short application demo :)."

        # Creates a new sub window
        layout = QVBoxLayout()

        # Information inside the window
        self.label = QLabel(self.text)

        # Adding it to the window
        layout.addWidget(self.label)

        # Adding the title to the window
        self.setWindowTitle("Help Information")

        # Initializing the window
        self.setLayout(layout)


class AboutUsWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        # The text of the information
        self.text = "This is a passion for me to build a Qt framework application!!!\n" \
                    "\n\t\tSorry!!!! -> Arty-Chan"

        # Creates a new sub window
        layout = QVBoxLayout()

        # Information inside the window
        self.label = QLabel(self.text)

        # Adding it to the window
        layout.addWidget(self.label)

        # Adding the title to the window
        self.setWindowTitle("About the project")

        # Initializing the window
        self.setLayout(layout)


# create pyqt6 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())