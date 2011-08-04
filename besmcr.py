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
        self.character_filename = ""
        
        # Initalise a bunch of poop
        self.update_stats()
    
    # --------------------------------------------------------------------------
    
    def update_for_new_character(self):
        """Inserts info from the character into the text boxes"""
        self.ui.nameEdit.setText(self.character.name)
        self.ui.ageEdit.setText(self.character.age)
        self.ui.heightEdit.setText(self.character.height)
        self.ui.weightEdit.setText(self.character.weight)
        self.ui.notesEdit.setText(self.character.notes) 
        
        self.ui.bodySpin.setValue(self.character.body)
        self.ui.mindSpin.setValue(self.character.mind)
        self.ui.soulSpin.setValue(self.character.soul)
        
        self.update_stats()
            
    def update_stats(self):
        """Updates the dervived stat text boxes"""
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
        self.ui.statusBar.showMessage("Character Points: " +
            str(self.character.get_remaining_character_points()))
        
    # --------------------------------------------------------------------------
    
    @QtCore.pyqtSlot(str)
    def on_nameEdit_textEdited(self, s):
        self.character.name = s
        
    @QtCore.pyqtSlot(str)
    def on_ageEdit_textEdited(self, s):
        self.character.age = s
    
    @QtCore.pyqtSlot(str)
    def on_weightEdit_textEdited(self, s):
        self.character.weight = s
        
    @QtCore.pyqtSlot(str)
    def on_heightEdit_textEdited(self, s):
        self.character.height = s
        
    @QtCore.pyqtSlot()
    def on_notesEdit_textChanged(self):
        self.character.notes = self.ui.notesEdit.toPlainText()
    
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
        
    # --------------------------------------------------------------------------
    
    @QtCore.pyqtSlot()
    def on_actionNew_triggered(self):
        self.character = character.Character()
        self.update_for_new_character()  
    
    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        filename = QtGui.QFileDialog.getOpenFileName(filter="YAML (*.yaml)")
        if filename:
            self.character_filename = filename
            self.character = character.load(filename)
            
            self.update_for_new_character()       
        
        self.ui.statusBar.showMessage("Opened: " + filename)
    
    # --------------------------------------------------------------------------
    
    @QtCore.pyqtSlot()
    def on_actionSave_triggered(self):
        # Check if we already have a filename in use
        if not self.character_filename:
            filename = QtGui.QFileDialog.getSaveFileName(filter="YAML (*.yaml)")
        else:
            filename = self.character_filename
            
        # Okay check if we actually have a real filename again
        if filename:
            self.character.save(filename)
            self.character_filename = filename
            
        self.ui.statusBar.showMessage("Saved: " + filename)
        
    @QtCore.pyqtSlot()
    def on_actionSave_As_triggered(self):
        filename = QtGui.QFileDialog.getSaveFileName(filter="YAML (*.yaml)")
            
        # Okay check if we actually have a real filename again
        if filename:
            self.character.save(filename)
            self.character_filename = filename
            
        self.ui.statusBar.showMessage("Saved: " + filename)

# ==============================================================================

if __name__ == "__main__":
    # Create our app object and show the main window
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    # Let Qt handle the rest
    sys.exit(app.exec_())
    
