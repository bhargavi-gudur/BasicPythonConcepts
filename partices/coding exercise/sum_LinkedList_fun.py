# Function to sum numbers in a list (like a linked list)
def sum_of_linked_list(linked_list):
    total = 0
    for num in linked_list:
        total += num
    return total

# Example list (simulated linked list)
linked_list = [10, 20, 30, 40]

# Call the function and print the result
print("Sum of linked list:", sum_of_linked_list(linked_list))