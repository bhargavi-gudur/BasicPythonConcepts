
do_continue = int(
    input(" do you want continue program add  1  else 0 to exit?"))
while (do_continue == 1):
    a = int(input(" enter the a "))
    b = int(input(" enter the b "))

    def add(a, b):
        c = a+b
        print("addition : ", c)

    def sub(a, b):
        c = a-b
        print("subraction:", c)
    add(a, b)
    sub(a, b)
    do_continue = int(input(" do you want continue ?"))


class add:
    def __init__(self, firstnumber, secondnumber):
        self.a = firstnumber
        self.b = secondnumber
        c = self.a + self.b
        print("c: ", c)

summation = add(3, 6)
print(summation.a+summation.b)
print(summation.a-summation.b)
