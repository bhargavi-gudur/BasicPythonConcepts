#sample python code sets
#sets are display  unordered
# sets  function is not allowed  indexing
set1={10,True,'jenny',11,11,23,33,10,20}
set2 ={12,345,"bhargavi,-10",123.78}
set3={10,23,10,24,45,56,45,11}

#printing set on the display
# set duclipates, slicing ,indexing  are not allowed 
print("-----------------------")
print("set 1 : ",set1)
set1.add(78)
print("adding in set 1:",set1)
print("set1 lenght :",len(set1))
print("-----------------------")
print("set 2 : ",set2)
set2.remove(12)
print("removed set 2 : ",set2)
print("set2 lenght :",len(set2))
print("-----------------------")
print("set 3 : ",set3)
set3.pop()
print("pop out  set 3 : ",set3)
print("set3 lenght :",len(set3))
print("-----------------------")
# tuples added in set 
print("tuples added in set3")
print("set 3 : ",set3)
print("set3 lenght :",len(set3))
set3.add((2,4,56.4,45))
print(" adding tuple set 3 : ",set3)
print("-----------------------")