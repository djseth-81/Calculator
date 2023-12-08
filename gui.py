"""
:Author: Seth Johnson
:Date: 12-06-2023
:Description:
This script contains the class CalculatorGUI. This is called by logic.py to generate the PyQt6 GUI object and necessary widgets to simulate a Calculator.
"""

### Import packages ###
from PyQt6 import QtCore, QtGui, QtWidgets

### Class definition ###
class CalculatorGUI(object):

    """
    GUI class that configures and builds the GUI for the TV remote
    Attributes
    ----------
    centralwidget : QWidget
        widget object that will possess all other widgets for this GUI
    displayBox : QLabel
        displays the provided or computed values
    button0 : QPushButton
        calls the Calculator.enterValue("0") method
    button1 : QPushButton
        calls the Calculator.enterValue("1") method
    button2 : QPushButton
        calls the Calculator.enterValue("2") method
    button3 : QPushButton
        calls the Calculator.enterValue("3") method
    button4 : QPushButton
        calls the Calculator.enterValue("4") method
    button5 : QPushButton
        calls the Calculator.enterValue("5") method
    button6 : QPushButton
        calls the Calculator.enterValue("6") method
    button7 : QPushButton
        calls the Calculator.enterValue("7") method
    button8 : QPushButton
        calls the Calculator.enterValue("8") method
    button9 : QPushButton
        calls the Calculator.enterValue("9") method
    buttonDOT : QPushButton
        calls the Calculator.enterValue(".") method
    buttonADD : QPushButton
        calls the Calculator.setOperation("add") method
    buttonMINUS : QPushButton
        calls the Calculator.setOperation("subtract") method
    buttonPROD : QPushButton
        calls the Calculator.setOperation("multiply") method
    buttonDIVIDE : QPushButton
        calls the Calculator.setOperation("divide") method
    buttonPOW : QPushButton
        calls the Calculator.setOperation("power") method
    buttonCLEAR : QPushButton
        calls the Calculator.reset() method
    buttonCOMPUTE : QPushButton
        calls the Calculator.compute() method
    
    Methods
    -------
    setupGUI(window: QWidget):
        Generates widgets and window default state
    """

    def setupGUI(self, MainWindow) -> None:
        ### Window presets ###
        MainWindow.setWindowTitle("Calculator")
        MainWindow.setFixedSize(503, 580)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        font = QtGui.QFont()
        font.setPointSize(20)

        ### Generating widgets ###
        # Display Window
        self.displayBox = QtWidgets.QLabel("",parent=self.centralwidget)
        self.displayBox.setGeometry(QtCore.QRect(10, 70, 480, 120))
        font.setKerning(True)
        self.displayBox.setFont(font)
        self.displayBox.setAutoFillBackground(True)
        self.displayBox.setScaledContents(False)
        self.displayBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        # Entry Buttons
        # 1
        self.button1 = QtWidgets.QPushButton("1", parent=self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 220, 80, 61))
        self.button1.setFont(font)
        # 2
        self.button2 = QtWidgets.QPushButton("2", parent=self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(110, 220, 80, 61))
        self.button2.setFont(font)
        # 3
        self.button3 = QtWidgets.QPushButton("3", parent=self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(210, 220, 80, 60))
        self.button3.setFont(font)
        # 4
        self.button4 = QtWidgets.QPushButton("4", parent=self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(10, 300, 80, 61))
        self.button4.setFont(font)
        # 5
        self.button5 = QtWidgets.QPushButton("5", parent=self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(110, 300, 80, 61))
        self.button5.setFont(font)
        # 6
        self.button6 = QtWidgets.QPushButton("6", parent=self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(210, 300, 80, 61))
        self.button6.setFont(font)
        # 7
        self.button7 = QtWidgets.QPushButton("7", parent=self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(10, 380, 80, 61))
        self.button7.setFont(font)
        # 8
        self.button8 = QtWidgets.QPushButton("8", parent=self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(110, 380, 80, 61))
        self.button8.setFont(font)
        # 9
        self.button9 = QtWidgets.QPushButton("9", parent=self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(210, 380, 80, 61))
        self.button9.setFont(font)
        # 0
        self.button0 = QtWidgets.QPushButton("0", parent=self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(110, 460, 80, 61))
        self.button0.setFont(font)
        # Decimal
        self.buttonDOT = QtWidgets.QPushButton(".", parent=self.centralwidget)
        self.buttonDOT.setGeometry(QtCore.QRect(210, 460, 80, 61))
        self.buttonDOT.setFont(font)

        # Operation buttons
        # Subtract
        self.buttonMINUS = QtWidgets.QPushButton("-", parent=self.centralwidget)
        self.buttonMINUS.setGeometry(QtCore.QRect(410, 220, 80, 61))
        self.buttonMINUS.setFont(font)
        # Divide
        self.buttonDIVIDE = QtWidgets.QPushButton("/", parent=self.centralwidget)
        self.buttonDIVIDE.setGeometry(QtCore.QRect(310, 380, 80, 61))
        self.buttonDIVIDE.setFont(font)
        # Multiply
        self.buttonPROD = QtWidgets.QPushButton("*", parent=self.centralwidget)
        self.buttonPROD.setGeometry(QtCore.QRect(310, 300, 80, 61))
        self.buttonPROD.setFont(font)
        # Add
        self.buttonADD = QtWidgets.QPushButton("+", parent=self.centralwidget)
        self.buttonADD.setGeometry(QtCore.QRect(310, 220, 80, 60))
        self.buttonADD.setFont(font)
        # Power
        self.buttonPOW = QtWidgets.QPushButton("^", parent=self.centralwidget)
        self.buttonPOW.setGeometry(QtCore.QRect(310, 460, 80, 60))
        self.buttonPOW.setFont(font)
        # Clear entry
        self.buttonCLEAR = QtWidgets.QPushButton("C", parent=self.centralwidget)
        self.buttonCLEAR.setGeometry(QtCore.QRect(10, 460, 80, 60))
        self.buttonCLEAR.setFont(font)
        # Compute operation
        self.buttonCOMPUTE = QtWidgets.QPushButton("=", parent=self.centralwidget)
        self.buttonCOMPUTE.setGeometry(QtCore.QRect(410, 300, 80, 220))
        self.buttonCOMPUTE.setFont(font)
        
        ### Assemble our window ###
        MainWindow.setCentralWidget(self.centralwidget) # assigning the Window's central widget GUI.centralwidget
        QtCore.QMetaObject.connectSlotsByName(MainWindow) # Compiling window metaobject
