#typeconversion string to int add numbers
a = input("enter the number a: ")
b = input("enter the number b:")

def stringtoint(a,b):
    if len(a) < 1 or len(b) < 2:  # Ensure sufficient length for indexing
        print("Error: Input strings are too short.")
        return
    first = a[0]
    second = b[1]
   
    try:
        int_sum = int(first) + int(second)
        print("Sum of string to int:", int_sum)
        
    except ValueError:
        try:
            str_float = float(first)
            print("string to float:", str_float)  
        
        except ValueError:
            print("Error: Unable to convert characters to floating adding two numbers.")
 
stringtoint(a,b)
