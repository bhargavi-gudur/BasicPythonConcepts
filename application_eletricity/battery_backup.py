"""
@file battery_backup.py
@brief Estimates battery backup runtime.
@date 12/11/2026
"""

def calculate_backup(voltage, capacity, efficiency, load):
    """
    @brief Calculates estimated battery backup time.
    @param voltage Battery voltage in volts.
    @param capacity Battery capacity in Ah.
    @param efficiency Usable efficiency in percentage.
    @param load Connected load in watts.
    @return Estimated backup time in hours.
    """
    usable_energy = voltage * capacity * efficiency / 100
    return usable_energy / load


# Main program
print("BATTERY BACKUP RUNTIME ESTIMATOR")

voltage = float(input("Enter battery voltage (V): "))
capacity = float(input("Enter battery capacity (Ah): "))
efficiency = float(input("Enter battery efficiency (%): "))
load = float(input("Enter connected load (W): "))

if (voltage <= 0 or capacity <= 0 or
        efficiency <= 0 or efficiency > 100 or load <= 0):
    print("Invalid input. Enter positive values and efficiency up to 100%.")
else:
    backup = calculate_backup(
        voltage, capacity, efficiency, load
    )

    print(f"\nEstimated Backup Time: {backup:.2f} hours")