"""
@file voltage_drop.py
@brief Calculates voltage drop in a two-wire DC circuit.
@date 14/11/2026
"""

COPPER_RESISTIVITY = 0.0175

def calculate_voltage_drop(length, current, area):
    """
    @brief Calculates voltage drop across a copper wire pair.
    @param length One-way wire length in metres.
    @param current Current in amperes.
    @param area Wire cross-sectional area in mm^2.
    @return Voltage drop in volts.
    """
    return (2 * length * current * COPPER_RESISTIVITY) / area


# Main program
print("WIRE VOLTAGE DROP CALCULATOR")

supply = float(input("Enter supply voltage (V): "))
length = float(input("Enter one-way wire length (m): "))
current = float(input("Enter current (A): "))
area = float(input("Enter wire area (mm^2): "))

if supply <= 0 or length <= 0 or current < 0 or area <= 0:
    print("Invalid input.")
else:
    drop = calculate_voltage_drop(length, current, area)
    load_voltage = supply - drop
    percentage = (drop / supply) * 100

    print(f"\nVoltage Drop: {drop:.2f} V")
    print(f"Load Voltage: {load_voltage:.2f} V")
    print(f"Voltage Drop Percentage: {percentage:.2f}%")