# random inbuilt function.
import random as rd
# choice inbuilt method
text = "weclome to bhargavisample code."
text_spitted = text.split("o ")
print(text_spitted)

# wap while select a random name from a list of names and the person selected have to pay for everybody's food bill.
name = input("enter everybody's name separated by coma :")
name_list = name.split(",")
lenght = len(name_list)
random_choice = rd.randint(0,lenght-1)
print(f"{name_list[random_choice]} will pay the bill")
