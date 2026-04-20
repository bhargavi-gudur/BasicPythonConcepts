"""
File: music_recording.py
Author: Gandla Bhargavi
Description:
    This program simulates a music recording purchase system.
    It uses dictionary to store music categories and costs.
    Supports online and offline purchase.
Date: 19-04-2026
"""

# Initialize music data
music = {
    1: ("Classical", 1000),
    2: ("Romantic", 800),
    3: ("Devotional", 600),
    4: ("Instrumental", 900)
}

# Show music list
def show_music():
    print("\nAvailable Music Recordings:")
    for key, value in music.items():
        print(f"{key}. {value[0]} - {value[1]} Rs")

# Purchase function
def purchase():
    print("\n1. Online Purchase\n2. Offline Purchase")
    type_choice = int(input("Enter choice: "))

    show_music()

    choice = int(input("Select music: "))

    if choice in music:
        name, cost = music[choice]

        print(f"Selected: {name}")
        print(f"Cost: {cost} Rs")

        if type_choice == 1:
            print("Payment Successful (Online)")
        elif type_choice == 2:
            print("Pay at counter (Offline)")
        else:
            print("Invalid payment type!")
    else:
        print("Invalid selection!")

# Main program
def main():
    print("===== Music Recording Store =====")
    print("Date: 19-04-2026")

    while True:
        print("\n1. Show Music")
        print("2. Purchase")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            show_music()
        elif choice == 2:
            purchase()
        elif choice == 3:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

# Run program
if __name__ == "__main__":
    main()