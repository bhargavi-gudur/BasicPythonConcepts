"""
@file ev_battery_median_filter.py
@author Gandla Bhargavi
@brief Simple EV battery voltage and temperature median filtering.
@date 12-10-2026
"""

from statistics import median

sensor_data = [
    {
        "id": 1,
        "voltage": [3.71, 3.72, 3.71, 3.72, 3.71],
        "temperature": [34.0, 34.2, 34.1, 34.3, 34.2]
    },
    {
        "id": 2,
        "voltage": [3.70, 3.71, 3.70, 3.71, 3.95],
        "temperature": [36.0, 36.2, 36.5, 36.4, 36.3]
    },
    {
        "id": 3,
        "voltage": [3.72, 3.71, 3.73, 3.72, 3.71],
        "temperature": [38.0, 38.2, 38.4, 38.3, 48.0]
    }
]

VOLTAGE_SPIKE_LIMIT = 0.05
TEMPERATURE_SPIKE_LIMIT = 3.0

print("===== EV BATTERY MEDIAN FILTER =====")

abnormal_sensors = 0

for sensor in sensor_data:

    raw_voltage = sensor["voltage"][-1]
    raw_temperature = sensor["temperature"][-1]

    median_voltage = median(sensor["voltage"])
    median_temperature = median(sensor["temperature"])

    voltage_deviation = abs(
        raw_voltage - median_voltage
    )

    temperature_deviation = abs(
        raw_temperature - median_temperature
    )

    voltage_spike = (
        voltage_deviation > VOLTAGE_SPIKE_LIMIT
    )

    temperature_spike = (
        temperature_deviation > TEMPERATURE_SPIKE_LIMIT
    )

    if voltage_spike and temperature_spike:
        status = "CHECK BOTH SENSORS"
    elif voltage_spike:
        status = "CHECK VOLTAGE"
    elif temperature_spike:
        status = "CHECK TEMPERATURE"
    else:
        status = "NORMAL"

    if voltage_spike or temperature_spike:
        abnormal_sensors += 1

    print(
        f"Sensor {sensor['id']} | "
        f"Raw Voltage: {raw_voltage:.3f} V | "
        f"Median Voltage: {median_voltage:.3f} V | "
        f"Raw Temperature: {raw_temperature:.1f} C | "
        f"Median Temperature: {median_temperature:.1f} C | "
        f"{status}"
    )

print(f"\nSensors Requiring Review: {abnormal_sensors}")

if abnormal_sensors > 0:
    print("System Status : SENSOR REVIEW REQUIRED")
    print("Action        : Verify abnormal readings against sensor diagnostics.")
else:
    print("System Status : NORMAL")
    print("Action        : Continue monitoring sensor readings.")

print("====================================")