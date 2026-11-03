"""
@file ElectricityTheft.py
@brief Detects abnormal differences in electricity meter readings.
@date 03/11/2026
"""


def calculate_difference(main_meter, consumer_meter):
    """
    @brief Calculate the difference between meter readings.
    @param main_meter Main meter units.
    @param consumer_meter Consumer meter units.
    @return Difference in electricity units.
    """
    return main_meter - consumer_meter


def detect_theft(difference, limit):
    """
    @brief Check whether the difference exceeds the allowed limit.
    @param difference Difference between meter readings.
    @param limit Allowed difference.
    @return True if suspicious difference is detected.
    """
    return difference > limit


def main():
    """Run the electricity theft detection application."""

    print("===== ELECTRICITY THEFT DETECTION =====")
    print("Date: 03/11/2026\n")

    try:
        main_meter = float(input("Enter main meter units: "))
        consumer_meter = float(input("Enter consumer meter units: "))
        limit = float(input("Enter allowed difference: "))

        if main_meter < 0 or consumer_meter < 0 or limit < 0:
            print("Invalid input!")
            return

        difference = calculate_difference(
            main_meter, consumer_meter
        )

        print("\n===== DETECTION REPORT =====")
        print(f"Main Meter Units     : {main_meter:.2f}")
        print(f"Consumer Meter Units : {consumer_meter:.2f}")
        print(f"Difference           : {difference:.2f}")

        if difference < 0:
            print("ALERT: Meter readings are inconsistent!")
        elif detect_theft(difference, limit):
            print("ALERT: Suspicious energy difference detected!")
        else:
            print("STATUS: No abnormal difference detected.")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()