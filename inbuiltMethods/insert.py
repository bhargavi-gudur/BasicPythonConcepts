# sample python insert method.
data =[12,33,45,24,56,90]
print("before inserting value :",data)
# insert at 4 inserting 67
data.insert(4,64)
print("after inserting value :",data)

#index method
for i in data:
 print(data.index(i),i)

#for loop take list  and printing on screen.
data =[]
num =int(input("user enter the how many number put in list:"))
for i in range(num):
  values = int(input(f"enter the value {i+1}: "))
  data.append(values)
  i =i+1

# other for loop to print list 
for i in range(num):
  print("values :",data[i])
  i =i+1