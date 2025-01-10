#python  basic  code related to swapping of two numbers .
# method 1
## swap method using three variable swapping two numbers.
print("method 1 -three variable")
a = input("enter value of a : ")
b = input("enter value of b : ")
print("*****************************")
print("before swapping :")
print("the value of a ",a)
print("the value of b ",b)
print("*****************************")
temp = a
a =b
b =temp 
print("*****************************")
print("after swapping :")
print("the value of a ",a)
print("the value of b ",b)
print("*****************************")
# method 2
## arthimatic operator  with two variable swapping two numbers
print("method 2 -arthimatic operator")
a = int(input("enter value of a : "))
b = int(input("enter value of b : "))
print("*****************************")
print("before swapping :")
print("the value of a ",a)
print("the value of b ",b)
print("*****************************")
a = a+b
b = a-b
a = a-b
print("*****************************")
print("after swapping :")
print("the value of a ",a)
print("the value of b ",b)
print("*****************************")
# method 3 
## x-or method using swapping two numbers
print("method 3 - x-or  ")
a = int(input("enter value of a : "))
b = int(input("enter value of b : "))
print("*****************************")
print("before swapping :")
print("the value of a ",a)
print("the value of b ",b)
print("*****************************")
a = a^b
b = a^b
a = a^b
print("*****************************")
print("after swapping :")
print("the value of a ",a)
print("the value of b ",b)
print("*****************************")