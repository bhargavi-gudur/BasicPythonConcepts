# This code demonstrates how to flatten a matrix using list comprehension. 
matrix =[[1,5,6],[89,67,78],[7,8,9],[130,456,678],[7,12,45]]
#  Using list comprehension to flatten a matrix
def flatten_matrix(matrix):
   flattened =[num for row in matrix for num in row]
   print(flattened)
   return flattened

def print_matrix(matrix):
   for row in matrix:
       print(row)
       
def sorting_matrix(matrix):
    sorted_matrix = [rows for value in matrix for rows in value]
    print(sorted(sorted_matrix))
    print(reversed(sorted_matrix))

   
    
flatten_matrix(matrix)
print_matrix(matrix)
sorting_matrix(matrix)


