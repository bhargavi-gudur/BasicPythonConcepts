# Write a program that prints the numbers from 100 to 300 
# that are divisible by 3 or 5.        
                
num1 = int(input("enter the value counter value : "))

def divisiable3and5(number):
    while number >= 100 and number <= 300:
        if number % 3 == 0:
            print(f"{number} is  divisible by 3")
        elif number % 5 == 0:
            print(f"{number} is  divisible by 5")
        else:
            print(f"{number} is not divisible by 3 or 5")
        number += 1

divisiable3and5(num1)
