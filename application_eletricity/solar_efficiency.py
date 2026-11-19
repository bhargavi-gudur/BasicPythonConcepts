"""
@file solar_efficiency.py
@brief Calculates solar panel conversion efficiency.
@date 19/11/2026
"""

def calculate_efficiency(output, irradiance, area):
    """
    @brief Calculates solar panel efficiency.
    @param output Electrical output power in watts.
    @param irradiance Solar irradiance in W/m^2.
    @param area Panel area in square metres.
    @return Efficiency as a percentage.
    """
    return (output / (irradiance * area)) * 100


# Main program
print("SOLAR PANEL EFFICIENCY CALCULATOR")

output = float(input("Enter output power (W): "))
irradiance = float(input("Enter solar irradiance (W/m^2): "))
area = float(input("Enter panel area (m^2): "))

if (output < 0 or irradiance <= 0 or area <= 0 or
        output > irradiance * area):
    print("Invalid input.")
else:
    efficiency = calculate_efficiency(
        output, irradiance, area
    )

    print(f"\nSolar Panel Efficiency: {efficiency:.2f}%")