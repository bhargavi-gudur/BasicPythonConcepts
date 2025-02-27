#identity operator
#sample python codeis, is not
#example 1
a = 5
b = 8
print("a is not b : ", a is not b)
print("a is b:", a is b)
print("memory allocation ids:\n","a:",id(a),"b:", id(b))
# example 2
a=40
print("id of a:",id(a))
a=34
b=a+1
print("id of a:",id(a))
print("check a is a:",a is a)
print("id of b:", id(b))
print("check a is b:", a is b)