"""
@file ev_battery_cell_sensor_fusion.py
@author Gandla Bhargavi
@brief Simple EV battery cell voltage and temperature sensor fusion.
@date 01-10-2026
"""

cells = [
    {"id": 1, "voltage": 3.72, "temperature": 34.5},
    {"id": 2, "voltage": 3.74, "temperature": 36.2},
    {"id": 3, "voltage": 3.71, "temperature": 35.8},
    {"id": 4, "voltage": 3.73, "temperature": 37.1},
    {"id": 5, "voltage": 3.58, "temperature": 49.5},
    {"id": 6, "voltage": 3.75, "temperature": 36.8}
]

VOLTAGE_LIMIT = 0.05
TEMPERATURE_LIMIT = 45.0

# Average voltage
average_voltage = sum(
    cell["voltage"] for cell in cells
) / len(cells)

print("===== EV BATTERY CELL SENSOR FUSION =====")

abnormal_cells = 0

for cell in cells:
    voltage_difference = (
        cell["voltage"] - average_voltage
    )

    voltage_abnormal = (
        abs(voltage_difference) > VOLTAGE_LIMIT
    )

    temperature_abnormal = (
        cell["temperature"] > TEMPERATURE_LIMIT
    )

    if voltage_abnormal and temperature_abnormal:
        status = "CRITICAL"
    elif voltage_abnormal or temperature_abnormal:
        status = "WARNING"
    else:
        status = "NORMAL"

    if status != "NORMAL":
        abnormal_cells += 1

    print(
        f"Cell {cell['id']} | "
        f"Voltage: {cell['voltage']:.3f} V | "
        f"Temperature: {cell['temperature']:.1f} °C | "
        f"{status}"
    )

# Find extreme values
hottest_cell = max(
    cells,
    key=lambda cell: cell["temperature"]
)

lowest_voltage_cell = min(
    cells,
    key=lambda cell: cell["voltage"]
)

print(f"\nAverage Voltage : {average_voltage:.3f} V")

print(
    f"Hottest Cell    : Cell {hottest_cell['id']} "
    f"({hottest_cell['temperature']:.1f} °C)"
)

print(
    f"Lowest Voltage  : Cell {lowest_voltage_cell['id']} "
    f"({lowest_voltage_cell['voltage']:.3f} V)"
)

print(f"Abnormal Cells  : {abnormal_cells}")

if (
    hottest_cell["temperature"] > TEMPERATURE_LIMIT
    and abs(
        hottest_cell["voltage"] - average_voltage
    ) > VOLTAGE_LIMIT
):
    print("System Status   : CRITICAL")
    print("Battery Alert   : Cell voltage and temperature anomaly")
    print("Action          : Reduce battery load and inspect cell.")
elif abnormal_cells > 0:
    print("System Status   : WARNING")
    print("Battery Alert   : Abnormal cell sensor data detected")
    print("Action          : Check cell condition and BMS balancing.")
else:
    print("System Status   : NORMAL")
    print("Battery Alert   : Cell parameters are within limits")
    print("Action          : Continue monitoring.")

print("============================================")