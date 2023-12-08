"""
:Author: Seth Johnson
:Date: 12-04-2023
:Description:
This file executes the Calculator application. It calls logic.Calulator to initiate the GUI and perform logic operations
"""
### Import packages ###
from gui import *
from logic import *

### Variable Declaration ###

### UDF Declaration ###

## Main Function ##
def main():
    """
    Callstack:
    main.py > logic.Logic() > gui.GUI().setupGUI()
    """
    app = QApplication([]) # Generate an application
    applet = Calculator() # Calling Calculator object to initiate applet
    applet.show() # Calls window to show
    app.exec() # Execute application

"""
TODO:
Features
    - can perform consecutive operations when hitting compute
    - displays "UNDEF" when an operation is undefined
Updates
    - add performing computations inbetween switching operators
    - add allowing to flip between pos and neg
"""

if __name__ == "__main__":
    main()
    print("Ran locally")