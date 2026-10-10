"""
@file ev_battery_sensor_noise_filter.py
@author Gandla Bhargavi
@brief Simple EV battery voltage and temperature noise filtering.
@date 11-10-2026
"""

sensor_data = [
    {
        "id": 1,
        "voltage": [3.71, 3.72, 3.71, 3.72, 3.71],
        "temperature": [34.0, 34.5, 34.2, 34.4, 34.3]
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
    }
]

WINDOW_SIZE = 3
VOLTAGE_LIMIT = 0.05
TEMPERATURE_LIMIT = 3.0


def moving_average(readings):
    window = readings[-WINDOW_SIZE:]
    return sum(window) / len(window)


print("===== EV BATTERY SENSOR NOISE FILTER =====")

abnormal_sensors = 0

for sensor in sensor_data:

    raw_voltage = sensor["voltage"][-1]
    raw_temperature = sensor["temperature"][-1]

    filtered_voltage = moving_average(sensor["voltage"])
    filtered_temperature = moving_average(
        sensor["temperature"]
    )

    voltage_difference = abs(
        raw_voltage - filtered_voltage
    )

    temperature_difference = abs(
        raw_temperature - filtered_temperature
    )

    voltage_noise = voltage_difference > VOLTAGE_LIMIT
    temperature_noise = (
        temperature_difference > TEMPERATURE_LIMIT
    )

    if voltage_noise and temperature_noise:
        status = "CHECK BOTH SENSORS"
    elif voltage_noise:
        status = "CHECK VOLTAGE"
    elif temperature_noise:
        status = "CHECK TEMPERATURE"
    else:
        status = "STABLE"

    if voltage_noise or temperature_noise:
        abnormal_sensors += 1

    print(
        f"Sensor {sensor['id']} | "
        f"Raw Voltage: {raw_voltage:.3f} V | "
        f"Filtered Voltage: {filtered_voltage:.3f} V | "
        f"Raw Temperature: {raw_temperature:.1f} C | "
        f"Filtered Temperature: {filtered_temperature:.3f} C | "
        f"{status}"
    )

print(f"\nSensors Requiring Review: {abnormal_sensors}")

if abnormal_sensors > 0:
    print("System Status : SENSOR REVIEW REQUIRED")
    print("Action        : Verify unusual readings against sensor diagnostics.")
else:
    print("System Status : STABLE")
    print("Action        : Continue monitoring filtered readings.")

print("===========================================")