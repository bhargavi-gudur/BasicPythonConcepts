"""
@file nursery_booking.py
@author Gandla Bhargavi
@brief
    This program simulates a nursery plant booking system.
    It uses OOP and list data structure to manage 20 indoor plants.
@date 06-04-2026
"""

class Plant:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Nursery:
    def __init__(self):
        self.plants = []

    # Initialize plant list
    def init_plants(self):
        names = [
            "Aloe Vera","Snake Plant","Money Plant","Peace Lily","Spider Plant",
            "Tulsi","Bamboo Plant","Jade Plant","Areca Palm","Fern",
            "Rubber Plant","ZZ Plant","Croton","Anthurium","Dracaena",
            "Cactus","Orchid","Calathea","Philodendron","Aglaonema"
        ]

        for i in range(20):
            plant = Plant(names[i], 100 + i * 10)
            self.plants.append(plant)

    # Show plants
    def show_plants(self):
        print("\n===== Indoor Plants List =====")
        for i, plant in enumerate(self.plants, start=1):
            print(f"{i}. {plant.name} - {plant.price} Rs")

    # Booking function
    def book_plant(self):
        print("\n1. Online\n2. Offline")
        booking_type = int(input("Enter booking type: "))

        self.show_plants()

        choice = int(input("Enter plant number: "))
        qty = int(input("Enter quantity: "))

        if choice < 1 or choice > 20:
            print("Invalid plant!")
            return

        selected = self.plants[choice - 1]
        total = selected.price * qty

        print(f"\nPlant: {selected.name}")
        print(f"Total Cost: {total} Rs")

        if booking_type == 1:
            print("Payment done online.")
        else:
            print("Pay at nursery (offline).")

        print("Booking Successful!")


# Main program
if __name__ == "__main__":
    nursery = Nursery()
    nursery.init_plants()

    print("===== Nursery Booking System =====")
    print("Date: 06-04-2026")

    while True:
        print("\n1. Show Plants")
        print("2. Book Plant")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            nursery.show_plants()
        elif choice == 2:
            nursery.book_plant()
        elif choice == 3:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")