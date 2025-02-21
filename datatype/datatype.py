# sample code in python using multi-datatype using built-in function. 
## primitive data types 
## inbuilt function int(), str() ,float(), type()
## type checking , type error, type conversion and type casting.

#string type
name_1 = "gandla bhargavi"
name_2 = " automotive electonic engineer"
print("printing :" ,name_1,name_2)
print("printing :", name_1+name_2)
# int conversion data type
integer1 =0x123
integer2 =0b1
integer3 =0o123
print("print integer1 :" ,int(integer1))
print("printing integer2:", int(integer2))
print("printing integer2:", int(integer3))
#string conversion
length = len("gandla bhargavi")
character = str(length)
print("your name is "+ character +"\tcharacters")
#string type method 1
length = len("gandla bhargavi")
character = str(length)
print("type of the string  type to find out :",type(character))
print("type of the string  type to find out :",type(length))
# inbuilt function
length = len("gandla bhargavi")
integer =12
print("conversion addition character+ integer:",length+integer)
# example 1
name ="124"
print(10+int(name))
#addition two number ask user 
first_no = int(input("enter first number :"))
second_no = int(input("enter second number :"))
sum = first_no +second_no
print('sum:',sum)
 


