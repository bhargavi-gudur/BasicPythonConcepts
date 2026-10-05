"""
@file ev_battery_voltage_temperature_derating.py
@author Gandla Bhargavi
@brief Simple EV battery voltage and temperature thermal derating detection.
@date 05-10-2026
"""

battery_data = [
    {"id": 1, "voltage": 360.0, "temperature": 34.5},
    {"id": 2, "voltage": 355.0, "temperature": 41.5},
    {"id": 3, "voltage": 335.0, "temperature": 52.0},
    {"id": 4, "voltage": 362.0, "temperature": 37.0},
    {"id": 5, "voltage": 345.0, "temperature": 44.0}
]

WARNING_TEMPERATURE = 40.0
CRITICAL_TEMPERATURE = 50.0
MIN_VOLTAGE = 340.0

print("===== EV BATTERY THERMAL DERATING MONITOR =====")

abnormal_count = 0

for sensor in battery_data:

    voltage = sensor["voltage"]
    temperature = sensor["temperature"]

    low_voltage = voltage < MIN_VOLTAGE
    high_temperature = temperature > WARNING_TEMPERATURE
    critical_temperature = temperature > CRITICAL_TEMPERATURE

    if critical_temperature and low_voltage:
        status = "CRITICAL"
        derating = 50
    elif critical_temperature:
        status = "CRITICAL"
        derating = 40
    elif high_temperature and low_voltage:
        status = "WARNING"
        derating = 30
    elif high_temperature:
        status = "WARNING"
        derating = 20
    else:
        status = "NORMAL"
        derating = 0

    if status != "NORMAL":
        abnormal_count += 1

    print(
        f"Sensor {sensor['id']} | "
        f"Voltage: {voltage:.1f} V | "
        f"Temperature: {temperature:.1f} C | "
        f"{status} | "
        f"Derating: {derating}%"
    )

average_temperature = sum(
    sensor["temperature"]
    for sensor in battery_data
) / len(battery_data)

hottest_sensor = max(
    battery_data,
    key=lambda sensor: sensor["temperature"]
)

lowest_voltage = min(
    battery_data,
    key=lambda sensor: sensor["voltage"]
)

thermal_warnings = sum(
    sensor["temperature"] > WARNING_TEMPERATURE
    for sensor in battery_data
)

print(f"\nAverage Temperature : {average_temperature:.1f} C")

print(
    f"Hottest Sensor      : Sensor "
    f"{hottest_sensor['id']} "
    f"({hottest_sensor['temperature']:.1f} C)"
)

print(
    f"Lowest Voltage      : Sensor "
    f"{lowest_voltage['id']} "
    f"({lowest_voltage['voltage']:.1f} V)"
)

print(f"Thermal Warnings    : {thermal_warnings}")
print(f"Abnormal Sensors    : {abnormal_count}")

if hottest_sensor["temperature"] > CRITICAL_TEMPERATURE:
    if hottest_sensor["voltage"] < MIN_VOLTAGE:
        derating = 50
    else:
        derating = 40

    print("\nSystem Status : CRITICAL")
    print("Battery Alert : High battery temperature detected")
    print(f"Thermal Action: Apply {derating}% simulated power derating")
    print("Action        : Reduce simulated battery load and inspect cooling system.")

elif abnormal_count > 0:

    if hottest_sensor["temperature"] > WARNING_TEMPERATURE:
        derating = 20
    else:
        derating = 0

    print("\nSystem Status : WARNING")
    print("Battery Alert : Thermal condition requires attention")
    print(f"Thermal Action: Apply {derating}% simulated power derating")
    print("Action        : Continue monitoring battery temperature.")

else:
    print("\nSystem Status : NORMAL")
    print("Battery Alert : Battery temperature is within demo limits")
    print("Thermal Action: No derating required")
    print("Action        : Continue monitoring.")

print("================================================")