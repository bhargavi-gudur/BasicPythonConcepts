# sample expection handling sample python code.
x = int(input("enter the value of x : "))
y = int(input("enter the value of y : "))

try:
 z = x/y
 
except ZeroDivisionError as e:
  print("expection ocurred :",e)
  z = None
except TypeError as e:
 print(" type error  ", type(e).__name)
 z = None
except Exception as e:
 print(" type error  ", type(e).__name)
 z = None
else :
  print("division is ",z)

