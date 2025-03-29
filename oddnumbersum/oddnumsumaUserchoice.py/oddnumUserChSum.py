def sumofoddnum(num):
    current = 1
    for i in range(num):
        print("odd numbers : ", current)
        current += 2

def choice():
    while True:
        num = int(input("enter the num value : "))
        sumofoddnum(num)
        choice_var = input(
            "enter the choice y or n  to continue the sum of  odd number function? ")
        if choice_var == 'n':
            print("Exiting the function. Goodbye!")
            break
        elif choice_var != 'y':
            print("Invalid choice. Exiting the function.")
            break


choice()
