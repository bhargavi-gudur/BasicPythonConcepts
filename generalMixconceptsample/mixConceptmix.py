
def floormethod():
    a = 10
    b = 4
    b = a
    print("before change to assigned values : ", a/b, a//b)
    a = 10
    print("after change to assigned  values :", a/b, a//b)


def logic_add_0perator():
    a = 12
    b = 6
    print(" logical And Operator : ", a & b)
    print(" logical Or Operator : ", a | b)
    print(" logical Xor Operator : ", a ^ b)
    print(" logical Not Operator : ", ~a)
    print(" logical Not Operator : ", ~b)
    print(" logical Left Shift Operator : ", a << 2)
    print(" logical Right Shift Operator : ", a >> 2)
    print(" logical Left Shift Operator : ", b << 2)
    print(" logical Right Shift Operator : ", b >> 2)


def elseifSample():
    if True:
        print("One")
    elif True:
        print("Two")
    else:
        print("Three")


def slicingstring():
    str = "Python"
    print(str[:-4])
    str1 = "Python"
    print(str1[-4:6])


def stringlen():
    str = "         Hello "
    print(len(str))
    new_str = str.strip()
    print(len(new_str))


def stringsplit():
    str = "The words present in this string are separated by white space."
    # Write your code here
    new_str = str.split(" ")
    print(len(new_str))


def stringreplace():
    str = input("enter the string: ")
    # Write your code here
    new_str = str.replace(" ", "_")
    print(new_str)


def sumofNaturalNum(N):
    order_naturalNum = (N * (N + 1))/2
    print(order_naturalNum)

# Convert the number to a string to iterate through its digits


def count_of_digits():
    num = int(input("enter the number: "))
    digits = [int(digit) for digit in str(num)]

    for digit in digits:
        print(digit, end="")


# Convert the number to a string to iterate through its digits
def sum_of_digits():
    # Convert the number to a string to iterate through its digits
    num = int(input("enter the number: "))
    # Convert the number to a string to iterate through its digits
    digits = [int(digit) for digit in str(num)]
    sum1 = 0
    for digit in digits:
        sum1 = sum1 + digit
    print(sum1)


# def calling  about methods
def calling_methods():
    print("floormethod")
    floormethod()
    print("logic_add_0perator")
    logic_add_0perator()
    print("elseifSample")
    elseifSample()
    print("slicingstring")
    slicingstring()
    print("stringlen")
    stringlen()
    print("stringsplit")
    stringsplit()
    print("stringreplace")
    stringreplace()
    print("sumofNaturalNum")
    N = int(input(" "))
    sumofNaturalNum(N)
    print("sum_of_digits")
    sum_of_digits()
    print("count_of_digits")
    count_of_digits()


# calling the methods inside the function methods
print("the methods are called inside the function methods")
calling_methods()
print("-" * 50)
