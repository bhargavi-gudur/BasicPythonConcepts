fruit = {"apple": 250, "orange ": 300, "mango": 50}
print(fruit.get("apple"))
# Returns "Not Found" if the key is not found
print(fruit.get("banana", "Not Found"))


data = {"Name": "Alan", "Age": 25}
# Write your code here

for x, y in data.items():
    print(x, y)

fruits = {"apple": 250, "orange": 300, "mango": 50}
# Write your code here
fruit["apple"] = 500
fruit["banana"] = 100
print(fruit)
