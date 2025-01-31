#sample list python program
exp = [2340,2500,3100,2980]
total = 0
for item in exp:
    total = total+ item
print("item :", total)
# sample list using range function 
for i in  range(1,10):
    print("i:",i)
# sample list program using range function add.
add =0
for i in  range(1,10):
    add = add+i
    print("i:",i," add:",add)  
# sample list using range function and len function.
# addition 
lists_item =[1,2,3,4,5,6,7,8,9]
for i in  range(len(lists_item)):
    print("lists ",lists_item[i]+i)

# key location same code using list annd for loop.
key_location =input('enter the location?')
locations=["garage","living room",'chair',"closet","bedroom"]
for  i in  locations:
    if i == key_location:
        print('KEY FOUND')
        break
    else :
        print("key is not found in",i)
# pop function
lists = (2,3,4,56,67,89,123,129)
print('tuple:',lists.pop())
