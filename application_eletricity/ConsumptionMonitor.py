"""
@file ConsumptionMonitor.py
@brief Monitors electricity consumption and calculates bills.
@date 05/11/2026
"""


def calculate_daily_energy(power, hours):
    """
    @brief Calculate daily electricity consumption.
    @param power Appliance power in watts.
    @param hours Daily usage in hours.
    @return Energy consumed in kWh.
    """
    return (power * hours) / 1000


def calculate_monthly_energy(daily_energy, days):
    """
    @brief Calculate monthly electricity consumption.
    @param daily_energy Daily energy in kWh.
    @param days Number of days.
    @return Monthly energy consumption in kWh.
    """
    return daily_energy * days


def calculate_bill(units, rate):
    """
    @brief Calculate electricity bill.
    @param units Total energy consumption in kWh.
    @param rate Electricity tariff per unit.
    @return Total electricity cost.
    """
    return units * rate


def main():
    """Run the electricity consumption monitoring system."""

    print("===== ELECTRICITY MONITORING SYSTEM =====")
    print("Date: 05/11/2026\n")

    try:
        power = float(input("Enter appliance power (Watts): "))
        hours = float(input("Enter daily usage (Hours): "))
        days = int(input("Enter number of days: "))
        rate = float(input("Enter electricity rate (Rs.): "))

        if power < 0 or not 0 <= hours <= 24 or days <= 0 or rate < 0:
            print("Invalid input!")
            return

        daily = calculate_daily_energy(power, hours)
        monthly = calculate_monthly_energy(daily, days)
        bill = calculate_bill(monthly, rate)

        print("\n===== ENERGY REPORT =====")
        print(f"Daily Consumption   : {daily:.2f} kWh")
        print(f"Total Consumption   : {monthly:.2f} kWh")
        print(f"Estimated Electricity Bill: Rs. {bill:.2f}")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()