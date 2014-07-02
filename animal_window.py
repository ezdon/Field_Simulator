import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import *
from manual_grow_dialog_class import *


from cow_class import *
from sheep_class import *

class AnimalWindow(QMainWindow):
    """Class creates main window to observe crop simulation"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animal Simulator")
        self.create_select_animal_layout()
        self.stacked_layout = QStackedLayout() # this holds the various layouts for this window
        self.stacked_layout.addWidget(self.select_animal_widget)

        #set central widget to display layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        
    def create_select_animal_layout(self):
        #allows you to select the crop type

        self.animal_radio_buttons = RadioButtonWidget("Animal Simulation", "Please select an animal",("Cow", "Sheep"))
        self.instantiate_button = QPushButton("Create animal")
        #create layout to hold the widgets
        self.initial_layout = QVBoxLayout()
        
        self.initial_layout.addWidget(self.animal_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_animal_widget = QWidget()
        self.select_animal_widget.setLayout(self.initial_layout)

        

        #connections
        self.instantiate_button.clicked.connect(self.instantiate_animal)

    def create_view_animal_layout(self,animal_type):
        #second layout of the window - view the crop growth
        self.grow_label = QLabel("Weight")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Animal Status")

        self.grow_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

##        if crop_type == 1:
##            self.crop_view = WheatView()
##        elif crop_type == 2:
##            self.crop_view = PotatoView()
            
        #ensure the crop view appears a certain size
##        self.crop_view.setHorizontalScrollBarPolicy(1)
##        self.crop_view.setVerticalScrollBarPolicy(1)
##        self.crop_view.setFixedHeight(182)
##        self.crop_view.setFixedWidth(242)
            
        self.manual_grow_button = QPushButton("Manual Grow")
        self.automatic_grow_button = QPushButton("Automatically Grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        #add label widgets to the status layout
        self.status_grid.addWidget(self.grow_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        #add line edit widgets to the status layout
        self.status_grid.addWidget(self.grow_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        #add widgets/layouts to the grow layout
##        self.grow_grid.addWidget(self.crop_view,0,0)
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        #create a widget to display the grow layout
        self.view_animal_widget = QWidget()
        self.view_animal_widget.setLayout(self.grow_grid)

        #connections
        self.automatic_grow_button.clicked.connect(self.automatically_grow_animal)
        self.manual_grow_button.clicked.connect(self.manually_grow_animal)

        
    def instantiate_animal(self):
        animal_type = self.animal_radio_buttons.selected_button() #get the radio that was selected
        if animal_type == 1:
            self.simulated_animal = Cow()
        elif animal_type == 2:
            self.simulated_animal = Sheep()
    
        self.create_view_animal_layout(animal_type) #create the view crop layout
        self.stacked_layout.addWidget(self.view_animal_widget)
        self.stacked_layout.setCurrentIndex(1)

    def automatically_grow_animal(self):
        for days in range(30):
            food = random.randint(1,10)
            water = random.randint(1,10)
            self.simulated_animal.grow(food,water)
##        self.update_animal_view_status()

    def manually_grow_animal(self):
        manual_values_dialog = ManualGrowDialog()
        manual_values_dialog.exec_()
        food, water = manual_values_dialog.values()
        self.simulated_animal.grow(food,water)
##        self.update_animal_view_status()

        
##    def update_animal_view_status(self):
##        animal_status_report = self.simulated_animal.report()
##         #update the text fields
##        self.growth_line_edit.setText(str(animal_status_report["growth"]))
##        self.days_line_edit.setText(str(animal_status_report["days growing"]))
##        self.status_line_edit.setText(str(animal_status_report["status"]))
##
##        if crop_status_report["status"] == "Baby":
##            self.crop_view.switch_scene(0)
##        elif crop_status_report["status"] == "Small":
##            self.crop_view.switch_scene(1)
##        elif crop_status_report["status"] == "Medium":
##            self.crop_view.switch_scene(2)
##        elif crop_status_report["status"] == "Mature":
##            self.crop_view.switch_scene(3)
##        elif crop_status_report["status"] == "Fully grown":
##            self.crop_view.switch_scene(4)
        
def main():
    animal_simulation = QApplication(sys.argv)
    animal_window = AnimalWindow()
    animal_window.show()
    animal_window.raise_()
    animal_simulation.exec_()

if __name__ == "__main__":
    main()
