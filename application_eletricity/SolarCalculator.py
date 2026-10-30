"""
@file SolarCalculator.py
@brief Calculates solar panel electricity generation and savings.
@date 31/10/2026
"""


def calculate_daily_energy(capacity, sunlight):
    """
    @brief Calculate daily solar energy generation.
    @param capacity Solar panel capacity in watts.
    @param sunlight Daily sunlight hours.
    @return Daily energy in kWh.
    """
    return (capacity * sunlight) / 1000


def calculate_monthly_energy(daily):
    """
    @brief Calculate monthly solar energy generation.
    @param daily Daily energy in kWh.
    @return Monthly energy in kWh.
    """
    return daily * 30


def calculate_savings(energy, rate):
    """
    @brief Calculate estimated electricity savings.
    @param energy Energy generated in kWh.
    @param rate Electricity tariff per unit.
    @return Estimated savings in rupees.
    """
    return energy * rate


def main():
    """Run the solar electricity calculator."""

    print("===== SOLAR ELECTRICITY CALCULATOR =====")

    try:
        capacity = float(input("Enter solar panel capacity (Watts): "))
        sunlight = float(input("Enter daily sunlight hours: "))
        rate = float(input("Enter electricity rate per unit: "))

        if capacity < 0 or not 0 <= sunlight <= 24 or rate < 0:
            print("Invalid input!")
            return

        daily = calculate_daily_energy(capacity, sunlight)
        monthly = calculate_monthly_energy(daily)
        savings = calculate_savings(monthly, rate)

        print("\n===== SOLAR ENERGY REPORT =====")
        print(f"Daily Generation   : {daily:.2f} kWh")
        print(f"Monthly Generation : {monthly:.2f} kWh")
        print(f"Estimated Savings  : Rs. {savings:.2f}")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()