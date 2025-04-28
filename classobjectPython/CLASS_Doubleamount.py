# This code defines a class called MoneyDouble that calculates
# the double amount of money based on a given number.

class MoneyDouble:
    # This class is used to calculate the double amount of money based on a given number.
    # The constructor initializes the object with the given number.
    def __init__(self, num):
        self.number = num
    # This method calculates the double amount of money based on the given number.
    # If the number is 1, it returns 1. Otherwise, it returns double the number minus 2.

    def calculate(self):
        if self.number == 1:
            return 1
        return 2 * (self.number - 1)

# This code creates an instance of the MoneyDouble class with a user-provided
# number and prints the result of the calculation.


# It prompts the user to enter a number, creates an instance of the MoneyDouble
# class with that number,
number = int(input("Enter a number: "))
moneydouble_obj = MoneyDouble(number)
result = moneydouble_obj.calculate()
print(result)
