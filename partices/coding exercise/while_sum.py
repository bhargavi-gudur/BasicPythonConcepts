#sum of positive number and when press zero out od loop
total =0 
num = int(input('Enter the value: '))
while num!=0:
    total =total + num
    num = int(input('Enter the value: '))
    print(" num : ",num," total : ",total)
print('when zero pressed existing from loop')