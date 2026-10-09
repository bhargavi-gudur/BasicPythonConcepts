"""
@file ev_battery_cell_moving_average.py
@author Gandla Bhargavi
@brief Simple EV battery cell moving-average anomaly detection.
@date 10-10-2026
"""

cells = [
    {
        "id": 1,
        "voltage": [3.71, 3.72, 3.71, 3.72, 3.71],
        "temperature": [34.0, 34.5, 35.0, 34.8, 35.0]
    },
    {
        "id": 2,
        "voltage": [3.70, 3.71, 3.70, 3.71, 3.50],
        "temperature": [36.0, 36.5, 37.0, 37.5, 46.0]
    },
    {
        "id": 3,
        "voltage": [3.72, 3.71, 3.73, 3.72, 3.71],
        "temperature": [38.0, 38.5, 39.0, 39.2, 39.5]
    },
    {
        "id": 4,
        "voltage": [3.69, 3.70, 3.69, 3.70, 3.68],
        "temperature": [35.0, 35.5, 35.8, 36.0, 36.2]
    }
]

VOLTAGE_LIMIT = 0.05
TEMPERATURE_LIMIT = 5.0

print("===== EV BATTERY MOVING AVERAGE MONITOR =====")

abnormal_cells = 0

for cell in cells:

    # All readings except the latest form the baseline.
    previous_voltages = cell["voltage"][:-1]
    previous_temperatures = cell["temperature"][:-1]

    average_voltage = (
        sum(previous_voltages) / len(previous_voltages)
    )

    average_temperature = (
        sum(previous_temperatures) / len(previous_temperatures)
    )

    current_voltage = cell["voltage"][-1]
    current_temperature = cell["temperature"][-1]

    voltage_deviation = current_voltage - average_voltage

    temperature_deviation = (
        current_temperature - average_temperature
    )

    voltage_anomaly = (
        abs(voltage_deviation) > VOLTAGE_LIMIT
    )

    temperature_anomaly = (
        abs(temperature_deviation) > TEMPERATURE_LIMIT
    )

    if voltage_anomaly and temperature_anomaly:
        status = "CRITICAL"
    elif voltage_anomaly or temperature_anomaly:
        status = "WARNING"
    else:
        status = "NORMAL"

    if status != "NORMAL":
        abnormal_cells += 1

    print(
        f"Cell {cell['id']} | "
        f"Average Voltage: {average_voltage:.3f} V | "
        f"Current Voltage: {current_voltage:.3f} V | "
        f"Voltage Deviation: {voltage_deviation:.3f} V | "
        f"Average Temperature: {average_temperature:.2f} C | "
        f"Current Temperature: {current_temperature:.1f} C | "
        f"Temperature Deviation: {temperature_deviation:.2f} C | "
        f"{status}"
    )

print(f"\nAbnormal Cells: {abnormal_cells}")

if abnormal_cells > 0:
    print("System Status : WARNING")
    print("Battery Alert : Moving-average anomaly detected")
    print("Action        : Verify sensor readings and inspect affected cells.")
else:
    print("System Status : NORMAL")
    print("Battery Alert : No anomalies detected by demo thresholds")
    print("Action        : Continue monitoring.")

print("==============================================")