"""
@file ShortCircuit.py
@brief Identifies possible electrical overcurrent conditions.
@date 08/11/2026
"""


def detect_overcurrent(current, limit):
    """
    @brief Check whether current exceeds the safety limit.
    @param current Measured current in amperes.
    @param limit Maximum permitted current.
    @return True if current exceeds the limit.
    """
    return current > limit


def calculate_power(voltage, current):
    """
    @brief Calculate electrical power.
    @param voltage Supply voltage in volts.
    @param current Current in amperes.
    @return Power in watts.
    """
    return voltage * current


def main():
    """Run the short circuit detection simulation."""

    print("===== SHORT CIRCUIT DETECTION SYSTEM =====")
    print("Date: 08/11/2026\n")

    try:
        voltage = float(input("Enter supply voltage (V): "))
        current = float(input("Enter measured current (A): "))
        limit = float(input("Enter maximum current limit (A): "))

        if voltage < 0 or current < 0 or limit <= 0:
            print("Invalid input!")
            return

        power = calculate_power(voltage, current)

        print("\n===== ELECTRICAL SAFETY REPORT =====")
        print(f"Supply Voltage : {voltage:.2f} V")
        print(f"Current        : {current:.2f} A")
        print(f"Power          : {power:.2f} W")

        if detect_overcurrent(current, limit):
            print("WARNING: OVERCURRENT DETECTED!")
        else:
            print("STATUS: Current is within the set limit.")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()