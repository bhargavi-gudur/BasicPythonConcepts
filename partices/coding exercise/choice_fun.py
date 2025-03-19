# Write a program that performs the tasks of a simple calculator. 
# The program should first take an integer as input and then based on that integer perform the task as given below.
# If the input is 1, 2 integers are taken from the user and their sum is printed.    
a = int(input("enter the a value : "))
b = int(input("enter the b value : "))
choice = input("enter the choice : ")


def arithmetic(choice_operator):
  if choice == 'pow':
      c = a**b
      print("pow", c)
  elif choice == 'mod':
      c = a % b
      print("mod", c)


arithmetic(choice)
