import os
import sys

from PyQt4 import QtCore
from PyQt4 import QtGui

from besmcr import *

# ==============================================================================

class MainWindow(QtGui.QMainWindow):
    """Our main Qt window class."""
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # Load the UI files
        self.ui = gui.mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Create a new character instance for us to work with
        self.character = character.Character()
        self.character.max_character_points = 20
        
        # Initalise a bunch of poop
        self.update_stats()
    
    # --------------------------------------------------------------------------
    
    def update_stats(self):
        self.ui.healthEdit.setText(str(self.character.get_health()))
        self.ui.energyEdit.setText(str(self.character.get_energy()))
        
        self.ui.combatEdit.setText(str(self.character.get_combat()))
        self.ui.defenseEdit.setText(str(self.character.get_defense()))
        self.ui.shockEdit.setText(str(self.character.get_shock()))
        
        self.update_spinbox_ranges()
        self.update_statusbar()
    
    def update_spinbox_ranges(self):
        body_max = self.character.max_character_points - (self.character.mind + 
            self.character.soul)
        mind_max = self.character.max_character_points - (self.character.body + 
            self.character.soul)
        soul_max = self.character.max_character_points - (self.character.body + 
            self.character.mind)
            
        self.ui.bodySpin.setMaximum(body_max)
        self.ui.mindSpin.setMaximum(mind_max)
        self.ui.soulSpin.setMaximum(soul_max)
    
    def update_statusbar(self):
        self.ui.characterPointsStatus.setText("Character Points: " +
            str(self.character.get_remaining_character_points()))
        
    # --------------------------------------------------------------------------
    
    @QtCore.pyqtSlot(int)
    def on_bodySpin_valueChanged(self, i):     
        self.character.body = i
        self.update_stats()
        
    @QtCore.pyqtSlot(int)
    def on_mindSpin_valueChanged(self, i):    
        self.character.mind = i
        self.update_stats()
        
    @QtCore.pyqtSlot(int)
    def on_soulSpin_valueChanged(self, i):    
        self.character.soul = i
        self.update_stats()

# ==============================================================================

if __name__ == "__main__":
    # Create our app object and show the main window
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    # Let Qt handle the rest
    sys.exit(app.exec_())
    
