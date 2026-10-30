"""
@file ElectricitySaving.py
@brief Calculates electricity and money savings.
@date 30/10/2026
"""


def calculate_saving(power, hours):
    """
    @brief Calculate daily electricity savings.
    @param power Appliance power in watts.
    @param hours Reduced usage hours per day.
    @return Energy saved in kWh.
    """
    return (power * hours) / 1000


def calculate_money(units, rate):
    """
    @brief Calculate money saved.
    @param units Energy saved in kWh.
    @param rate Electricity rate per unit.
    @return Money saved in rupees.
    """
    return units * rate


def main():
    """Run the electricity saving calculator."""

    print("===== ELECTRICITY SAVING CALCULATOR =====")

    try:
        power = float(input("Enter appliance power (Watts): "))
        hours = float(input("Enter reduced usage hours per day: "))
        rate = float(input("Enter electricity rate per unit: "))

        if power < 0 or not 0 <= hours <= 24 or rate < 0:
            print("Invalid input!")
            return

        daily = calculate_saving(power, hours)
        monthly = daily * 30
        yearly = daily * 365

        monthly_money = calculate_money(monthly, rate)
        yearly_money = calculate_money(yearly, rate)

        print("\n===== SAVING REPORT =====")
        print(f"Daily Saving   : {daily:.2f} kWh")
        print(f"Monthly Saving : {monthly:.2f} kWh")
        print(f"Yearly Saving  : {yearly:.2f} kWh")
        print(f"Monthly Money  : Rs. {monthly_money:.2f}")
        print(f"Yearly Money   : Rs. {yearly_money:.2f}")

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()