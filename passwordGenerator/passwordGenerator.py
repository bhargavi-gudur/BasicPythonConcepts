# sample password generator
import random as rd

symbols   =['!', '@', '#', '$', '%', '^', '&', '', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '|', '`', '~','*']
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers =['1', '2', '3', '4', '5', '6', '7', '8', '9']
print("weclome to password generator !")
num_letters=int(input("how many letters yo want in your password ?\n"))
num_symbols=int(input("how many letters yo want in your password ?\n"))
num_numbers=int(input("how many letters yo want in your password ?\n"))

password_list = [ ]

for i in range(1,num_letters+1):
    char = rd.choice(letters)
    password_list +=char

for i in range(1,num_symbols+1):
    char = rd.choice(symbols)
    password_list +=char

for i in range(1,num_numbers+1):
    char = rd.choice(numbers)
    password_list +=char

print(password_list)
rd.shuffle(password_list)
print("password list shuffle",password_list)
password=""
for char in password_list:
    password += char
print("password",password)