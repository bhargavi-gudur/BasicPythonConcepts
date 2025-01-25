# program to add digits of a number.
# method 1
num = input("enter the integer : ")
digit1 = int(num[0])
digit2 = int(num[1])
sum = digit1+ digit2
print('the add digit addition :',sum)
# method 2 using for loop
num = input("enter the integer : ")
sum = 0
for digit in num :
    sum = sum + (int(digit))
print("sum of digit number :",sum)