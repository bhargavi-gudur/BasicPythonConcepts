# find the sum of even number using range function.
# 1 way approach
#Using Modulo Operator
sum_even = 0
for loop in range(1,11):
 if loop %2 ==0:
  sum_even +=loop
 print(f'{loop} ->sum of even number:{sum_even}')
 print("************************************")
 # 2 way appraoch
 # Using Step in Range Function
 sum_even = 0
for loop in range(2,11,2):
  sum_even +=loop
  print(f'{loop} ->sum of even number:{sum_even}')
print("************************************")