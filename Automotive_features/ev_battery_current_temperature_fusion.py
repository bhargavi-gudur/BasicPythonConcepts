"""
@file ev_battery_current_temperature_fusion.py
@author Gandla Bhargavi
@brief Simple EV battery current and temperature sensor fusion.
@date 02-10-2026
"""

battery_data = [
    {"id": 1, "current": 145.0, "temperature": 34.5},
    {"id": 2, "current": 175.0, "temperature": 39.2},
    {"id": 3, "current": 230.0, "temperature": 48.5},
    {"id": 4, "current": 160.0, "temperature": 37.8},
    {"id": 5, "current": 190.0, "temperature": 44.0}
]

MAX_CURRENT = 200.0
MAX_TEMPERATURE = 45.0

print("===== EV BATTERY CURRENT + TEMPERATURE MONITOR =====")

abnormal_count = 0

for sensor in battery_data:

    current = sensor["current"]
    temperature = sensor["temperature"]

    current_high = current > MAX_CURRENT
    temperature_high = temperature > MAX_TEMPERATURE

    if current_high and temperature_high:
        status = "CRITICAL"
    elif current_high or temperature_high:
        status = "WARNING"
    else:
        status = "NORMAL"

    if status != "NORMAL":
        abnormal_count += 1

    print(
        f"Sensor {sensor['id']} | "
        f"Current: {current:.1f} A | "
        f"Temperature: {temperature:.1f} C | "
        f"{status}"
    )

average_current = sum(
    sensor["current"]
    for sensor in battery_data
) / len(battery_data)

highest_current = max(
    battery_data,
    key=lambda sensor: sensor["current"]
)

hottest_sensor = max(
    battery_data,
    key=lambda sensor: sensor["temperature"]
)

overload_count = sum(
    sensor["current"] > MAX_CURRENT
    for sensor in battery_data
)

print(f"\nAverage Current   : {average_current:.1f} A")

print(
    f"Highest Current   : Sensor "
    f"{highest_current['id']} "
    f"({highest_current['current']:.1f} A)"
)

print(
    f"Hottest Sensor    : Sensor "
    f"{hottest_sensor['id']} "
    f"({hottest_sensor['temperature']:.1f} C)"
)

print(f"Current Overloads : {overload_count}")
print(f"Abnormal Sensors  : {abnormal_count}")

if (
    highest_current["current"] > MAX_CURRENT
    and hottest_sensor["temperature"] > MAX_TEMPERATURE
):
    print("\nSystem Status : CRITICAL")
    print("Battery Alert : Current and temperature overload detected")
    print("Action        : Reduce simulated battery load and inspect sensor.")
elif abnormal_count > 0:
    print("\nSystem Status : WARNING")
    print("Battery Alert : Abnormal sensor value detected")
    print("Action        : Continue monitoring.")
else:
    print("\nSystem Status : NORMAL")
    print("Battery Alert : Battery parameters are within demo limits")
    print("Action        : Continue monitoring.")

print("====================================================")