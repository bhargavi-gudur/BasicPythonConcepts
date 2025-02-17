# sample enumerate program
# enumerate program to print index and value.
data =[1,2,4,8,34,67]
for index ,value in enumerate(data):
    print("index : ",index,"value:",value)

# for loop get  data from user list .
num = int(input("enter the value :"))
data_list = []
for i in range(num):
    #if value < 0:
 values = int(input(f" the value{i+1}:")) 
 data_list.append(values)
 #data_list[value]= num

 #step 2 : print the list
 print(" the element in the list are ")
 element = [values for values in enumerate(data_list)]
 print(index,element)