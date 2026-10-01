"""
@file ev_battery_power_sensor.py
@author Gandla Bhargavi
@brief Simple EV battery voltage and current sensor monitoring.
@date 29-09-2026
"""

# Battery sensor readings
sensors = [
    {"id": 1, "voltage": 360, "current": 120},
    {"id": 2, "voltage": 365, "current": 145},
    {"id": 3, "voltage": 370, "current": 230},
    {"id": 4, "voltage": 362, "current": 130}
]

MAX_POWER = 80.0

print("===== EV BATTERY POWER MONITOR =====")

for sensor in sensors:
    voltage = sensor["voltage"]
    current = sensor["current"]

    # Power = Voltage × Current
    power = (voltage * current) / 1000

    if power > MAX_POWER:
        status = "WARNING"
    else:
        status = "NORMAL"

    print(
        f"Sensor {sensor['id']} | "
        f"Voltage: {voltage} V | "
        f"Current: {current} A | "
        f"Power: {power:.1f} kW | "
        f"{status}"
    )

print("====================================")