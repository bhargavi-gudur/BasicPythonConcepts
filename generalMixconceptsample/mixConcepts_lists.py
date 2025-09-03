''' 
 This code is a sample of various list operations in Python, 
 including creation, iteration, summation, and modification of lists.
'''
numbers = [10, 20, 30]
# Write your code here

for i in numbers:
    print(i)


def list_number():
    list_var = [10, 20, 30]
    print(list_var)


list_number()


# Write your code here


def sum1():
    sum_var = 0
    numbers = [10, 20, 30]
    for i in numbers:
        sum_var += i

    print(sum_var)


sum1()

user_input_N = int(input(" "))


def get_integer():
    numbers = [10, 200, 300, 1000]
    if user_input_N in numbers:
        print("Yes")
    else:
        print("No")


get_integer()


def sumof_lists():
    # Take input from the user and create a list
    numbers = list(
        map(int, input("Enter numbers separated by spaces: ").split()))

    # Iterate through the list and calculate the sum
    sum_var = 0
    for num in numbers:
        sum_var += num

    print("Sum of the numbers:", sum_var)


sumof_lists()

map_conversionTOlists = map(int, input(
    "Enter numbers separated by spaces: ").split())
numbers = list(map_conversionTOlists)
print(numbers)

# Write your code here to change the third element
def change_third_element():
    numbers = [10, 20, 30, 40, 50, 60, 70]
    numbers[2] = 1000
    print(numbers)


def changenumber():
    numbers = [10, 20, 30, 40, 50, 60, 70]
    # valuechanges = int(input())
    # numbers[2]=valuechanges4
    numbers[2] = 1000
    print(numbers)
changenumber()

def clear_list():
    numbers = [10, 20, 30, 40, 50, 60, 70]
    numbers[:] = []
    print(numbers)
clear_list()

# Write your code here to insert a number at a given position
numbers = [10, 20, 30, 40, 50]
# Take inputs from user
pos = int(input("Enter the position: "))
insert_num = int(input("Enter the number to insert: "))

# Check if position is valid
if pos < 0 or pos > len(numbers):  # Invalid position condition
    print("Invalid")
else:
    # Insert the number at the specified position
    numbers.insert(pos, insert_num)
    print(numbers)
