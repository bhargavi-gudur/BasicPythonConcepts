# sample for loop in python
loop = 6
# Using for loop to iterate over a range of numbers
for i in range(loop):
    print('hello world , learn python',i)

# for loop using list 
list_loop =[2,3,4,4,5,[2,3,4,55,67],78]

#using for loop to iterate over a range of  list insides numbers.
for i in range(len(list_loop)):
    #print("lists : ",i)
    print(f"loop :{i} lists:{list_loop[i]}")

# Nested for loop
for i in range(3):     # outer loop
    for j in range(2): # inside loop
        print(f"i: {i}, j: {j}")

