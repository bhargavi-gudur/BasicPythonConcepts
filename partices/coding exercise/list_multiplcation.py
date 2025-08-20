def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example list
num_list = [2, 3, 4]

# Call the function
print("Multiplication of list:", multiply_list(num_list))