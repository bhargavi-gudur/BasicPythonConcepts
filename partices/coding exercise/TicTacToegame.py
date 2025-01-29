# sample tic -tac -toe grid python code .

#initialise the grid with empty spaces.
grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_grid(grid):
    for row in grid:
        print('|'.join(row))
        print('-'*5)

# Get user input for row and column
row = int(input("Enter the row (1-3) where you want to place 'X': ")) - 1
col = int(input("Enter the column (1-3) where you want to place 'X': ")) 

if row < 0 or row > 2 or col < 0 or col > 2:
    print("invalid range ",row,col)
else :
   grid [row][col] ='X'
   display_grid(grid)