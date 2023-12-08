"""
:Author: Seth Johnson
:Date: 12-06-2023
:Description:

Unit tests for the formulas module that will be used in the Calculator application.

Assumptions: Type str is the default
"""
"""
TODO:
- operators handle non-digit strings properly
- operators handle UNDEF or NULL results and displays them properly
- operators provide proper outputs for:
    - floats: one +/-, both + and both -
    - str: one +/-, both + and both -
    - Sufficiently large, and sufficiently small numbers
"""
### Import packages ###
import math
import unittest
from formulas import *

### Test class ###
class MyTestCases(unittest.TestCase):

    DELTA = 0.001 # allowable deviation

    def test_add(self):
        ### Validating the actual math ###
        # Small numbers, large numbers, and conventional numbers
        self.assertAlmostEqual(add('2', '3'), 5.0, delta=self.DELTA) # One digit
        self.assertAlmostEqual(add('0.0001', '.0002'), 0.0003, delta=self.DELTA) # small numbers 
        self.assertAlmostEqual(add('200000', '300000'), 500000.0, delta=self.DELTA) # large numbers 

        ### What happens if the data cannot be converted to type float?
        # Passed parameters are not numbers
        self.assertRaises(ValueError, add, 'x', '3')
        self.assertRaises(ValueError, add, '2', 'y')
        self.assertRaises(ValueError, add, 'x', 'y')

        ### What happens if inputs are not positive?
        # Passing zero as a parameter
        self.assertAlmostEqual(add('2', '0'), 2.0, delta=self.DELTA)
        self.assertAlmostEqual(add('0', '3'), 3.0, delta=self.DELTA)
        self.assertAlmostEqual(add('0', '0'), 0.0, delta=self.DELTA)
        # Passing a negative value
        self.assertAlmostEqual(add('-2', '3'), 1.0, delta=self.DELTA)
        self.assertAlmostEqual(add('2', '-3'), -1.0, delta=self.DELTA)
        self.assertAlmostEqual(add('-2', '-3'), -5.0, delta=self.DELTA)
        
    
    def test_subtract(self):
        ### Validating the actual math ###
        # Small numbers, large numbers, and conventional numbers
        self.assertAlmostEqual(subtract('2', '3'), -1.0, delta=self.DELTA) # One digit
        self.assertAlmostEqual(subtract('0.0002', '.0001'), 0.0001, delta=self.DELTA) # small numbers 
        self.assertAlmostEqual(subtract('500000', '200000'), 300000.0, delta=self.DELTA) # large numbers 

        ### What happens if the data cannot be converted to type float?
        # Passed parameters are not numbers
        self.assertRaises(ValueError, subtract, 'x', '3')
        self.assertRaises(ValueError, subtract, '2', 'y')
        self.assertRaises(ValueError, subtract, 'x', 'y')

        ### What happens if inputs are not positive?
        # Passing zero as a parameter
        self.assertAlmostEqual(subtract('2', '0'), 2.0, delta=self.DELTA)
        self.assertAlmostEqual(subtract('0', '3'), -3.0, delta=self.DELTA)
        self.assertAlmostEqual(subtract('0', '0'), 0.0, delta=self.DELTA)
        # Passing a negative value
        self.assertAlmostEqual(subtract('-2', '3'), -5.0, delta=self.DELTA)
        self.assertAlmostEqual(subtract('2', '-3'), 5.0, delta=self.DELTA)
        self.assertAlmostEqual(subtract('-2', '-3'), 1.0, delta=self.DELTA)
    
    def test_multiply(self):
        ### Validating the actual math ###
        # Small numbers, large numbers, and conventional numbers
        self.assertAlmostEqual(multiply('2', '3'), 6.0, delta=self.DELTA) # One digit
        self.assertAlmostEqual(multiply('0.0002', '0.0001'), 0.000000002, delta=self.DELTA) # small numbers 
        self.assertAlmostEqual(multiply('200000', '300000'), 60000000000.0, delta=self.DELTA) # large numbers 

        ### What happens if the data cannot be converted to type float?
        # Passed parameters are not numbers
        self.assertRaises(ValueError, multiply, 'x', '3')
        self.assertRaises(ValueError, multiply, '2', 'y')
        self.assertRaises(ValueError, multiply, 'x', 'y')

        ### What happens if inputs are not positive?
        # Passing zero as a parameter
        self.assertAlmostEqual(multiply('2', '0'), 0.0, delta=self.DELTA)
        self.assertAlmostEqual(multiply('0', '3'), 0.0, delta=self.DELTA)
        self.assertAlmostEqual(multiply('0', '0'), 0.0, delta=self.DELTA)
        # Passing a negative value
        self.assertAlmostEqual(multiply('-2', '3'), -6.0, delta=self.DELTA)
        self.assertAlmostEqual(multiply('2', '-3'), -6.0, delta=self.DELTA)
        self.assertAlmostEqual(multiply('-2', '-3'), 6.0, delta=self.DELTA)
    
    def test_divide(self):
        ### Validating the actual math ###
        # Small numbers, large numbers, and conventional numbers
        self.assertAlmostEqual(divide('2', '3'), 0.667, delta=self.DELTA) # One digit
        self.assertAlmostEqual(divide('0.0001', '0.0002'), 0.5, delta=self.DELTA) # small numbers 
        self.assertAlmostEqual(divide('200000', '300000'), 0.667, delta=self.DELTA) # large numbers 

        ### What happens if the data cannot be converted to type float?
        # Passed parameters are not numbers
        self.assertRaises(ValueError, divide, 'x', '3')
        self.assertRaises(ValueError, divide, '2', 'y')
        self.assertRaises(ValueError, divide, 'x', 'y')

        ### What happens if inputs are not positive?
        # Passing zero as a parameter
        self.assertRaises(ZeroDivisionError, divide, '2', '0')
        self.assertAlmostEqual(divide('0', '3'), 0.0, delta=self.DELTA)
        self.assertRaises(ZeroDivisionError, divide, '0', '0')
        # Passing a negative value
        self.assertAlmostEqual(divide('-2', '3'), -0.667, delta=self.DELTA)
        self.assertAlmostEqual(divide('2', '-3'), -0.667, delta=self.DELTA)
        self.assertAlmostEqual(divide('-2', '-3'), 0.667, delta=self.DELTA)
    
    def test_power(self):
        ### Validating the actual math ###
        # Small numbers, large numbers, and conventional numbers
        self.assertAlmostEqual(power('2', '3'), 8.0, delta=self.DELTA) # One digit
        self.assertAlmostEqual(power('0.0002', '3'), 1.00, delta=self.DELTA) # small base
        self.assertAlmostEqual(power('2', '0.003'), 1.00, delta=self.DELTA) # small exponent

        self.assertAlmostEqual(power('200000', '3'), 8000000000000000.0, delta=self.DELTA) # large base
        self.assertAlmostEqual(power('2', '80'), 1208925819614629174706176.0, delta=self.DELTA) # large exponent
        self.assertRaises(ValueError, power, '2', '100') # too large of an exponent

        ### What happens if the data cannot be converted to type float?
        # Passed parameters are not numbers
        self.assertRaises(ValueError, power, 'x', '3')
        self.assertRaises(ValueError, power, '2', 'y')
        self.assertRaises(ValueError, power, 'x', 'y')

        ### What happens if inputs are not positive?
        # Passing zero as a parameter
        self.assertAlmostEqual(power('2', '0'), 1.0, delta=self.DELTA)
        self.assertAlmostEqual(power('0', '3'), 0.0, delta=self.DELTA)
        self.assertRaises(ValueError, power, '0', '0')
        # Passing a negative value
        self.assertAlmostEqual(power('-2', '3'), -8.0, delta=self.DELTA)
        self.assertAlmostEqual(power('2', '-3'), 0.125, delta=self.DELTA)
        self.assertAlmostEqual(power('-2', '-3'), -0.125, delta=self.DELTA)

if __name__ == "__main__":
    unittest.main()