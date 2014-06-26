import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *
from wheat_class import *
from potato_class import *

class CropWindow(QMainWindow):
    """Class creates main window to observe crop simulation"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_select_crop_layout()

    def create_select_crop_layout(self):
        #allows you to select the crop type

        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop",("Wheat", "Potato"))
        self.instantiate_button = QPushButton("Create crop")
        #create layout to hold the widgets
        self.initial_layout = QVBoxLayout()
        
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_crop_widget)

        #connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)

    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button() #get the radio that was selected
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif crop_type == 2:
            self.simulated_crop = Potato()
        print(self.simulated_crop)    
            
        
def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()

if __name__ == "__main__":
    main()
