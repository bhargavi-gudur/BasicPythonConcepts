"""
@file LoadManagement.py
@brief Calculates and monitors household electrical load.
@date 04/11/2026
"""


def calculate_load(power):
    """
    @brief Calculate total electrical load.
    @param power List of appliance power ratings.
    @return Total load in watts.
    """
    return sum(power)


def check_load(load, limit):
    """
    @brief Check whether electrical load exceeds the limit.
    @param load Total electrical load in watts.
    @param limit Maximum permitted load.
    @return True if load exceeds the limit.
    """
    return load > limit


def main():
    """Run the electricity load management application."""

    print("===== ELECTRICITY LOAD MANAGEMENT =====")
    print("Date: 04/11/2026\n")

    try:
        n = int(input("Enter number of appliances: "))

        if n <= 0:
            print("Invalid number of appliances!")
            return

        power = []

        for i in range(n):
            watts = float(
                input(f"Enter power of appliance {i + 1} (Watts): ")
            )

            if watts < 0:
                print("Invalid power rating!")
                return

            power.append(watts)

        limit = float(input("Enter maximum load limit (Watts): "))

        if limit < 0:
            print("Invalid load limit!")
            return

        total_load = calculate_load(power)

        print("\n===== LOAD REPORT =====")
        print(f"Total Electrical Load: {total_load:.2f} W")
        print(f"Maximum Load Limit   : {limit:.2f} W")

        if check_load(total_load, limit):
            print("WARNING: Electrical overload detected!")
        else:
            print("STATUS: Electrical load is within the limit.")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()