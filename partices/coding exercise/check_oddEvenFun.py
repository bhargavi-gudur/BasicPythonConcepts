#approach 1
print("_"*30)
print("approcach 1 using normal print statement")
num = int(input('enter the number :'))
def check_even_odd(num):
    if (num < 0):
        print("invalid number , please enter greater than zero.")
    elif (num > 0):
        for num in range(0, num+1):
            if num % 2 == 0:
              print("it is a even number", "num:", num)
              print("_"*30)
          
            else:
              print("it is a odd number ", "num:", num)
              print("_"*30)
check_even_odd(num)

#approch2
print("_"*30)
print("approcach 2 using f string")
num = int(input('enter the number :'))
print("_"*30)

def check_even_odd(num):
    if (num < 0):
        print(f"invalid number {num} , please enter greater than zero.")
    elif (num > 0):
        for i in range(0, num+1):
            if i % 2 == 0:
              print(f" a even number {i}")
              print("_"*30)

            else:
              print(f" a odd number {i}")
              print("_"*30)
              
check_even_odd(num)
