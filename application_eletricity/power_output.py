"""
Power Outage Impact Analyzer

Estimates outage impact based on:
- Outage duration
- Interrupted load
- Affected consumers
- Facility criticality

This is an educational simulation.
"""


def calculate_impact(duration, load, consumers, facility):
    """
    Calculate the power outage impact score.

    Args:
        duration: Outage duration in hours.
        load: Interrupted load in kW.
        consumers: Number of affected consumers.
        facility: Facility category.

    Returns:
        Impact score between 0 and 100.
    """

    score = 0

    if duration > 2:
        score += 20

    if duration > 6:
        score += 20

    if load > 100:
        score += 20

    if load > 500:
        score += 20

    if consumers > 100:
        score += 10

    if consumers > 1000:
        score += 10

    if facility == "commercial":
        score += 10
    elif facility == "industrial":
        score += 20
    elif facility == "hospital":
        score += 40

    return min(score, 100)


def classify_impact(score):
    """
    Classify outage severity based on impact score.

    Args:
        score: Calculated impact score.

    Returns:
        Severity category.
    """

    if score >= 80:
        return "SEVERE"
    elif score >= 60:
        return "HIGH"
    elif score >= 30:
        return "MODERATE"
    else:
        return "LOW"


def main():
    """Run the power outage impact analyzer."""

    print("Power Outage Impact Analyzer")
    print("---------------------------")

    try:
        duration = float(input("Enter outage duration (hours): "))
        load = float(input("Enter interrupted load (kW): "))
        consumers = int(input("Enter affected consumers: "))

        facility = input(
            "Facility type (residential/commercial/"
            "industrial/hospital): "
        ).strip().lower()

        if duration < 0 or load < 0 or consumers < 0:
            print("\nInvalid input. Negative values are not allowed.")
            return

        valid_facilities = [
            "residential", "commercial",
            "industrial", "hospital"
        ]

        if facility not in valid_facilities:
            print("\nInvalid facility type.")
            return

        interrupted_energy = duration * load

        score = calculate_impact(
            duration, load, consumers, facility
        )

        severity = classify_impact(score)

        print("\n--- Outage Analysis ---")
        print(f"Interrupted Energy: {interrupted_energy:.2f} kWh")
        print(f"Impact Score: {score}/100")
        print(f"Severity: {severity}")

        if severity == "SEVERE":
            print("Priority: Immediate restoration assessment")
        elif severity == "HIGH":
            print("Priority: High restoration priority")
        elif severity == "MODERATE":
            print("Priority: Restoration should be planned promptly")
        else:
            print("Priority: Normal restoration priority")

    except ValueError:
        print("\nInvalid input. Please enter valid numeric values.")


if __name__ == "__main__":
    main()