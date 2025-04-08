'''This program will take a list of numbers and print 
 the even and odd numbers from the list using list comprehension.'''
 
numbers =[1,2,3,4,5,6,7,8,9,10]
def even_numbers(numbers):
    even_nums =[i for i in numbers if i%2 ==0]
    print("Even numbers are:",even_nums)
def Odd_numbers(numbers):
    odd_nums = [i for i in numbers if (i %2) != 0]
    print("odd_nums numbers are:", odd_nums)

even_numbers(numbers)
Odd_numbers(numbers)

