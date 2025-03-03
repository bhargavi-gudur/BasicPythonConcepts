#sample while loop python program.
# use case : custom control over iteration.

#approach 1
data =[1,33,5,64,22,45,78]
i = 0
while i<len(data):
    print("data", data[i])
    i = i+1

#approach 2
data =[]
num = int(input("Enter the number of elements: "))
i=0
# Collect data into the list
while i<num:
    value =int(input(f"enter value {i+1} : "))
    data.append(value)
    i=i+1

i=0 # Reset index for printing

# Print the list
while i<len(data):
    i = i+1
print("data", data)