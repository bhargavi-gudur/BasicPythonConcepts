n = int(input())  # Get user input


def pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print(" ", end="")  # Use 'end=""' to print on the same line
            else:
                print("*", end="")  # Print spaces instead of new lines
        print()  # Move to the next line


pattern(n)


