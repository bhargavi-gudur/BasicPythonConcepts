# List comprehension in Python
# List comprehension is a concise way to create lists in Python.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # List comprehension to generate all valid coordinates
    result = [[i, j, k] for i in range(
        x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

    print(result)
