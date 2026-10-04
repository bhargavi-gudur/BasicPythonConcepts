"""
@file ev_battery_current_voltage_fault_detection.py
@author Gandla Bhargavi
@brief Simple EV battery current and voltage fault detection.
@date 04-10-2026
"""

battery_data = [
    {"id": 1, "voltage": 360.0, "current": 120.0},
    {"id": 2, "voltage": 350.0, "current": 145.0},
    {"id": 3, "voltage": 330.0, "current": 230.0},
    {"id": 4, "voltage": 362.0, "current": 130.0},
    {"id": 5, "voltage": 345.0, "current": 210.0}
]

MIN_VOLTAGE = 340.0
MAX_CURRENT = 200.0

print("===== EV BATTERY ELECTRICAL FAULT MONITOR =====")

abnormal_count = 0

for sensor in battery_data:

    voltage = sensor["voltage"]
    current = sensor["current"]

    undervoltage = voltage < MIN_VOLTAGE
    overcurrent = current > MAX_CURRENT

    if undervoltage and overcurrent:
        status = "CRITICAL"
    elif undervoltage or overcurrent:
        status = "WARNING"
    else:
        status = "NORMAL"

    if status != "NORMAL":
        abnormal_count += 1

    print(
        f"Sensor {sensor['id']} | "
        f"Voltage: {voltage:.1f} V | "
        f"Current: {current:.1f} A | "
        f"{status}"
    )

average_voltage = sum(
    sensor["voltage"]
    for sensor in battery_data
) / len(battery_data)

lowest_voltage = min(
    battery_data,
    key=lambda sensor: sensor["voltage"]
)

highest_current = max(
    battery_data,
    key=lambda sensor: sensor["current"]
)

undervoltage_count = sum(
    sensor["voltage"] < MIN_VOLTAGE
    for sensor in battery_data
)

overcurrent_count = sum(
    sensor["current"] > MAX_CURRENT
    for sensor in battery_data
)

print(f"\nAverage Voltage     : {average_voltage:.1f} V")

print(
    f"Lowest Voltage      : Sensor "
    f"{lowest_voltage['id']} "
    f"({lowest_voltage['voltage']:.1f} V)"
)

print(
    f"Highest Current     : Sensor "
    f"{highest_current['id']} "
    f"({highest_current['current']:.1f} A)"
)

print(f"Undervoltage Faults : {undervoltage_count}")
print(f"Overcurrent Faults  : {overcurrent_count}")
print(f"Abnormal Sensors    : {abnormal_count}")

if (
    lowest_voltage["voltage"] < MIN_VOLTAGE
    and highest_current["current"] > MAX_CURRENT
):
    print("\nSystem Status : CRITICAL")
    print("Battery Alert : Combined electrical fault detected")
    print("Action        : Reduce simulated load and inspect battery.")
elif abnormal_count > 0:
    print("\nSystem Status : WARNING")
    print("Battery Alert : Voltage or current anomaly detected")
    print("Action        : Continue monitoring.")
else:
    print("\nSystem Status : NORMAL")
    print("Battery Alert : Electrical parameters are within demo limits")
    print("Action        : Continue monitoring.")

print("================================================")