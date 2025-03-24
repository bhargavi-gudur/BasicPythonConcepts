def random_code():
    print(len("23"))
    print(10*",12,11")
    name = "bhargavi"
    print(10+len(name))
    print(int("10")+int("10"))
    name = "134"
    print(10+int(name))

    a = int(input("enter first number a: "))
    b = int(input("enter first number b: "))
    print("int : ", a+b, "lenght:")

    c = input("enter first number c: ")
    d = input("enter first number d: ")
    print("int : ", int(c)+int(d), "len:", len(c+d))


def addDigitNum():
    number = input("enter the  only number in string ")
    # sum_digit = int(number[0])+int(number[1])
    # print("sum:",sum_digit)
    sum_digit = 0
    for i in range(len(number)):
        sum_digit = sum_digit + int(number[i])
        print(
            f"at index {i} ,in loop  the string number {int(number[i])} the sum of num is -> {sum_digit}")


random_code()
addDigitNum()
