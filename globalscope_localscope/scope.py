#sample scope global and local scope sample program
print(40*"-")
a = 10
def display():
    a = 15
    print("display -> inside a :", a)

    def show():
        a = 90
        print("show -> inside a :", a)
    show()
display()
print("outside a :", a)
print(40*"-")
a, b = 5, 6
if a < b:
    c = a+b
print("c->", c)
print(40*"-")
a, b = 1.5, 7.6

def indisplay():
    if a < b:
        c = a+b
        print("under if statement c->", c)
    print("exact if statement c->", c)


indisplay()
print(40*"-")
