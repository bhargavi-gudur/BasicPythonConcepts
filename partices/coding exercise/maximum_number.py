#program to find maximum from a list of numbers.
list_max =[1,2,31,35,3112,23,45,32,41,592]

# using with inbuilt function 
for i in list_max:
    print("list of number :",i)
print("max number :",max(list_max))
print("*********************************************************")
#separator to find maximum from a list of numbers.
numbers =input('enter list of numbers:')
number_lists =numbers.split(",")
print(number_lists)
for i in range(0,len(number_lists)):
    number_lists[i] =int(number_lists[i])
print("max number :",max(number_lists))

print("*********************************************************")
#separator to find maximum from a list of numbers.
# without max function
numbers =input('enter list of numbers:')
number_lists =numbers.split(",")
print(number_lists)
# this iterate convert string to integer type lists
for i in range(len(number_lists)):
    number_lists[i] =int(number_lists[i])

# Initialize the maximum number with the first element
max_number = number_lists[0]

# Iterate through the list to find the maximum number.
for num in number_lists:
    if num > max_number:
        max_number = num 

# Print the list of numbers from user input
print("List of numbers from user input:", number_lists)

# Print the maximum number
print("Max number:", max_number)
print("*********************************************************")