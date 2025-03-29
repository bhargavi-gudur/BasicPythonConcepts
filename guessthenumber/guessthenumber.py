#
import random

def guess_the_number():
    print("welcome to the number guessing game !")
    print("Choose your difficulty level:")
    print("1. Easy (3 chances)")
    print("2. Tough (6 chances)")

    difficulty = input("Enter 1 for Easy or 2 for Tough: ")

    if difficulty == "1":
        chances = 3
        print("youves chosen easy mode.you have 3 chances!")
    elif difficulty == "2":
        chances = 6
        print("youves chosen easy mode.you have 3 chances!")
    else:
        print("Invalid choice. Exiting the game.")
        return

    target_number = random.randint(1, 100)
    print("ive picked a number between  1 and 10 . try to guess it !")

    while chances > 0:
        guess = int(
            input(f"You have {chances} chances left. Enter your guess: "))

        if guess == target_number:
            print(
                f"Congratulations! You guessed the number {target_number} correctly!")
            return
        elif guess < target_number:
            print("Too low!")
        else:
            print("Too high!")

        # Decrease the number of chances
        chances -= 1

    # If the loop ends without a correct guess
    print(
        f"Sorry, you're out of chances. The correct number was {target_number}. Better luck next time!")


# Call the function to start the game
guess_the_number()
