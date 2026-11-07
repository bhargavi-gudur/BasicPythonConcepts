"""
@file ApplianceRuntime.py
@brief Calculates appliance runtime and electricity consumption.
@date 07/11/2026
"""


def calculate_energy(power, hours):
    """
    @brief Calculate electricity consumption.
    @param power Appliance power in watts.
    @param hours Operating time in hours.
    @return Energy consumed in kWh.
    """
    return (power * hours) / 1000


def calculate_cost(energy, rate):
    """
    @brief Calculate electricity cost.
    @param energy Energy consumed in kWh.
    @param rate Electricity tariff per unit.
    @return Total electricity cost.
    """
    return energy * rate


def main():
    """Run the appliance runtime calculator."""

    print("===== APPLIANCE RUNTIME CALCULATOR =====")
    print("Date: 07/11/2026\n")

    try:
        power = float(input("Enter appliance power (Watts): "))
        hours = float(input("Enter operating time (Hours): "))
        rate = float(input("Enter electricity rate (Rs./unit): "))

        if power < 0 or hours < 0 or rate < 0:
            print("Invalid input!")
            return

        energy = calculate_energy(power, hours)
        cost = calculate_cost(energy, rate)

        print("\n===== APPLIANCE REPORT =====")
        print(f"Power Rating       : {power:.2f} W")
        print(f"Operating Time     : {hours:.2f} Hours")
        print(f"Energy Consumption : {energy:.2f} kWh")
        print(f"Electricity Cost   : Rs. {cost:.2f}")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()