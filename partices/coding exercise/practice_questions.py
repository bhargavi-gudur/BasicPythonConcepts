# 1. Area of rectangle
def area_of_rectangle(length, width):
    return length * width

# 2. Greeting message
def greeting(name, age):
    return f"Hello {name}, you are {age} years old."

# 3. Even or Odd
def is_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# 4. Max and Min from list
def find_max_min(numbers):
    return max(numbers), min(numbers)

# 5. Palindrome check
def is_palindrome(string):
    return string == string[::-1]

# 6. Compound interest
def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return round(amount, 2)

# 7. Days to years, weeks, and days
def convert_days(days):
    years = days // 365
    weeks = (days % 365) // 7
    remaining_days = (days % 365) % 7
    return years, weeks, remaining_days

# 8. Sum of positive numbers
def sum_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)

# 9. Count words in sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)

# 10. Swap variables
def swap_variables(a, b):
    return b, a

# ========================
# Call and print each result
# ========================
print("1. Area of Rectangle:", area_of_rectangle(5, 10))
print("2. Greeting:", greeting("Alice", 25))
print("3. Even or Odd (7):", is_even_or_odd(7))
print("4. Max and Min:", find_max_min([3, 7, 2, 9, 1]))
print("5. Palindrome Check ('madam'):", is_palindrome("madam"))
print("6. Compound Interest:", compound_interest(1000, 5, 2))
print("7. Convert 800 days:", convert_days(800))
print("8. Sum of Positives:", sum_positive_numbers([4, -2, 6, -1, 7]))
print("9. Word Count:", count_words("This is a sample sentence"))
print("10. Swap (a=10, b=20):", swap_variables(10, 20))