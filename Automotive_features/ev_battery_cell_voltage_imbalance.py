"""
@file ev_battery_cell_voltage_imbalance.py
@author Gandla Bhargavi
@brief Simple EV battery cell voltage imbalance detection.
@date 30-09-2026
"""

# Battery cell voltages
cells = [
    {"id": 1, "voltage": 3.72},
    {"id": 2, "voltage": 3.74},
    {"id": 3, "voltage": 3.71},
    {"id": 4, "voltage": 3.73},
    {"id": 5, "voltage": 3.60},
    {"id": 6, "voltage": 3.75}
]

IMBALANCE_LIMIT = 0.05

# Calculate average voltage
total_voltage = sum(cell["voltage"] for cell in cells)
average_voltage = total_voltage / len(cells)

print("===== EV BATTERY CELL VOLTAGE MONITOR =====")

imbalanced_cells = 0

for cell in cells:
    voltage = cell["voltage"]
    difference = voltage - average_voltage

    if abs(difference) > IMBALANCE_LIMIT:
        status = "IMBALANCED"
        imbalanced_cells += 1
    else:
        status = "NORMAL"

    print(
        f"Cell {cell['id']} | "
        f"Voltage: {voltage:.3f} V | "
        f"Difference: {difference:.3f} V | "
        f"{status}"
    )

# Find highest and lowest cells
highest_cell = max(cells, key=lambda cell: cell["voltage"])
lowest_cell = min(cells, key=lambda cell: cell["voltage"])

voltage_spread = (
    highest_cell["voltage"] -
    lowest_cell["voltage"]
)

print(f"\nAverage Voltage  : {average_voltage:.3f} V")
print(
    f"Highest Cell     : Cell {highest_cell['id']} "
    f"({highest_cell['voltage']:.3f} V)"
)
print(
    f"Lowest Cell      : Cell {lowest_cell['id']} "
    f"({lowest_cell['voltage']:.3f} V)"
)
print(f"Voltage Spread   : {voltage_spread:.3f} V")
print(f"Imbalanced Cells : {imbalanced_cells}")

if imbalanced_cells > 0:
    print("System Status    : WARNING")
    print("Battery Alert    : Cell voltage imbalance detected")
    print("Action           : Check cell condition and balancing system.")
else:
    print("System Status    : NORMAL")
    print("Battery Alert    : Cell voltages are balanced")
    print("Action           : Continue monitoring.")

print("============================================")