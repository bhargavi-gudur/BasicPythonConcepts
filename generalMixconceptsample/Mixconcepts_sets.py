data = {'a', 'e', 'i', 'o', 'u'}
data.clear()
print(data)
print("list", list(data))


data = {10, 200, 100, 500, 2000}
# Write your code here
print(data)
copy_var = data.copy()
print(copy_var)


a = {10, 20, 100, 50}
b = {10, 20, 30}
c = a.union(b)
print(len(c))

a = {'a', 'e', 'x', 'y', 'i', 'f', 'k', 'c'}
# Write your code here

b = {'a', 'i', 'e', 'o', 'u'}

common_var = a.intersection(b)
print(common_var)
