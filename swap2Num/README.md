# Python Basic Code for Swapping Two Numbers

## Overview

This project demonstrates various methods for swapping the values of two numbers in Python. It includes three different techniques: using a temporary variable, using arithmetic operators, and using the XOR bitwise operator.

## Code Explanation

### Method 1: Swap using Three Variables

This method uses a temporary variable to hold one of the values during the swap process.

**Steps:**
1. Prompt the user to enter values for `a` and `b`.
2. Print the values before swapping.
3. Use a temporary variable `temp` to hold the value of `a`.
4. Assign the value of `b` to `a`.
5. Assign the value of `temp` (original value of `a`) to `b`.
6. Print the values after swapping.

### Method 2: Swap using Arithmetic Operators

This method uses arithmetic operations to swap the values without a temporary variable.

**Steps:**
1. Prompt the user to enter integer values for `a` and `b`.
2. Print the values before swapping.
3. Add `a` and `b` and store the result in `a`.
4. Subtract the new value of `a` by `b` and store the result in `b`.
5. Subtract the new value of `a` by the new value of `b` and store the result in `a`.
6. Print the values after swapping.

### Method 3: Swap using XOR Bitwise Operator

This method uses the XOR bitwise operator to swap the values without a temporary variable.

**Steps:**
1. Prompt the user to enter integer values for `a` and `b`.
2. Print the values before swapping.
3. Apply the XOR operation between `a` and `b` and store the result in `a`.
4. Apply the XOR operation between the new value of `a` and `b` and store the result in `b`.
5. Apply the XOR operation between the new value of `a` and the new value of `b` and store the result in `a`.
6. Print the values after swapping.

## Running the Code

1. Run the Python script.
2. Enter the requested inputs when prompted.
3. Observe the outputs displayed on the console.

## Tips

- Ensure that the inputs are in the correct format (integers for methods 2 and 3).
- Use meaningful prompts to guide the user in providing the correct input.

## Conclusion

This project helps you understand various ways to swap the values of two numbers in Python using different techniques.
