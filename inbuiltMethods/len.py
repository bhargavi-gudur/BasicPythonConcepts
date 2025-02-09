# sample lenght function python code
# len function returns number of items in an objects.
#such as lists,string , tuples, dictionary.

#example :len()
data =[1,2,45,67,90]
lenght =  len(data)
print("len:",lenght)

#example:range() and len()
data =[1,2,45,67,90]
lenght =  range(len(data))
print("range and len :",lenght)

#example:range()
# this function generates a sequences of numbers.
#  for loop to iterate over a sequence of numbers.
data =[1,2,45,67,90]
for i in range(5):
    print(f"index:{i} , data:{data[i]} ")
