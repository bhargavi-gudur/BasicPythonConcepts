# Love calculator Python program
name1 = input("What is your name? ")
name2 = input("What is his/her name? ")

# Combine the names and convert to lowercase
combined_string = name1 + name2
lower_case_string = combined_string.lower()

# Count the occurrences of each letter in 'true love'
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
# Calculate the love score
true_score = t + r + u + e
love_score = l + o + v + e
love_percentage = int(str(true_score) + str(love_score))

print(f"Your love score is {love_percentage}.")
