"""
@file HouseholdElectricity.py
@brief Calculates household electricity consumption and cost.
@date 28/10/2026
"""


def calculate_units(power, hours, days):
    """
    @brief Calculate electricity consumption.
    @param power Appliance power in watts.
    @param hours Daily usage in hours.
    @param days Number of usage days.
    @return Energy consumed in kWh.
    """
    return (power * hours * days) / 1000


def calculate_bill(units, rate):
    """
    @brief Calculate electricity bill.
    @param units Total electricity consumption in kWh.
    @param rate Cost per unit.
    @return Total estimated bill.
    """
    return units * rate


def main():
    """Run the household electricity calculator."""

    print("HOUSEHOLD ELECTRICITY USAGE CALCULATOR")
    print("Date: 28/10/2026")

    try:
        n = int(input("Enter number of appliances: "))
        days = int(input("Enter number of usage days: "))
        rate = float(input("Enter electricity rate per unit (Rs.): "))

        if n <= 0 or days <= 0 or rate < 0:
            print("Invalid input.")
            return

        total_units = 0.0

        for i in range(1, n + 1):
            print(f"\nAppliance {i}")

            name = input("Enter appliance name: ")
            power = float(input("Enter power rating (watts): "))
            hours = float(input("Enter daily usage (hours): "))

            if power < 0 or not 0 <= hours <= 24:
                print("Invalid power or usage time.")
                return

            units = calculate_units(power, hours, days)
            total_units += units

            print(f"Energy used by {name}: {units:.2f} kWh")

        bill = calculate_bill(total_units, rate)

        print("\n========== ELECTRICITY BILL ==========")
        print(f"Usage period     : {days} days")
        print(f"Total units used : {total_units:.2f} kWh")
        print(f"Rate per unit    : Rs. {rate:.2f}")
        print(f"Estimated bill   : Rs. {bill:.2f}")
        print("======================================")

    except ValueError:
        print("Invalid input. Please enter the correct values.")


if __name__ == "__main__":
    main()