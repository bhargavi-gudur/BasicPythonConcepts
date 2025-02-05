#delete value in lists
#exercies 1
num =[2,4,15,57,50,2,1,3,4,5,78,82,12,7]
#delete 4 
print("num at 1st index :",num[1])
print("before remove value :",num)
del(num[1])
print("after remove value :",num)

# exercies 2
nums =[25,36,95,14,12,26]
del(nums[2:5])
print("list:",nums)

#exerices 3
#delete value in tuple
nums =(25,36,95,14,12,26)
nums_list = list(nums)  # Convert tuple to list

# Delete elements from index 2 to 4 (inclusive)
del nums_list[2:5]

# Convert list back to tuple
nums =  tuple(nums_list)
print("tuple : ",nums)