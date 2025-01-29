import random as rd

# Initialize the matrix
def initialize_matrix():
    row1 = ['😁', '😁', '😁']
    row2 = ['😁', '😁', '😁']
    row3 = ['😁', '😁', '😁']
    return [row1, row2, row3]

# Display the matrix with coordinates
def display_matrix(matrix):
    print("    1   2   3")
    for i, row in enumerate(matrix):
        print(f"{i+1} {row}")

# Get user input with validation
def get_position():
    while True:
        pos = input("Enter the position (row and column, e.g., 12) where you want to hide money: ")
        if len(pos) == 2 and pos.isdigit() and 1 <= int(pos[0]) <= 3 and 1 <= int(pos[1]) <= 3:
            return int(pos[0]), int(pos[1])
        else:
            print("Invalid input. Please enter a valid position in the format '12', where 1 is the row and 2 is the column.")

# Main function to run the program
def main():
    matrix = initialize_matrix()
    display_matrix(matrix)
    
    row_num, col_num = get_position()
    
    row_selected = matrix[row_num - 1]
    row_selected[col_num - 1] = 'X'
    
    print("\nUpdated Matrix:")
    display_matrix(matrix)

# Run the main function
main()
