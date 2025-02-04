#copying list in other list using append method.
print("append method,copying list")
data =[1,2,56,67,35]
cpy_data =[]

for i in range(len(data)):
 cpy_data.append(data[i]) # Create a copy of the list using append
 print(cpy_data[i])
 
print("cpy_data:",cpy_data)
print("data:",data)


# without append method
print("silcing method,copying list")
data =[1,2,56,67,35]
cpy_data = data[ : ] # Create a copy of the list using slicing
for i in range(len(data)):
 print(cpy_data[i])
print("cpy_data:",cpy_data)
print("data:",data)
