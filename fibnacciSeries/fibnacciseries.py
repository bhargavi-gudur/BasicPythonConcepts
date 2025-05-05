def fibonacci_series():
    n = int(input(""))  # Added user prompt

    a, b = 0, 1  # Initialize first two numbers

    for i in range(n):
        print(a, end=" ")  # Print the number with space
        a, b = b, a + b  # Update values for next iteration


fibonacci_series()
