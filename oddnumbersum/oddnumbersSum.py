# odd   numbers sum and print the odd number by user enter value.
num = int(input("enter the num value : "))
def sumofoddnum(num):
    current = 1
    sum = 0
    for i in range(num):
        sum += current
        print(f"odd numbers :{current} , sum : {sum}")
        current += 2
    print(f"total sum : {sum}")
    
for i in range(5):
 sumofoddnum(num)
