#sample python code lists 
print('method 1 lists')
numbers = [10,1,0,2,3,3,4]
for loop in numbers: 
    print(f"List item: {loop}")
#len inbuilt function to list size
print("length:",len(numbers))

# alternate method
# using range inbuilt function list will iterate 
# and print on screen
print('method 2 lists ')
numbers = [10,1,0,2,3,3,4]
for loop in range(len(numbers)): 
    print(f"List item: {loop}")
#len inbuilt function to list size
print("length:",len(numbers))

# slicing lists 
print(' lists silcing  ')
numbers = [10,1,0,2,3,3,4]
print("slicing :", numbers[0:5])
print("extending silicing :",numbers[0:6:5])

#inbuild sort ()
print(' lists sort  ')
numbers = [10,1,0,2,3,3,4]
numbers.sort()
print("sort :", numbers)

#max inbuilt function
numbers = [10,1,0,2,3,3,4]
print(" maximum number in the list")
print(max(numbers))

#min inbuilt function
numbers = [10,1,0,2,3,3,4]
print(" minmum number in the list")
print(min(numbers))

#insert inbuilt function
numbers = [10,1,0,2,3,3,4]
print(" insert number in the list")
print(numbers.insert(3,89))
print(f"List item: {numbers}")

#append inbuilt function
numbers = [10,1,0,2,3,3,4]
print(" append number in the list")
print(numbers.append(123))
print(f"List item: {numbers}")

#pop inbuilt function
numbers = [10,1,0,2,3,3,4]
print(" pop number in the list")
print(numbers.pop(5))
print(f"List item: {numbers}")

#count inbuilt function
numbers = [10,1,0,2,3,3,4]
print(" count number in the list")
print(f"List count in list: {numbers.count(3)}")