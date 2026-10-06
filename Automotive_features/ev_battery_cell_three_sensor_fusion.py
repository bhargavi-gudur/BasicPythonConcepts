"""
@file ev_battery_cell_three_sensor_fusion.py
@author Gandla Bhargavi
@brief Simple EV battery cell voltage, current and temperature sensor fusion.
@date 06-10-2026
"""

cells = [
    {"id": 1, "voltage": 3.72, "current": 120.0, "temperature": 34.5},
    {"id": 2, "voltage": 3.70, "current": 145.0, "temperature": 38.5},
    {"id": 3, "voltage": 3.35, "current": 230.0, "temperature": 52.0},
    {"id": 4, "voltage": 3.74, "current": 130.0, "temperature": 36.0},
    {"id": 5, "voltage": 3.65, "current": 210.0, "temperature": 43.5},
    {"id": 6, "voltage": 3.71, "current": 150.0, "temperature": 41.0}
]

MIN_VOLTAGE = 3.40
MAX_CURRENT = 200.0
WARNING_TEMPERATURE = 40.0
CRITICAL_TEMPERATURE = 50.0

print("===== EV BATTERY CELL 3-SENSOR MONITOR =====")

abnormal_cells = 0

for cell in cells:

    voltage = cell["voltage"]
    current = cell["current"]
    temperature = cell["temperature"]

    low_voltage = voltage < MIN_VOLTAGE
    overcurrent = current > MAX_CURRENT
    high_temperature = temperature > WARNING_TEMPERATURE
    critical_temperature = temperature > CRITICAL_TEMPERATURE

    if critical_temperature and overcurrent and low_voltage:
        fault = "MULTIPLE FAULT"
        status = "CRITICAL"

    elif critical_temperature and overcurrent:
        fault = "THERMAL + CURRENT"
        status = "CRITICAL"

    elif critical_temperature and low_voltage:
        fault = "THERMAL + VOLTAGE"
        status = "CRITICAL"

    elif overcurrent and low_voltage:
        fault = "CURRENT + VOLTAGE"
        status = "WARNING"

    elif critical_temperature:
        fault = "HIGH TEMPERATURE"
        status = "CRITICAL"

    elif overcurrent:
        fault = "OVERCURRENT"
        status = "WARNING"

    elif low_voltage:
        fault = "LOW VOLTAGE"
        status = "WARNING"

    elif high_temperature:
        fault = "ELEVATED TEMPERATURE"
        status = "WARNING"

    else:
        fault = "NO FAULT"
        status = "NORMAL"

    if status != "NORMAL":
        abnormal_cells += 1

    print(
        f"Cell {cell['id']} | "
        f"Voltage: {voltage:.2f} V | "
        f"Current: {current:.1f} A | "
        f"Temperature: {temperature:.1f} C | "
        f"Fault: {fault} | "
        f"{status}"
    )

average_voltage = sum(
    cell["voltage"]
    for cell in cells
) / len(cells)

lowest_voltage_cell = min(
    cells,
    key=lambda cell: cell["voltage"]
)

highest_current_cell = max(
    cells,
    key=lambda cell: cell["current"]
)

hottest_cell = max(
    cells,
    key=lambda cell: cell["temperature"]
)

critical_cells = sum(
    cell["temperature"] > CRITICAL_TEMPERATURE
    for cell in cells
)

print(f"\nAverage Cell Voltage : {average_voltage:.3f} V")

print(
    f"Lowest Voltage Cell  : Cell "
    f"{lowest_voltage_cell['id']} "
    f"({lowest_voltage_cell['voltage']:.2f} V)"
)

print(
    f"Highest Current Cell : Cell "
    f"{highest_current_cell['id']} "
    f"({highest_current_cell['current']:.1f} A)"
)

print(
    f"Hottest Cell         : Cell "
    f"{hottest_cell['id']} "
    f"({hottest_cell['temperature']:.1f} C)"
)

print(f"Critical Cells       : {critical_cells}")
print(f"Abnormal Cells       : {abnormal_cells}")

if critical_cells > 0:

    print("\nSystem Status : CRITICAL")
    print("Battery Alert : Critical cell condition detected")
    print("Action        : Reduce simulated battery load and inspect affected cell.")

elif abnormal_cells > 0:

    print("\nSystem Status : WARNING")
    print("Battery Alert : Cell-level electrical or thermal anomaly detected")
    print("Action        : Continue monitoring affected cells.")

else:

    print("\nSystem Status : NORMAL")
    print("Battery Alert : All cell parameters are within demo limits")
    print("Action        : Continue monitoring.")

print("===============================================")