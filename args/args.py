'''
This module contains a function to multiply arbitrary 
numbers of arguments.
'''


def mul(*args):
    value = 1
    print("********************************")
    for convolation in args:
        value *= convolation
        print(f"multiplication in args -> {convolation} ,{value}")
    print(f"Final value: {value}")
    print("********************************")


mul(2, -3, 6, 8)
mul(2, 5, 8, 9, 0, 6)
