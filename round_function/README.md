# Python Round Function

This project demonstrates the use of the `round` function in Python to round numbers to a specified number of decimal places.

## Usage

The `round` function takes two arguments:
1. The number to be rounded.
2. The number of decimal places to round to (optional).

If the second argument is omitted, the number is rounded to the nearest integer.

## Examples

```python
# Rounding integers and floating point numbers
print(round(7))           # Output: 7
print(round(7, 2))        # Output: 7
print(round(7.2344))      # Output: 7
print(round(7.666, 2))    # Output: 7.67
print(round(7.645672, 0)) # Output: 8.0
print(round(7.5))         # Output: 8
print(round(6.5))         # Output: 6
print(round(3.5))         # Output: 4

# Using the round function with different ndigits values
print(round(674, 2))      # Output: 674
print(round(674, 0))      # Output: 674.0
print(round(674, -2))     # Output: 700
print(round(665, -1))     # Output: 670
print(round(645, -1))     # Output: 640
print(round(675, 1))      # Output: 675.0
print(round(675.678889, 1)) # Output: 675.7
print(round(675.9, -1))   # Output: 680

# Type of the rounded result
print("type: ", type(round(675.9, -1)))  # Output: <class 'int'>
