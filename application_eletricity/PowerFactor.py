"""
@file PowerFactor.py
@brief Calculates electrical power factor.
@date 09/11/2026
"""


def calculate_apparent_power(voltage, current):
    """
    @brief Calculate apparent power.
    @param voltage Supply voltage in volts.
    @param current Current in amperes.
    @return Apparent power in VA.
    """
    return voltage * current


def calculate_power_factor(real_power, apparent_power):
    """
    @brief Calculate power factor.
    @param real_power Real power in watts.
    @param apparent_power Apparent power in VA.
    @return Power factor.
    """
    return real_power / apparent_power


def main():
    """Run the power factor calculator."""

    print("===== POWER FACTOR CALCULATOR =====")
    print("Date: 09/11/2026\n")

    try:
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))
        real_power = float(input("Enter real power (W): "))

        if voltage <= 0 or current <= 0 or real_power < 0:
            print("Invalid input!")
            return

        apparent_power = calculate_apparent_power(voltage, current)

        if real_power > apparent_power:
            print("Invalid power values!")
            return

        pf = calculate_power_factor(real_power, apparent_power)

        print("\n===== POWER FACTOR REPORT =====")
        print(f"Apparent Power : {apparent_power:.2f} VA")
        print(f"Real Power     : {real_power:.2f} W")
        print(f"Power Factor   : {pf:.2f}")

        if pf >= 0.95:
            print("Status: Good Power Factor")
        else:
            print("Status: Power Factor Needs Improvement")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()