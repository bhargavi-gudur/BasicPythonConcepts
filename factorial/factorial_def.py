#alternate approach
# Define the function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input
number = int(input("Enter the number to calculate the factorial: "))

# Calculate the factorial and display the result
result = factorial(number)
print(f"The factorial of {number} is {result}")
