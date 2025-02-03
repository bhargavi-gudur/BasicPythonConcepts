import random as rd

# Get user input for their choice
user_choice = int(input("Enter your choice: rock-0, scissor-1, paper-2 ? :"))

# Generate random choice for computer
computer_choice = rd.randint(0, 2)
print("Computer choice:", computer_choice)

# Check if user entered an invalid number
if user_choice > 2 or user_choice < 0:
    print("Invalid number.")
else:
    # Display choices
    choices = ["rock", "scissor", "paper"]
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    # Determine the winner
    if computer_choice == user_choice:
        print("It's a draw.")
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 0):
        print("You win!")
    else:
        print("You lose.")
