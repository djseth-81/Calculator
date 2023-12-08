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
        returns the current saved val1 as a string
    getVal2():
        returns the current saved val2 as a string
    getAnswer():
        returns the current saved answer as a float
    getDisplayVal():
        returns the current value displayed by the GUI as a string
    getOperation():
        returns the selected operation as a string
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
    def updateDisplay(self) -> None:
        """
        Updates the value in displayBox.
        """
        self.displayBox.setText(self.__displayVal)

    def enterValue(self, val: str) -> None:
        """
        Appends a value to the end of the displayVal.

        :param val: string value to be appended to displayVal
        """
        if self.__displayVal == "0": # when displayVal is 0
            if re.findall("[1-9]", val): # resets 0 to most significant digit
                self.__displayVal = val
            elif val == ".": # appends decimal
                self.__displayVal += val
        elif self.__displayVal == f"{self.__ans:.2f}" or len(re.findall("[a-zA-Z]", self.__displayVal)) > 0: # if answer has been displayed on screen after an operation, replace with a new value
            self.__displayVal = val
        elif re.findall("\.+", self.__displayVal) and val == ".": # When the decmial place is already defined
            pass
        else: # append val otherwise
            self.__displayVal += val
        self.updateDisplay() # updates GUI displayBox

    def setDisplay(self, val: str) -> None:
        """
        Sets value to the passed parameter val.
        
        :param val: string value that will replace current value of displayVal
        """
        # intended for use in compute()
        self.__displayVal = val
        self.updateDisplay() # updates GUI displayBox

    def setOperation(self, val: str) -> None: 
        """
        Records the operation that will need to be computed.

        :param val: string value representing operation to run when compute() is called
        """
        self.__val1 = self.__displayVal # if no val2 is assigned, assign to displayVal
        if len(self.__val2) > 0: # if a value is assigned to val2, wipe it
            self.__val2 = ""
        self.setDisplay("0")
        self.__operation = val # assigns operand for computation

    def compute(self) -> None:
        """
        Computes the recorded arithmetic operation and displays the answer to the GUI.
        """
        if len(self.__val2) == 0: # if no val2 is assigned, assign to displayVal
            self.__val2 = self.__displayVal

        # case block for each different operation
        try:
            if self.__operation == "add":
                self.__ans = add(self.__val1, self.__val2)
            elif self.__operation == "subtract":
                self.__ans = subtract(self.__val1, self.__val2)
            elif self.__operation == "multiply":
                self.__ans = multiply(self.__val1, self.__val2)
            elif self.__operation == "divide":
                self.__ans = divide(self.__val1, self.__val2)
            elif self.__operation == "power":
                self.__ans = power(self.__val1, self.__val2)
            self.__val1 = str(self.__ans) # assigning ans to val1
            self.setDisplay(f"{self.__ans:.2f}") # displays answer to lableDisplay
        except (ValueError, ZeroDivisionError): # If an undefined error was thrown during an operation
            self.setDisplay("UNDEF")

    def reset(self) -> None:
        """
        Resets all instance variables to their default state.
        Intended for the Clear button.
        """
        self.__displayVal = "0"
        self.__val1 = ""
        self.__val2 = ""
        self.__operation = ""
        self.__ans = 0.0
        self.updateDisplay()

    ### Accessors ###
    def getVal1(self) -> str:
        """
        Returns the current val1 value as a string.
        """
        return self.__val1
    
    def getVal2(self) -> str:
        """
        Returns the current val2 value as a string.
        """
        return self.__val2

    def getAnswer(self) -> float:
        """
        Returns the current ans value as a float.
        """
        return self.__ans

    def getDisplayVal(self) -> str: 
        """
        Returns the current displayed text in the GUI as a string.
        """
        return self.displayBox.text().strip()

    def getOperation(self) -> str:
        """
        Returns the currently selected operation as a string.
        """
        return self.__operation

    def __str__(self) -> str:
        """
        Returns a formatted string to print the instance variables to the console.
        """
        return f"view={self.getDisplayVal()}, x={self.getVal1()}, y={self.getVal2()}, Operation={self.getOperation()}, Answer={self.getAnswer()}"
