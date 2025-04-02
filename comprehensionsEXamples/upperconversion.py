# This code converts a list of words to uppercase using a list comprehension. 
words =["hello", "world", "python", "rocks","programming"]
def uppercase_word(words):
    uppercase_Words =[i.upper()  for i in words]
    print("Uppercase words:", uppercase_Words)
    
uppercase_word(words)

# Path: comprehensionsEXamples/evennumbers.py
numbers = [1, 2, 3, 4, 5]
def even_num(numbers):
    even_numbers  =[ i for i in numbers if i%2 ==0]
    print("Even numbers:", even_numbers)
even_num(numbers)
