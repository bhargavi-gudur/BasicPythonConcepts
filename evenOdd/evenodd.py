#sample if-else  odd or even python code
number =int(input("enter the number to find odd or even :"))
if  number>=0 and number%2 == 0:
    print("even number ->", number)
elif number>=0 and number%2 == 1:
     print("odd number ->", number)
else :
    print("invalid input",number)