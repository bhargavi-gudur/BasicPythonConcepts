"""
@file power_factor_correction.py
@brief Estimates capacitor bank size for power factor correction.
@date 18/11/2026
"""

import math

def calculate_capacitor(power, initial_pf, target_pf):
    """
    @brief Calculates the required capacitor bank rating.
    @param power Active power in kW.
    @param initial_pf Initial power factor.
    @param target_pf Desired power factor.
    @return Required capacitor rating in kVAR.
    """
    phi1 = math.acos(initial_pf)
    phi2 = math.acos(target_pf)

    return power * (math.tan(phi1) - math.tan(phi2))


# Main program
print("POWER FACTOR CORRECTION CALCULATOR")

power = float(input("Enter active power (kW): "))
initial_pf = float(input("Enter initial power factor: "))
target_pf = float(input("Enter target power factor: "))

if (power <= 0 or not 0 < initial_pf <= 1 or
        not 0 < target_pf <= 1 or target_pf < initial_pf):
    print("Invalid input. Target PF must be greater than or equal to initial PF.")
else:
    capacitor = calculate_capacitor(
        power, initial_pf, target_pf
    )

    print(f"\nRequired Capacitor Bank: {capacitor:.2f} kVAR")