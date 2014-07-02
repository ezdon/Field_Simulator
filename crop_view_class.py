from PyQt4.QtGui import *

import resources

class CropView(QGraphicsView):
    """provides a graphics view that has the resources for displaying crop
       status visually."""

    def __init__(self):
        super().__init__()

    def resources(self,crop_type):
        #get the graphics
        seed = QPixmap(":/{0}_seed.png".format(crop_type))
        seedling = QPixmap(":/{0}_seedling.png".format(crop_type))
        young = QPixmap(":/{0}_young.png".format(crop_type))    
        mature = QPixmap(":/{0}_mature.png".format(crop_type))   
        old = QPixmap(":/{0}_old.png".format(crop_type))

        crop_pictures = [seed,seedling,young,mature,old]

        #add graphics to scenes
        self.crop_scenes = []
        for each in crop_pictures:
            self.crop_scenes.append(QGraphicsScene())
            self.crop_scenes[-1].addPixmap(each)
        self.setScene(self.crop_scenes[0]) #set the initial scene

    def switch_scene(self,scene):
        self.setScene(self.crop_scenes[scene])


class WheatView(CropView):
    def __init__(self):
        super().__init__()
        self.resources("wheat")

class PotatoView(CropView):
    def __init__(self):
        super().__init__()
        self.resources("potato")
        
            
            
            

    
