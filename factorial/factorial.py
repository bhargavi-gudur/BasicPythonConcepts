#sample program python factorial of the number
number = int(input("enter the factorial of the number:"))
fact = 1
for i in range(1,number+1):
    fact = i*fact
    print("i",i,fact)
print(f"The factorial of {number} is {fact}")