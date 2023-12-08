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

"""
TODO:
- FIXME
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
    return  float(x) + float(y)

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
        raise ValueError
    
    return float(x) / float(y) # FIXME: Cannot handle 0 as divisor

def power(x: str, y: str) -> float:
    """
    This recursive function calculates the exponent of a number given an exponent.

    :param x: a string value that is converted into a float value to represent the base
    :param y: a string value that is converted into a float value to represent the exponent
    :return: the exponentiation of the floats of x to the y 
    """
    """
    TODO:
    - handle y <= 0
        - y < 0 -> -1 / x^y
        - y = 0 -> 1
    """
    if len(re.findall("[0-9]", x)) == 0 or len(re.findall("[0-9]", x)) == 0: # Checks if numbers are found in the passed parameters
        raise ValueError
    
    # Converting values from str to float 
    x = float(x)
    y = float(y) # FIXME: cannot handle y <= 0.0

    if x == 0.0 and y == 0.0: # handles 0^0 operation
        raise ValueError("Undefined operation 0^0.")
    
    if x != 0.0 and y == 0.0: # handles 0 as the exponent
        return 1.0

    # performing power operation
    if not (y > 0.0): # Raise error if exponent is not a positive integer
        raise ValueError("exponent is not a positive integer") # Change to work well with the GUI
        
    if y == 1.0: # base condition
        return x
    else: # recursive condition
        return x * power(str(x), str(y - 1.0)) # Convert params into type str to satisfy  typehinting and RegEx

if __name__ == "__main__":
    
    ### DEBUGGING ###
    # add
    print(f"2.0 + 3 = {add('2.0', '3'):.2f}") # = 5.00
    print(f"-2 + 3 = {add('-2', '3'):.2f}") # = 1.00
    print(f"0 + 3 = {add('0', '3'):.2f}") # = 3.00
    # print(f"x + 3 = {add('x', '3'):.2f}") # ValueError
    # print(f"0 + y = {add('0', 'y'):.2f}") # ValueError
    # subtract
    print(f"2 - 3.0 = {subtract('2', '3.0'):.2f}") # = -1.00
    print(f"2 - -3 = {subtract('2', '-3.0'):.2f}") # = 5.00
    print(f"2 - 0 = {subtract('2', '0'):.2f}") # = 2.00
    # multiply
    print(f"2 * 3 = {multiply('2', '3'):.2f}") # = 6.00
    print(f"2 * -3 = {multiply('2', '-3'):.2f}") # = -6.00
    print(f"2 * 0 = {multiply('2', '0'):.2f}") # = 0.00
    # divide
    print(f"2 / 3.0 = {divide('2', '3.0'):.2f}") # = 0.67
    print(f"2 / -3 = {divide('2', '-3'):.2f}") # = -0.67
    print(f"0 / 3 = {divide('0', '3'):.2f}") # = 0.00
    # print(f"2 / 0 = {divide('2', '0'):.2f}") # = Undef # FIXME: cannot handle 0 as divisor
    # power
    print(f"2 ^ 3 = {power('2', '3'):.2f}") # = 8.00
    print(f"-2 ^ 3 = {power('-2', '3'):.2f}") # = -8.00
    print(f"2 ^ 0 = {power('2', '0'):.2f}") # = 1.00
    print(f"0 ^ 3 = {power('0', '3'):.2f}") # = 1.00
    # print(f"2 ^ -3 = {power('2', '-3'):.2f}") # = 0.12 FIXME: y value cannot handle negative exponents
    # print(f"0 ^ 0 = {power('0', '0'):.2f}") # = Undef FIXME: y value is goofed
    
    print("### CONSOLE: `formulas.py` ran locally...")
