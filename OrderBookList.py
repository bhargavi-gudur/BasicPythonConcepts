"""
@file OrderBookList.py
@author Gandla Bhargavi
@brief Program to store and display a list of booked orders.

@date 2025-11-29
"""

class OrderBook:
    def __init__(self):
        self.order_list = []      # stores ordered items
        self.count = 0            # number of items

    def add_item(self, item):
        """Add an item to the order list"""
        self.order_list.append(item)
        self.count += 1
        print(f"Added: {item}")

    def show_orders(self):
        """Display the booked order list"""
        print("\n--- Order Book List ---")
        if not self.order_list:
            print("No orders booked.")
        else:
            for i, item in enumerate(self.order_list, start=1):
                print(f"{i}. {item}")

        print(f"Total Items : {self.count}")
        print("Date        : 28-11-2025")


def main():
    ob = OrderBook()

    while True:
        item = input("Enter order item (type 'done' to finish): ")
        if item.lower() == "done":
            break
        if item.strip():
            ob.add_item(item)

    ob.show_orders()


if __name__ == "__main__":
    main()