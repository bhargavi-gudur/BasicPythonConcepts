"""
@file generator_fuel.py
@brief Calculates generator fuel consumption and cost.
@date 13/11/2026
"""

def calculate_fuel(rate, hours):
    """
    @brief Calculates total fuel consumption.
    @param rate Fuel consumption in litres per hour.
    @param hours Generator running time in hours.
    @return Total fuel consumed in litres.
    """
    return rate * hours


def calculate_cost(fuel, price):
    """
    @brief Calculates total fuel cost.
    @param fuel Total fuel consumed in litres.
    @param price Fuel price per litre.
    @return Total fuel cost.
    """
    return fuel * price


# Main program
print("GENERATOR FUEL COST CALCULATOR")

rate = float(input("Enter fuel consumption (litres/hour): "))
hours = float(input("Enter running time (hours): "))
price = float(input("Enter fuel price per litre: "))

if rate <= 0 or hours <= 0 or price <= 0:
    print("Invalid input. Values must be positive.")
else:
    fuel = calculate_fuel(rate, hours)
    cost = calculate_cost(fuel, price)

    print(f"\nTotal Fuel Consumed: {fuel:.2f} litres")
    print(f"Total Fuel Cost: Rs. {cost:.2f}")