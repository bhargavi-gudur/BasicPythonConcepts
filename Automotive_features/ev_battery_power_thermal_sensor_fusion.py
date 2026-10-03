"""
@file ev_battery_power_thermal_sensor_fusion.py
@author Gandla Bhargavi
@brief Simple EV battery voltage, current and temperature sensor fusion.
@date 03-10-2026
"""

battery_data = [
    {"id": 1, "voltage": 360.0, "current": 120.0, "temperature": 34.5},
    {"id": 2, "voltage": 365.0, "current": 145.0, "temperature": 38.0},
    {"id": 3, "voltage": 370.0, "current": 230.0, "temperature": 49.0},
    {"id": 4, "voltage": 362.0, "current": 130.0, "temperature": 36.5},
    {"id": 5, "voltage": 368.0, "current": 150.0, "temperature": 42.0}
]

MAX_POWER = 80.0
MAX_TEMPERATURE = 45.0

print("===== EV BATTERY POWER + THERMAL MONITOR =====")

abnormal_count = 0

for sensor in battery_data:

    voltage = sensor["voltage"]
    current = sensor["current"]
    temperature = sensor["temperature"]

    power = (voltage * current) / 1000

    power_high = power > MAX_POWER
    temperature_high = temperature > MAX_TEMPERATURE

    if power_high and temperature_high:
        status = "CRITICAL"
    elif power_high or temperature_high:
        status = "WARNING"
    else:
        status = "NORMAL"

    if status != "NORMAL":
        abnormal_count += 1

    print(
        f"Sensor {sensor['id']} | "
        f"Voltage: {voltage:.1f} V | "
        f"Current: {current:.1f} A | "
        f"Power: {power:.1f} kW | "
        f"Temperature: {temperature:.1f} C | "
        f"{status}"
    )

average_power = sum(
    (sensor["voltage"] * sensor["current"]) / 1000
    for sensor in battery_data
) / len(battery_data)

highest_power = max(
    battery_data,
    key=lambda sensor:
    sensor["voltage"] * sensor["current"]
)

hottest_sensor = max(
    battery_data,
    key=lambda sensor: sensor["temperature"]
)

power_anomalies = sum(
    (sensor["voltage"] * sensor["current"]) / 1000
    > MAX_POWER
    for sensor in battery_data
)

print(f"\nAverage Power    : {average_power:.1f} kW")

print(
    f"Highest Power    : Sensor "
    f"{highest_power['id']} "
    f"({highest_power['voltage'] * highest_power['current'] / 1000:.1f} kW)"
)

print(
    f"Hottest Sensor   : Sensor "
    f"{hottest_sensor['id']} "
    f"({hottest_sensor['temperature']:.1f} C)"
)

print(f"Power Anomalies  : {power_anomalies}")
print(f"Abnormal Sensors : {abnormal_count}")

highest_power_value = (
    highest_power["voltage"] *
    highest_power["current"]
) / 1000

if (
    highest_power_value > MAX_POWER
    and hottest_sensor["temperature"] > MAX_TEMPERATURE
):
    print("\nSystem Status : CRITICAL")
    print("Battery Alert : High power and thermal anomaly detected")
    print("Action        : Reduce simulated battery load and inspect sensor.")
elif abnormal_count > 0:
    print("\nSystem Status : WARNING")
    print("Battery Alert : Electrical or thermal anomaly detected")
    print("Action        : Continue monitoring.")
else:
    print("\nSystem Status : NORMAL")
    print("Battery Alert : Battery parameters are within demo limits")
    print("Action        : Continue monitoring.")

print("=================================================")