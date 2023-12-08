"""
:Author: Seth Johnson
:Date: 12-04-2023
:Description:
This module contains arithmetic functions to be used within the logic of the Calculator application.

Functions
---------
add(x, y):
    performs addition between two numbers
subtract(x, y):
    performs subtraction between two numbers
multiply(x, y):
    performs multiplication between two numbers
divide(x, y):
    performs division between two numbers
power(x, y):
    performs exponentiation between two numbers
"""

### Import packages ###
import re

### Variable Declaration ###

### UDF Declaration ###
def add(x: str, y: str) -> float:
    """
    Performs an addition between two float values

    :param x: a string value that is converted into a float value
    :param y: a string value that is converted into a float value
    :return: the sum of the floats of x and y
    """
    if len(re.findall("[0-9]", x)) == 0 or len(re.findall("[0-9]", x)) == 0: # Checks if numbers are found in the passed parameters
        raise ValueError
    return  round(float(x),4) + round(float(y), 4)

def subtract(x: str, y: str) -> float:
    """
    Performs a subtraction between two float values
    
    :param x: a string value that is converted into a float value
    :param y: a string value that is converted into a float value
    :return: the difference of the floats of x and y
    """
    if len(re.findall("[0-9]", x)) == 0 or len(re.findall("[0-9]", x)) == 0: # Checks if numbers are found in the passed parameters
        raise ValueError
    return float(x) - float(y)

def multiply(x: str, y: str) -> float:
    """
    Performs a multiplication between two float values

    :param x: a string value that is converted into a float value
    :param y: a string value that is converted into a float value
    :return: the product of the floats of x and y
    """
    if len(re.findall("[0-9]", x)) == 0 or len(re.findall("[0-9]", x)) == 0: # Checks if numbers are found in the passed parameters
        raise ValueError
    return float(x) * float(y)

def divide(x: str, y: str) -> float:
    """
    Performs a division between two float values

    :param x: a string value that is converted into a float value to represent the numerator
    :param y: a string value that is converted into a float value to represent the denominator
    :return: the quotient between the floats of x and y
    """
    if len(re.findall("[0-9]", x)) == 0 or len(re.findall("[0-9]", x)) == 0: # Checks if numbers are found in the passed parameters
        raise ValueError

    if float(y) == 0.0: # Handles 0 as Divisor
        raise ZeroDivisionError("Cannot divide by 0")
    
    return float(x) / float(y)

def power(x: str, y: str) -> float:
    """
    This recursive function calculates the exponent of a number given an exponent.

    :param x: a string value that is converted into a float value to represent the base
    :param y: a string value that is converted into a float value to represent the exponent
    :return: the exponentiation of the floats of x to the y 
    """

    if len(re.findall("[0-9]", x)) == 0 or len(re.findall("[0-9]", y)) == 0: # Checks if numbers are found in the passed parameters
        raise ValueError
    
    # Converting values from str to float 
    base = float(x)
    exp = abs(float(y)) # converts to an absolute value float of the string

    if base == 0.0 and exp == 0.0: # handles 0^0 operation
        raise ValueError("Undefined operation 0^0.")
    
    if base != 0.0 and exp == 0.0: # handles 0 as the exponent
        return 1.0

    # performing power operation
    # if not (exp > 0.0): # Raise error if exponent is not a positive integer
    #     raise ValueError("Exponent is not a positive integer") # Change to work well with the GUI
        
    if exp == 1.0: # base condition
        result = base
    else: # recursive condition
        result = base * power(str(base), str(exp - 1.0)) # Convert params into type str to satisfy  typehinting and RegEx

    return result if (float(y) > 0) else 1 / result # divides 1 by result if y was itially passed as < 0
