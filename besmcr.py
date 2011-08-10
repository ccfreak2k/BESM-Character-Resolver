import os
import sys

from PyQt4 import QtCore
from PyQt4 import QtGui

# ------------------------------------------------------------------------------

from besmcr import gui
from besmcr import character

# ==============================================================================

class MainWindow(QtGui.QMainWindow):
    """Our main Qt window class."""
        
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # Load the UI files
        self.ui = gui.mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Create a new character instance for us to work with
        self.character = character.Character()
        self.character_filename = ""
        self.update_gui_character_info()
    
    # --------------------------------------------------------------------------
    
    def update_gui(self):
        """Updates the entire GUI"""
        self.update_gui_character_info()
        self.update_gui_derived_stats()
        self.update_gui_spinbox_ranges() 
        
    def update_gui_character_info(self):
        """Inserts info from the character into the text boxes"""
        self.ui.nameEdit.setText(self.character.name)
        self.ui.ageEdit.setText(self.character.age)
        self.ui.heightEdit.setText(self.character.height)
        self.ui.weightEdit.setText(self.character.weight)
        self.ui.notesEdit.setText(self.character.notes) 
        
        self.ui.bodySpin.setValue(self.character.body)
        self.ui.mindSpin.setValue(self.character.mind)
        self.ui.soulSpin.setValue(self.character.soul)
        
        self.ui.cpSpin.setValue(self.character.character_points)
        self.ui.spSpin.setValue(self.character.skill_points)
        
        # Find whatever genre was in our character file in the combo box
        i = self.ui.genreSelection.findText(self.character.genre)
        if i >= 0:
            self.ui.genreSelection.setCurrentIndex(i)
        
    def update_gui_derived_stats(self):
        """Updates the dervived stat text boxes"""
        self.ui.healthEdit.setText(str(self.character.get_health()))
        self.ui.energyEdit.setText(str(self.character.get_energy()))
        self.ui.combatEdit.setText(str(self.character.get_combat()))
        self.ui.defenseEdit.setText(str(self.character.get_defense()))
        self.ui.shockEdit.setText(str(self.character.get_shock()))
        
        self.ui.remainingCpEdit.setText(str(
            self.character.get_remaining_character_points()))
        self.ui.remainingSpEdit.setText(str(self.character.skill_points)) 
            
    def update_gui_spinbox_ranges(self):
        """Adjusts the spinbox ranges to match character point limitations"""
        body_max = self.character.character_points - (self.character.mind + 
            self.character.soul)
        mind_max = self.character.character_points - (self.character.body + 
            self.character.soul)
        soul_max = self.character.character_points - (self.character.body + 
            self.character.mind)
            
        # Even if we can technically spend more than 12, game mechanics do not
        # allow it, so cap it.
        if body_max > 12:
            body_max = 12
        if mind_max > 12:
            mind_max = 12
        if soul_max > 12:
            soul_max = 12
            
        self.ui.bodySpin.setMaximum(body_max)
        self.ui.mindSpin.setMaximum(mind_max)
        self.ui.soulSpin.setMaximum(soul_max)
        
    # --------------------------------------------------------------------------
    
    @QtCore.pyqtSlot(str)
    def on_nameEdit_textEdited(self, s):
        self.character.name = str(s)
        
    @QtCore.pyqtSlot(str)
    def on_ageEdit_textEdited(self, s):
        self.character.age = str(s)
    
    @QtCore.pyqtSlot(str)
    def on_weightEdit_textEdited(self, s):
        self.character.weight = str(s)
        
    @QtCore.pyqtSlot(str)
    def on_heightEdit_textEdited(self, s):
        self.character.height = str(s)
        
    @QtCore.pyqtSlot()
    def on_notesEdit_textChanged(self):
        self.character.notes = str(self.ui.notesEdit.toPlainText())
        
    @QtCore.pyqtSlot(str)
    def on_genreSelection_currentIndexChanged(self, s):
        self.character.genre = str(s)
    
    # --------------------------------------------------------------------------
    
    @QtCore.pyqtSlot(int)
    def on_bodySpin_valueChanged(self, i):     
        self.character.body = int(i)
        self.update_gui()
        
    @QtCore.pyqtSlot(int)
    def on_mindSpin_valueChanged(self, i):    
        self.character.mind = int(i)
        self.update_gui()
        
    @QtCore.pyqtSlot(int)
    def on_soulSpin_valueChanged(self, i):    
        self.character.soul = int(i)
        self.update_gui()
    
    # --------------------------------------------------------------------------
    
    @QtCore.pyqtSlot(int)
    def on_cpSpin_valueChanged(self, i):
        self.character.character_points = int(i)
        self.update_gui()
        
    @QtCore.pyqtSlot(int)
    def on_spSpin_valueChanged(self, i):
        self.character.skill_points = int(i)
        self.update_gui()
        
    # --------------------------------------------------------------------------
    
    @QtCore.pyqtSlot()
    def on_actionNew_triggered(self):
        self.character = character.Character()
        self.update_gui()   
    
    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        filename = QtGui.QFileDialog.getOpenFileName(filter="YAML (*.yaml)")
        if filename:
            self.character_filename = filename
            self.character = character.load(filename)
            
            self.update_gui()     
    
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
        
    @QtCore.pyqtSlot()
    def on_actionSave_As_triggered(self):
        filename = QtGui.QFileDialog.getSaveFileName(filter="YAML (*.yaml)")
            
        # Okay check if we actually have a real filename again
        if filename:
            self.character.save(filename)
            self.character_filename = filename
    
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        """Exits the application."""
        quit()

# ==============================================================================

if __name__ == "__main__":
    # Create our app object and show the main window
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    # Let Qt handle the rest
    sys.exit(app.exec_())
    
