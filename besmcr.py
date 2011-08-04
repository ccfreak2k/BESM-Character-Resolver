#!/usr/bin/env python
"""
SYNOPSIS

    besmcr.py

DESCRIPTION

    Python program to assist in making a BESM d20 character.

AUTHOR

    ccfreak2k

LICENSE

    This program is licensed under the terms of the BSD license.

VERSION

    $Id$
"""

# ==============================================================================

import os
import sys

from PyQt4 import QtCore
from PyQt4 import QtGui

from besmcr import gui

# ==============================================================================

class MainWindow(QtGui.QMainWindow):
    """Our main Qt window class."""
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # Load the UI files
        self.ui = gui.mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

# ==============================================================================

if __name__ == "__main__":
    # Create our app object and show the main window
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    # Let Qt handle the rest
    sys.exit(app.exec_())
    
