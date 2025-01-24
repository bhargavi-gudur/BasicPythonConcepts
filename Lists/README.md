# Python List Operations

This script demonstrates various operations that can be performed on Python lists.

## Operations

1. **Method 1: Iterating through a list using a `for` loop**
    ```python
    numbers = [10, 1, 0, 2, 3, 3, 4]
    for item in numbers:
        print(f"List item: {item}")
    print("Length:", len(numbers))
    ```

2. **Method 2: Iterating through a list using `range()`**
    ```python
    for i in range(len(numbers)):
        print(f"List item: {numbers[i]}")
    print("Length:", len(numbers))
    ```

3. **Slicing Lists**
    ```python
    print("Slicing:", numbers[0:5])
    print("Extended Slicing:", numbers[0:6:2])
    ```

4. **Sorting Lists**
    ```python
    numbers.sort()
    print("Sorted:", numbers)
    ```

5. **Finding Maximum Value**
    ```python
    print(max(numbers))
    ```

6. **Finding Minimum Value**
    ```python
    print(min(numbers))
    ```

7. **Inserting Elements**
    ```python
    numbers.insert(3, 89)
    print(f"List after insertion: {numbers}")
    ```

8. **Appending Elements**
    ```python
    numbers.append(123)
    print(f"List after appending: {numbers}")
    ```

9. **Popping Elements**
    ```python
    numbers.pop(5)
    print(f"List after popping: {numbers}")
    ```

10. **Counting Occurrences**
    ```python
    print(f"Count of 3 in list: {numbers.count(3)}")
    ```

## Explanation

This script covers basic list operations in Python, including:
- Iterating through lists
- Slicing lists to retrieve subsets
- Sorting lists
- Finding the maximum and minimum values
- Inserting, appending, and removing elements
- Counting occurrences of specific elements

These operations demonstrate the versatility and ease of use of Python lists for various data manipulation tasks.
