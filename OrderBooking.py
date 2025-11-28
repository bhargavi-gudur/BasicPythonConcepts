"""

@file OrderBooking.py
@author Gandla Bhargavi
@brief Simple program to take customer orders and show order summary.

@date 2025-11-28

"""

class OrderBooking:
    def __init__(self):
        self.orders = []       # stores item names
        self.total_items = 0   # count items

    # Add item to order list
    def add_order(self, item):
        self.orders.append(item)
        self.total_items += 1
        print(f"Added: {item}")

    # Show order summary
    def show_summary(self):
        print("\n--- Order Summary ---")
        if not self.orders:
            print("No orders booked.")
        else:
            for i, item in enumerate(self.orders, start=1):
                print(f"{i}. {item}")

        print(f"Total Items : {self.total_items}")
        print("Date        : 28-11-2025")


def main():
    ob = OrderBooking()

    while True:
        item = input("Enter item name to book (or type 'done'): ")
        if item.lower() == "done":
            break
        if item.strip():
            ob.add_order(item)

    ob.show_summary()


if __name__ == "__main__":
    main()