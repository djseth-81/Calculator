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
- formulas.py FIXME
    - Logic.py
    Caclulator
        - allows to flip between pos and neg
        - consecutive same operator computations
        - performing computations inbetween switching operators

"""

if __name__ == "__main__":
    main()
    print("Ran locally")