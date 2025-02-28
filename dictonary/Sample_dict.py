# Write a Python program to iterate over dictionaries using for loops.
# Write a Python program to sum all the items in a dictionary.
key_value = {"gandla": 123, "shyam": 14565, "iran": 677, "riya": 344}
print("dictonary:", key_value)
for i in key_value:
 print(f"key ->{i}, value -> {key_value[i]}")

key_value["riya"] = 9088
print("dictonary:", key_value)
print("sum of all values:", sum(key_value.values()))
key_value['time'] = {"time_in:": 123, "time_out:": 823}
print("dictonary:", key_value)
print(key_value['time']["time_in:"])
print(key_value.get('time'))
print(key_value.pop('time'))
for i in key_value:
 print(f"key ->{i}, value -> {key_value[i]}")
