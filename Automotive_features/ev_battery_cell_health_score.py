"""
@file ev_battery_cell_health_score.py
@author Gandla Bhargavi
@brief Simple EV battery cell health scoring using voltage and temperature trends.
@date 08-10-2026
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
        "current_voltage": 3.63,
        "previous_temperature": 37.0,
        "current_temperature": 43.0
    },
    {
        "id": 3,
        "previous_voltage": 3.68,
        "current_voltage": 3.54,
        "previous_temperature": 43.0,
        "current_temperature": 51.0
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
        "current_temperature": 46.0
    },
    {
        "id": 6,
        "previous_voltage": 3.72,
        "current_voltage": 3.70,
        "previous_temperature": 38.0,
        "current_temperature": 40.0
    }
]

VOLTAGE_DROP_LIMIT = 0.05
TEMPERATURE_RISE_LIMIT = 5.0
HIGH_TEMPERATURE_LIMIT = 45.0

print("===== EV BATTERY CELL HEALTH MONITOR =====")

health_scores = []

for cell in cells:

    voltage_drop = (
        cell["previous_voltage"] -
        cell["current_voltage"]
    )

    temperature_rise = (
        cell["current_temperature"] -
        cell["previous_temperature"]
    )

    score = 100

    if voltage_drop > VOLTAGE_DROP_LIMIT:
        score -= 30

    if temperature_rise > TEMPERATURE_RISE_LIMIT:
        score -= 30

    if cell["current_temperature"] > HIGH_TEMPERATURE_LIMIT:
        score -= 20

    score = max(score, 0)

    if score >= 80:
        status = "HEALTHY"
    elif score >= 50:
        status = "WARNING"
    else:
        status = "CRITICAL"

    health_scores.append(
        {
            "id": cell["id"],
            "score": score,
            "status": status
        }
    )

    print(
        f"Cell {cell['id']} | "
        f"Voltage Drop: {voltage_drop:.2f} V | "
        f"Temperature Rise: {temperature_rise:.1f} C | "
        f"Health Score: {score}% | "
        f"{status}"
    )

average_health = sum(
    cell["score"]
    for cell in health_scores
) / len(health_scores)

weakest_cell = min(
    health_scores,
    key=lambda cell: cell["score"]
)

strongest_cell = max(
    health_scores,
    key=lambda cell: cell["score"]
)

healthy_cells = sum(
    cell["status"] == "HEALTHY"
    for cell in health_scores
)

warning_cells = sum(
    cell["status"] == "WARNING"
    for cell in health_scores
)

critical_cells = sum(
    cell["status"] == "CRITICAL"
    for cell in health_scores
)

print(f"\nAverage Health Score : {average_health:.1f}%")

print(
    f"Weakest Cell         : Cell "
    f"{weakest_cell['id']} "
    f"({weakest_cell['score']}%)"
)

print(
    f"Strongest Cell       : Cell "
    f"{strongest_cell['id']} "
    f"({strongest_cell['score']}%)"
)

print(f"Healthy Cells        : {healthy_cells}")
print(f"Warning Cells        : {warning_cells}")
print(f"Critical Cells       : {critical_cells}")

if critical_cells > 0:

    print("\nSystem Status : CRITICAL")
    print("Battery Alert : Weak cell health detected")
    print("Action        : Inspect affected cell and reduce simulated battery stress.")

elif warning_cells > 0:

    print("\nSystem Status : WARNING")
    print("Battery Alert : Cell health degradation detected")
    print("Action        : Continue monitoring cell trends.")

else:

    print("\nSystem Status : NORMAL")
    print("Battery Alert : Cell health is within demo limits")
    print("Action        : Continue monitoring.")

print("===========================================")