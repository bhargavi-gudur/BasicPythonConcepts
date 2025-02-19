#sample program dictonary .
keys  = {1,2,4,53,67,14}
values ={'bhargavi','sam','koti','rothi','ram','tara'}
combined = dict(zip(keys,values))
for i in keys:
 print(f"dictionary[{i}]: ",combined.get(i,"key not found"))