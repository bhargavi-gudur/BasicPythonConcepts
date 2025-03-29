# to find the given number is prime or not prime number .
import os


def prime(num):
    continue_loop = input("Do you want to continue? (y/n): ").lower()
    while continue_loop != 'n':
        flag = False  # Reset the flag for each number
        if num == 0 or num == 1:
            print(f"{num} is not a prime number.")
        elif num > 1:
            for i in range(2, num):  # Check divisors from 2 to num-1
                if num % i == 0:
                    flag = True
                    break  # Stop checking if a divisor is found

            if flag:
                print(f"{num} is not a prime number.")
            else:
                print(f"{num} is a prime number.")

        # Prompt for a new number and check continuation

        continue_loop = input("Do you want to continue? (y/n): ").lower()
        num = int(input("Enter another number: "))
        os.system('cls')


# Main execution
user_num = int(input("Enter a number: "))
prime(user_num)
