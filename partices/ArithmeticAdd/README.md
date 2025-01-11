# arithmic addition in string 
## method 1
1.num = input("enter the integer: "): Prompts the user to enter an integer as a string.

2.digit_sum = int(num[0]) + int(num[1]): Converts the first and second characters of the string to integers and adds them.

3. print('The addition of the digits:', digit_sum): Prints the sum of the digits.

## method 2
1.num = input("enter the integer: "): Prompts the user to enter an integer as a string.

2.digit_sum = 0: Initializes a variable to store the sum of the digits.

3.for digit in num:: Iterates through each character in the string num.

4.digit_sum += int(digit): Converts each character to an integer and adds it to digit_sum.

5.print('The addition of the digits:', digit_sum): Prints the sum of the digits.