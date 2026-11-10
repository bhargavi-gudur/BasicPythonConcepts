"""
@file CurrentMonitor.py
@brief Monitors electrical current and detects abnormal conditions.
@date 11/11/2026
"""


def check_current(current, minimum, maximum):
    """
    @brief Check the electrical current condition.
    @param current Measured current in amperes.
    @param minimum Minimum current limit.
    @param maximum Maximum current limit.
    @return Current status.
    """
    if current < minimum:
        return "LOW CURRENT DETECTED!"
    elif current > maximum:
        return "OVERCURRENT DETECTED!"
    else:
        return "Current is within the permitted range."


def calculate_power(voltage, current):
    """
    @brief Calculate electrical power.
    @param voltage Supply voltage in volts.
    @param current Current in amperes.
    @return Power in watts.
    """
    return voltage * current


def main():
    """Run the current monitoring system."""

    print("===== CURRENT MONITORING SYSTEM =====")
    print("Date: 11/11/2026\n")

    try:
        voltage = float(input("Enter supply voltage (V): "))
        current = float(input("Enter measured current (A): "))
        minimum = float(input("Enter minimum current limit (A): "))
        maximum = float(input("Enter maximum current limit (A): "))

        if (voltage < 0 or current < 0 or minimum < 0
                or maximum <= minimum):
            print("Invalid input!")
            return

        power = calculate_power(voltage, current)

        print("\n===== CURRENT REPORT =====")
        print(f"Supply Voltage  : {voltage:.2f} V")
        print(f"Measured Current: {current:.2f} A")
        print(f"Electrical Power: {power:.2f} W")

        print("STATUS:", check_current(current, minimum, maximum))

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()