"""
:Author: Seth Johnson
:Date: 12-04-2023
:Description:
This file contians the class Calulator, which is initiated by the main script.
"""
"""
TODO:
- Handle repetitive computation for the same operator
- Handle repetitive computation for different operators
- REMOVE PRINT STRINGS WHEN FINISHED

"""
### Import packages ###
from PyQt6.QtWidgets import *
from gui import *
import re
from formulas import *

### Class definition ###
class Calculator(QMainWindow, CalculatorGUI):
    """
    A class representign a graphical Calculator object

    Attributes
    ----------
    displayVal : str
        The string to be displayed to the user
    val1 : str
        The saved string value that a user has entered after an operation has been selected
    val2 : str
        The saved string value that a user has entered after compute has been executed
    operation : str
        The string value representing which operation is to be executed
    ans : float
        The float value from the resulting computation

    
    Methods
    -------
    updateDisplay():
        updates the value displayed by the GUI
    enterValue(val):
        updates the display string value with a new character chosen by the user
    setDisplay(val):
        sets the display string value to the passed parameter
    setOperation():
        chooses an operation to be computed
    compute():
        performs the operation selected
    reset():
        resets the GUI settings to the default
    getVal1():
        returns the current saved val1 as a float
    getVal2():
        returns the current saved val2 as a float
    getAnswer():
        returns the current saved answer
    getDisplayVal():
        returns the current value displayed by the GUI
    getOperation():
        returns the selected operation
    __str__():
        returns a formatted string by calling the accessors for each of the attributes
    """
    ### Class Variables ###

    ### Constructors ###
    def __init__(self):
        super().__init__()

        ### initialize GUI operations ###
        self.setupGUI(self)

        ### initialize instance variables ###
        self.__displayVal: str = "0"
        self.updateDisplay()
        self.__val1: str = ""
        self.__val2: str = ""
        self.__operation: str = ""
        self.__ans: float = 0.0

        ### Arithmetic operations ###
        self.buttonADD.clicked.connect(lambda : self.setOperation("add"))
        self.buttonMINUS.clicked.connect(lambda : self.setOperation("subtract"))
        self.buttonPROD.clicked.connect(lambda : self.setOperation("multiply"))
        self.buttonDIVIDE.clicked.connect(lambda : self.setOperation("divide"))
        self.buttonPOW.clicked.connect(lambda : self.setOperation("power"))

        ### entry operations ###
        self.button0.clicked.connect(lambda : self.enterValue("0"))
        self.button1.clicked.connect(lambda : self.enterValue("1"))
        self.button2.clicked.connect(lambda : self.enterValue("2"))
        self.button3.clicked.connect(lambda : self.enterValue("3"))
        self.button4.clicked.connect(lambda : self.enterValue("4"))
        self.button5.clicked.connect(lambda : self.enterValue("5"))
        self.button6.clicked.connect(lambda : self.enterValue("6"))
        self.button7.clicked.connect(lambda : self.enterValue("7"))
        self.button8.clicked.connect(lambda : self.enterValue("8"))
        self.button9.clicked.connect(lambda : self.enterValue("9"))
        self.buttonDOT.clicked.connect(lambda : self.enterValue("."))
        
        # envrionment operations
        self.buttonCLEAR.clicked.connect(lambda : self.reset())
        self.buttonCOMPUTE.clicked.connect(lambda : self.compute())

    ### Mutators ###
    def updateDisplay(self) -> None: # updates the value in labelDisplay
        self.displayBox.setText(self.__displayVal)

    def enterValue(self, val: str) -> None: # appends a value to the end of the displayValue
        if self.__displayVal == "0": # when displayVal is 0
            if re.findall("[1-9]", val): # resets 0 to most significant digit
                self.__displayVal = val
            elif val == ".": # appends decimal
                self.__displayVal += val
        elif re.findall("\.+", self.__displayVal) and val == ".": # When the decmial place is already defined
            pass
        elif self.__val1 == self.__displayVal or self.__val2 == self.__displayVal: # if answer has been displayed on screen after an operation, replace with a new value
            self.__displayVal = val
        else: # append val otherwise
            self.__displayVal += val
        self.updateDisplay() # updates GUI labelDisplay
        print(self.__str__()) ### DEBUG

    def setDisplay(self, val: str) -> None: # sets value to the passed parameter val
        # intended for use in compute()
        self.__displayVal = val
        self.updateDisplay()
        print(self.__str__()) ### DEBUG

    def setOperation(self, val: str) -> None: # Determines operation to compute when needed
        print(f"You chose to {val}")
        self.__val1 = self.__displayVal
        print(f"Saving val1 = {self.__val1}")
        self.setDisplay("0")
        self.__operation = val # assigns operand for computation
        print(self.__str__()) ### DEBUG

    def compute(self) -> None:
        self.__val2 = self.__displayVal
        print(f"Saving val2 = {self.__val2}")
        print(f"Computing for {self.__val1} and {self.__val2}")

        # case block for each different operation
        if self.__operation == "add":
            self.__ans = add(self.__val1, self.__val2)
        elif self.__operation == "subtract":
            self.__ans = subtract(self.__val1, self.__val2)
        elif self.__operation == "multiply":
            print(f"{self.__val1} * {self.__val2} = {multiply(self.__val1, self.__val2)}")
            self.__ans = multiply(self.__val1, self.__val2)
        elif self.__operation == "divide":
            self.__ans = divide(self.__val1, self.__val2)
        elif self.__operation == "power":
            self.__ans = power(self.__val1, self.__val2)
        self.__val1 = str(self.__ans) # assigning ans to val1
        self.setDisplay(str(self.__ans)) # displays answer to lableDisplay
        print(self.__str__()) ### DEBUG

    def reset(self) -> None: # reverts the answer, val1, val2, and displayVal to their default state
        # Intended for the Clear button
        self.__displayVal = "0"
        self.__val1 = ""
        self.__val2 = ""
        self.__operation = ""
        self.__ans = ""
        self.updateDisplay()
        print(self.__str__()) ### DEBUG

    ### Accessors ###
    def getVal1(self) -> float: # gets the current float of val1
        return float(self.__val1)
    
    def getVal2(self) -> float: # gets the current float of val2
        return float(self.__val2)

    def getAnswer(self) -> float: # Gets the current answer value
        return self.__ans

    def getDisplayVal(self) -> str: # gets the current displayed text in the GUI
        return self.displayBox.getText()

    def getOperation(self) -> str: # returns the currently selected operation
        return self.__operation

    def __str__(self) -> str:
        return f"view={self.getDisplayVal()}, x={self.getVal1()}, y={self.getVal2()}, Operation={self.getOperation()}, Answer={sel.getAnswer()}"
"""
TODO:
- Calculator 
    - Should be able to continually perform the operation
        - first entry is ANS, second is SECOND USER ENTRY
    - Introduce toggle between positive and negative entries
    - Dropdown to allow searching for old operations?
        - IF SO: add an ALL CLEAR option to GUI
"""