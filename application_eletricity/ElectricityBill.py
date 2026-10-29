"""
@file ElectricityBill.py
@brief Calculates an electricity bill from meter readings.
@date 29/10/2026
"""


def calculate_bill(units, rate):
    """
    @brief Calculate the electricity bill.
    @param units Electricity consumed in kWh.
    @param rate Cost per unit in rupees.
    @return Total electricity cost.
    """
    return units * rate


def main():
    """Run the electricity bill calculator."""

    print("===== ELECTRICITY BILL CALCULATOR =====")
    print("Date: 29/10/2026\n")

    try:
        previous = float(input("Enter previous meter reading: "))
        current = float(input("Enter current meter reading: "))
        rate = float(input("Enter rate per unit (Rs.): "))

        if previous < 0 or current < previous or rate < 0:
            print("Please enter valid readings and rate.")
            return

        units = current - previous
        bill = calculate_bill(units, rate)

        print("\n===== BILL DETAILS =====")
        print(f"Previous Reading : {previous:.2f}")
        print(f"Current Reading  : {current:.2f}")
        print(f"Units Consumed   : {units:.2f} kWh")
        print(f"Rate Per Unit    : Rs. {rate:.2f}")
        print(f"Total Bill       : Rs. {bill:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()