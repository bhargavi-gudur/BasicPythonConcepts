#inbuilt function range program
#example 1
a = range(2,5)
print(f"a[0]:{a[0]},a[1]:{a[1]}")
print("************************************************")
#example 2
list_range =[1,2,3,3,4,221,23]
for lrange in  range(2,6) :
 print("2 step size:",list_range[lrange])
print("************************************************")
#example 3
a = range(2,15,1)
for i in a:
 print(f'a -> {i}')
print("************************************************")
#example 4 -> find total sum of 1 to 100 using range function
total = 0
for loop in range(1,101):
 total +=loop
 print(f'LOOP-> {loop} total ->{total}')
print("************************************************")