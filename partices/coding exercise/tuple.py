#sample creating a tuple
my_tuple =(1,2,3,44,56,42,22)
print("**********************************")
#index of an element
print("index : ",my_tuple.index(44))
#accessing element in a tuple
print(my_tuple[0],my_tuple[1],my_tuple[2],my_tuple[3],my_tuple[4],my_tuple[5],my_tuple[6])
print("**********************************")
#for loop sample creating .
my_tuple1 =(1,2,3,4,5,42,22)
#for accessing the element in a tuple.
for i in my_tuple1:
    print("tuple :" ,i)
print("**********************************")
#for loop sample using inbuilt len function
my_tuple1 = (1,2,3,4,5,42,22)
#count the number of ocuurences of and elements
print("count : ",my_tuple1.count(22))
#index of an element
print("index : ",my_tuple1.index(4))
#for accessing the element in a tuple.
for i in range(len(my_tuple1)):
    print("lenght_tuple :" ,i,"my_tuple1 ->",my_tuple1[i] )
print("**********************************")
# nested tuples
nested_tuples = (1,(2,3),(3,4,5))
#accessing the elements in a nested tuples
print(nested_tuples[0])
for i in range(len(nested_tuples)):
    print("nested tuples :",nested_tuples[i])
print("**********************************")
#tuple packing
packed_tuple =1,2,"apple",3.14
#tuple unpacking 
a ,b,c,d = packed_tuple
print(a,b,c,d)
print("**********************************")