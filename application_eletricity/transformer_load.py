"""
@file transformer_load.py
@brief Calculates transformer capacity and allowable loading.
@date 17/11/2026
"""

def calculate_capacity(voltage, current):
    """
    @brief Calculates transformer capacity in kVA.
    @param voltage Secondary voltage in volts.
    @param current Rated secondary current in amperes.
    @return Transformer capacity in kVA.
    """
    return (voltage * current) / 1000


def calculate_load(capacity, percentage):
    """
    @brief Calculates load capacity at a selected loading percentage.
    @param capacity Transformer capacity in kVA.
    @param percentage Desired loading percentage.
    @return Allowable load in kVA.
    """
    return capacity * percentage / 100


# Main program
print("TRANSFORMER LOAD CAPACITY CALCULATOR")

voltage = float(input("Enter secondary voltage (V): "))
current = float(input("Enter rated secondary current (A): "))
percentage = float(input("Enter desired loading percentage: "))

if (voltage <= 0 or current <= 0 or
        percentage <= 0 or percentage > 100):
    print("Invalid input.")
else:
    capacity = calculate_capacity(voltage, current)
    load = calculate_load(capacity, percentage)

    print(f"\nTransformer Capacity: {capacity:.2f} kVA")
    print(f"Estimated Load Capacity: {load:.2f} kVA")