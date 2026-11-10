"""
@file VoltageMonitor.py
@brief Monitors electrical voltage and identifies voltage variations.
@date 10/11/2026
"""


def check_voltage(voltage, minimum, maximum):
    """
    @brief Check the voltage condition.
    @param voltage Measured voltage in volts.
    @param minimum Minimum permitted voltage.
    @param maximum Maximum permitted voltage.
    @return Voltage status.
    """
    if voltage < minimum:
        return "LOW VOLTAGE DETECTED!"
    elif voltage > maximum:
        return "HIGH VOLTAGE DETECTED!"
    else:
        return "Voltage is within the permitted range."


def main():
    """Run the voltage monitoring application."""

    print("===== VOLTAGE MONITORING SYSTEM =====")
    print("Date: 10/11/2026\n")

    try:
        voltage = float(input("Enter measured voltage (V): "))
        minimum = float(input("Enter minimum voltage limit (V): "))
        maximum = float(input("Enter maximum voltage limit (V): "))

        if voltage < 0 or minimum < 0 or maximum <= minimum:
            print("Invalid input!")
            return

        print("\n===== VOLTAGE REPORT =====")
        print(f"Measured Voltage : {voltage:.2f} V")
        print(f"Minimum Limit   : {minimum:.2f} V")
        print(f"Maximum Limit   : {maximum:.2f} V")

        print("STATUS:", check_voltage(voltage, minimum, maximum))

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()