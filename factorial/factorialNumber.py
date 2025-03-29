# this program  given number to find the factorial of the number .
# To take input from the user
num = int(input("Enter a number: "))

def factorial(num):
    factorial = 1
    if num < 0:
        print(num, "Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print(num, "The factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            factorial = factorial * i
            print(f"inside the loop {i} , the factorial :{factorial} ")
        print(f"The factorial of '{num}' is , {factorial}")

factorial(num)
