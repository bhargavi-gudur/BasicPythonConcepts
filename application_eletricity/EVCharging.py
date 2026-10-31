"""
@file EVCharging.py
@brief Calculates electric vehicle charging cost and time.
@date 01/11/2026
"""


def calculate_energy(capacity, percentage):
    """
    @brief Calculate required charging energy.
    @param capacity Battery capacity in kWh.
    @param percentage Charging percentage required.
    @return Energy required in kWh.
    """
    return capacity * percentage / 100


def calculate_cost(energy, rate):
    """
    @brief Calculate charging cost.
    @param energy Energy required in kWh.
    @param rate Electricity rate per unit.
    @return Total charging cost.
    """
    return energy * rate


def calculate_time(energy, power):
    """
    @brief Calculate ideal charging time.
    @param energy Energy required in kWh.
    @param power Charger power in kW.
    @return Charging time in hours.
    """
    return energy / power


def main():
    """Run the EV charging calculator."""

    print("===== EV CHARGING CALCULATOR =====")
    print("Date: 01/11/2026\n")

    try:
        capacity = float(input("Enter battery capacity (kWh): "))
        percentage = float(input("Enter charging percentage (%): "))
        rate = float(input("Enter electricity rate (Rs./kWh): "))
        charger_power = float(input("Enter charger power (kW): "))

        if (capacity <= 0 or not 0 <= percentage <= 100
                or rate < 0 or charger_power <= 0):
            print("Invalid input!")
            return

        energy = calculate_energy(capacity, percentage)
        cost = calculate_cost(energy, rate)
        time = calculate_time(energy, charger_power)

        print("\n===== CHARGING REPORT =====")
        print(f"Energy Required : {energy:.2f} kWh")
        print(f"Charging Cost  : Rs. {cost:.2f}")
        print(f"Charging Time  : {time:.2f} hours")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()