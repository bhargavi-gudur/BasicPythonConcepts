"""
@file standby_power.py
@brief Calculates standby electricity consumption and cost.
@date 15/11/2026
"""

def calculate_daily_energy(power, hours):
    """
    @brief Calculates daily standby energy consumption.
    @param power Standby power in watts.
    @param hours Standby hours per day.
    @return Daily energy consumption in kWh.
    """
    return (power * hours) / 1000


def calculate_monthly_cost(daily_energy, days, rate):
    """
    @brief Calculates monthly electricity cost.
    @param daily_energy Daily energy consumption in kWh.
    @param days Number of days.
    @param rate Electricity price per kWh.
    @return Monthly electricity cost.
    """
    return daily_energy * days * rate


# Main program
print("STANDBY POWER CALCULATOR")

power = float(input("Enter standby power (W): "))
hours = float(input("Enter standby hours per day: "))
days = int(input("Enter number of days: "))
rate = float(input("Enter electricity rate per kWh (Rs.): "))

if (power < 0 or hours < 0 or hours > 24 or
        days <= 0 or rate < 0):
    print("Invalid input.")
else:
    daily_energy = calculate_daily_energy(power, hours)
    monthly_energy = daily_energy * days
    cost = calculate_monthly_cost(daily_energy, days, rate)

    print(f"\nDaily Energy: {daily_energy:.2f} kWh")
    print(f"Total Energy: {monthly_energy:.2f} kWh")
    print(f"Total Electricity Cost: Rs. {cost:.2f}")