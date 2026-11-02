"""
@file ElectricityComparison.py
@brief Compares electricity consumption between two months.
@date 02/11/2026
"""


def calculate_bill(units, rate):
    """
    @brief Calculate electricity bill.
    @param units Electricity consumed in kWh.
    @param rate Cost per unit.
    @return Total bill amount.
    """
    return units * rate


def calculate_difference(month1, month2):
    """
    @brief Calculate difference in electricity consumption.
    @param month1 First month's consumption.
    @param month2 Second month's consumption.
    @return Difference in units.
    """
    return month2 - month1


def main():
    """Run the electricity usage comparison application."""

    print("===== ELECTRICITY USAGE COMPARISON =====")
    print("Date: 02/11/2026\n")

    try:
        month1 = float(input("Enter first month units: "))
        month2 = float(input("Enter second month units: "))
        rate = float(input("Enter electricity rate: "))

        if month1 < 0 or month2 < 0 or rate < 0:
            print("Invalid input!")
            return

        bill1 = calculate_bill(month1, rate)
        bill2 = calculate_bill(month2, rate)

        difference = calculate_difference(month1, month2)

        print("\n===== COMPARISON REPORT =====")
        print(f"First Month Units  : {month1:.2f} kWh")
        print(f"Second Month Units : {month2:.2f} kWh")
        print(f"First Month Bill   : Rs. {bill1:.2f}")
        print(f"Second Month Bill  : Rs. {bill2:.2f}")

        if difference > 0:
            print(f"Usage Increased   : {difference:.2f} kWh")
        elif difference < 0:
            print(f"Usage Decreased   : {-difference:.2f} kWh")
        else:
            print("Usage Unchanged")

        print(f"Bill Difference   : Rs. {bill2 - bill1:.2f}")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()