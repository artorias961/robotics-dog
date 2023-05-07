import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class DisplayAnImage(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties (x-coord, y-coord, width, height)
        self.setGeometry(100, 100, 300, 200)

        # Set the windows title for the application
        self.setWindowTitle('Arty-Chan Image loader')

        # Create a label for drop area
        self.drop_label = QLabel('Drag an image file here', self)

        # Setting the label for the drop off image (x-coord, y-coord, width, and height)
        self.drop_label.setGeometry(50, 50, 200, 100)

        # Align the image label 
        self.drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a label for the image
        self.image_label = QLabel(self)

        # Aligning the image label
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set up drag and drop events
        self.setAcceptDrops(True)

        # Create a layout for the window
        layout = QVBoxLayout()

        # Add the widget to the application
        layout.addWidget(self.drop_label)

        # Add the widget to the application
        layout.addWidget(self.image_label)

        # Create a central widget and set the layout
        central_widget = QWidget(self)

        #
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def dragEnterEvent(self, event):
        """
        The function is an drag operation enters the window's area. This method
        handles the drag and drop event and decides whether the drop is accepted
        or ignored.

        """
        # Determines if an event happens
        if event.mimeData().hasUrls():
            # Check if any of the dropped files are images
            for url in event.mimeData().urls():
                # From the drop off, get the file path of the image
                file_path = url.toLocalFile()

                # Create an instance of the QMimeDatabase class to look up MIME types for files
                mime_db = QMimeDatabase()

                # MIME type for the current file path
                mime_type = mime_db.mimeTypeForFile(file_path)

                # Checks if the MIME type is valid or not
                if mime_type.isValid() and mime_type.name().startswith('image/'):
                    # If it is an image file extension then accept
                    event.accept()
                    return
                
        # Else, ignore the file
        event.ignore()

    def dropEvent(self, event):
        # Checking the drop events
        for url in event.mimeData().urls():
            # Getting the current path of the file
            file_path = url.toLocalFile()
            
            # The string is empty to remove any previos string from the previous drag and drop operation 
            self.drop_label.setText('')

            # Show the image
            self.display_image(file_path)

    def display_image(self, file_path):
        # Load the image file
        image = QImageReader(file_path).read()

        # Scale the image to fit the label
        scaled_image = image.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio)

        # Display the image
        pixmap = QPixmap.fromImage(scaled_image)
        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    # Create the application and window instances
    app = QApplication(sys.argv)
    my_application = DisplayAnImage()

    # Show the window
    my_application.show()

    # Run the event loop
    sys.exit(app.exec())