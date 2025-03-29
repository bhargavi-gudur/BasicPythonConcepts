print("hello world!")
string_val = "hello world !"
print("displaying attribute : ", string_val)
print("lenght:", len(string_val))
for i in string_val:
    print(i.swapcase())
# print(dir(string_val))
print("firstprogram -python print function \nit is declared like this:\n'print(\'what to print\')' \n")

# string manipulation
string_val = "hello world ! "
string_com = "learning python programming"
combined_string = string_val+string_com
print("combined_string :", combined_string, "\nstring_val:",
      string_val, "\nstring_com:", string_com)

check = "hello world!"+"\t"+"learning python programming"
print("check ->", check)

# example 1
print("--------------------------------------")
print("string manipulation \nstring concentation is done with \"+\" sign\ne.g.print(\"hello" +
      "bharu\")\nnew lines can be created with a bakslash and n.")
print("--------------------------------------")
variable = "string manipulation \nstring concentation is done with \"+\" sign\ne.g.print(\"hello" + \
    "bharu\")\nnew lines can be created with a bakslash and n."
print(variable.upper())
print("--------------------------------------")
# example 2
prompt = input("Enter a number:")
print("You entered:", prompt)
print("type:", type(prompt))
print("converting to integer: ", int(prompt))
dataType = int(prompt)
print("type: ", type(dataType))
print("--------------------------------------")
str_dataType = str(dataType)
print("type: ", type(str_dataType))
for i in range(len(str_dataType)):
    print("i:",i,"value:",str_dataType[i])
# example 3
print("--------------------------------------")
string_var = input("what is your name?")
print(f"Hello {string_var} how are you?")
print("--------------------------------------")
#example 4
print("--------------------------------------")
print("swapping two numbers")
print("arithmatic approach")
a = 10
b =21
print("before swap : ","a:",a,"b:",b)
c = a+b
print("sum of c value :",c)
a = c-a
b = c-b
print("after swap : ","a:",a,"b:",b)
print("--------------------------------------")
print("x-or approach")
a = 10
b = 21
print("before swap : ", "a:", a, "b:", b)
c = a^b
a = c^a
b = c^b
print("after swap : ", "a:",a,"b:",b)
print("--------------------------------------")
print("user input -> x-or approach")
a = int(input("Enter a number a:"))
b = int(input("Enter a number b:"))
print("before swap : ", "a:", a, "b:", b)
c = a ^ b
a = c ^ a
b = c ^ b
print("after swap : ", "a:", a,"b:",b)
print("--------------------------------------")
print("no third variable approach")
a = int(input("Enter a number a:"))
b = int(input("Enter a number b:"))
print("before swap : ", "a:", a, "b:", b)
a = a+b
b = a-b
a = a-b
print("after swap : ", "a:", a, "b:", b)
print("--------------------------------------")