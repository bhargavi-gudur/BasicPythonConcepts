"""
@file FuelAdd.py
@author Gandla Bhargavi
@brief Program to add fuel amounts and show total fuel.

@date 2025-11-27
"""

class Fuel:
    def __init__(self):
        self.total = 0

    # Add fuel amount
    def add_fuel(self, amount):
        self.total += amount
        print(f"Added: {amount} liters")

    # Show total fuel
    def show_total(self):
        print("\n--- Fuel Summary ---")
        print(f"Total Fuel Added : {self.total} liters")
        print("Date             : 25-11-2025")


def main():
    fuel = Fuel()

    while True:
        amt = input("Enter fuel amount (or type 'done'): ")
        if amt.lower() == "done":
            break

        if amt.isdigit():
            fuel.add_fuel(int(amt))
        else:
            print("Please enter numbers only!")

    fuel.show_total()


if __name__ == "__main__":
    main()