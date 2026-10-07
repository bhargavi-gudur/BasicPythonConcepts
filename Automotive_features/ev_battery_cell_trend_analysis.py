"""
@file ev_battery_cell_trend_analysis.py
@author Gandla Bhargavi
@brief Simple EV battery cell voltage and temperature trend analysis.
@date 07-10-2026
"""

cells = [
    {
        "id": 1,
        "previous_voltage": 3.72,
        "current_voltage": 3.71,
        "previous_temperature": 34.0,
        "current_temperature": 35.0
    },
    {
        "id": 2,
        "previous_voltage": 3.71,
        "current_voltage": 3.68,
        "previous_temperature": 37.0,
        "current_temperature": 40.0
    },
    {
        "id": 3,
        "previous_voltage": 3.68,
        "current_voltage": 3.57,
        "previous_temperature": 43.0,
        "current_temperature": 50.5
    },
    {
        "id": 4,
        "previous_voltage": 3.73,
        "current_voltage": 3.72,
        "previous_temperature": 35.0,
        "current_temperature": 36.0
    },
    {
        "id": 5,
        "previous_voltage": 3.70,
        "current_voltage": 3.64,
        "previous_temperature": 39.0,
        "current_temperature": 45.5
    },
    {
        "id": 6,
        "previous_voltage": 3.72,
        "current_voltage": 3.71,
        "previous_temperature": 38.0,
        "current_temperature": 39.0
    }
]

VOLTAGE_DROP_LIMIT = 0.05
TEMPERATURE_RISE_LIMIT = 5.0
CRITICAL_TEMPERATURE = 50.0

print("===== EV BATTERY CELL TREND MONITOR =====")

abnormal_cells = 0

for cell in cells:

    voltage_change = (
        cell["current_voltage"] -
        cell["previous_voltage"]
    )

    temperature_change = (
        cell["current_temperature"] -
        cell["previous_temperature"]
    )

    voltage_dropping = (
        voltage_change < -VOLTAGE_DROP_LIMIT
    )

    temperature_rising = (
        temperature_change > TEMPERATURE_RISE_LIMIT
    )

    critical_temperature = (
        cell["current_temperature"] >
        CRITICAL_TEMPERATURE
    )

    if (
        critical_temperature
        and voltage_dropping
        and temperature_rising
    ):
        status = "CRITICAL"

    elif (
        voltage_dropping
        or temperature_rising
        or critical_temperature
    ):
        status = "WARNING"

    else:
        status = "NORMAL"

    if status != "NORMAL":
        abnormal_cells += 1

    print(
        f"Cell {cell['id']} | "
        f"Voltage Change: {voltage_change:.3f} V | "
        f"Temperature Change: {temperature_change:.1f} C | "
        f"{status}"
    )

average_voltage_change = sum(
    cell["current_voltage"] -
    cell["previous_voltage"]
    for cell in cells
) / len(cells)

largest_voltage_drop = min(
    cells,
    key=lambda cell:
    cell["current_voltage"] -
    cell["previous_voltage"]
)

largest_temperature_rise = max(
    cells,
    key=lambda cell:
    cell["current_temperature"] -
    cell["previous_temperature"]
)

voltage_drop_count = sum(
    (
        cell["current_voltage"] -
        cell["previous_voltage"]
    ) < -VOLTAGE_DROP_LIMIT
    for cell in cells
)

temperature_rise_count = sum(
    (
        cell["current_temperature"] -
        cell["previous_temperature"]
    ) > TEMPERATURE_RISE_LIMIT
    for cell in cells
)

print(
    f"\nAverage Voltage Change : "
    f"{average_voltage_change:.3f} V"
)

print(
    f"Largest Voltage Drop  : Cell "
    f"{largest_voltage_drop['id']} "
    f"("
    f"{largest_voltage_drop['current_voltage'] - largest_voltage_drop['previous_voltage']:.3f}"
    f" V)"
)

print(
    f"Largest Temperature Rise : Cell "
    f"{largest_temperature_rise['id']} "
    f"("
    f"{largest_temperature_rise['current_temperature'] - largest_temperature_rise['previous_temperature']:.1f}"
    f" C)"
)

print(f"Voltage Drop Cells     : {voltage_drop_count}")
print(f"Temperature Rise Cells : {temperature_rise_count}")
print(f"Abnormal Cells         : {abnormal_cells}")

if (
    largest_temperature_rise["current_temperature"]
    > CRITICAL_TEMPERATURE
    and voltage_drop_count > 0
    and temperature_rise_count > 0
):
    print("\nSystem Status : CRITICAL")
    print("Battery Alert : Rapid cell parameter deterioration detected")
    print("Action        : Reduce simulated battery load and inspect affected cell.")

elif abnormal_cells > 0:
    print("\nSystem Status : WARNING")
    print("Battery Alert : Cell voltage or temperature trend anomaly detected")
    print("Action        : Continue monitoring cell trends.")

else:
    print("\nSystem Status : NORMAL")
    print("Battery Alert : Cell trends are within demo limits")
    print("Action        : Continue monitoring.")

print("===========================================")