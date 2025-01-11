# arithmetic operator sample python codes.
## arithmetic 
print(1*2+9*5/90-12)
##comparsion
num1 = int(input("enter the num1 :"))
num2 = int(input("enter the num2 :"))
print(num1 ==num2)
print(num1 !=num2)
print(num1 >num2)
print(num1 <num2)
print(num1 >=num2)
print(num1 <=num2)

##logical and ,or ,not
#method 1
x = False
y = True
print(x and y)
print(x or y)
print('x',not x,'y',not y)
#method 2
x = int(input("enter the x :"))
y = int(input("enter the y :"))
print(x and y)
print(x or y)
print('x',not x,'y',not y)
#method3
x = int(input("enter the x :"))
y = int(input("enter the y :"))
print(x<1 and y>0)
print(x>0 or y<3)
print('x',not x,'y',not y)

##bitwise
b=1
b<<=2
print("check left shift one line assignment b :",b)
b=1
b>>=2
print("check right shift one line assignment b :",b)
b=9
b=~b
print("negation of b: ",b)
##floor division
a = int(input("enter the a :"))
b = int(input("enter the b :"))
print('floor division operator:',a//b)
##assignment
a =5
b =6
c= a+b
print("a",a,"b",b,"c",c)
a+=2
print("check add one line assignment a :",a)
b-=2
print("check sub one line assignment b :",b)
a*=2
print("check mul one line assignment a :",a)
c+=2
print("check add one line assignment c :",c)
a/=2
print("check division one line assignment a :",a)

##identity

##membership
