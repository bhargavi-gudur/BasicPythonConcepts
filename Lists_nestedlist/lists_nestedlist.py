# nested lists of list 
# the position  to find the hide money 
row1 =['😁','😁','😁']
row2 = ['😁','😁','😁']
row3 =['😁','😁','😁']

# nested list
matrix = [row1,row2,row3]

# printing on the screen row1 to row3 in list format
print(f"{row1}\n{row2}\n{row3}\n")

# enter  input  which position to hide money.
pos = input("enter the position where you want to hide money :")

# The input string pos is split into two parts. row_num takes the first character, and col_num takes the second. Both are then converted to integers.
row_num= int(pos[0])
col_num = int(pos[1])

row_selected = matrix[row_num-1]
row_selected[col_num-1] ='X'

print(f"{row1}\n{row2}\n{row3}\n")



