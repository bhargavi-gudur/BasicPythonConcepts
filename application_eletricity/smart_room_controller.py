"""
@file smart_room_controller.py
@brief Controls electrical loads based on occupancy and room conditions.
@date 21/11/2026
"""

def control_room(occupied, dark, temperature):
    """
    @brief Determines device operation based on room conditions.
    @param occupied Room occupancy status.
    @param dark Lighting condition.
    @param temperature Room temperature in Celsius.
    """

    print("\n--- SMART ROOM CONTROL REPORT ---")

    if not occupied:
        print("Room Status: Unoccupied")
        print("Lights: OFF")
        print("Fan: OFF")
        print("Cooling: OFF")
        print("Mode: ENERGY SAVING")

    else:
        print("Room Status: Occupied")

        if dark:
            print("Lights: ON")
        else:
            print("Lights: OFF (Daylight Available)")

        if temperature >= 30:
            print("Cooling: ON")
        else:
            print("Cooling: OFF")

        if temperature >= 25:
            print("Fan: ON")
        else:
            print("Fan: OFF")

        print("Mode: COMFORT MODE")


# Main program
print("SMART ROOM POWER CONTROLLER")

occupancy = int(input("Is room occupied? (1=Yes, 0=No): "))
light = int(input("Is room dark? (1=Yes, 0=No): "))
temperature = float(input("Enter room temperature (C): "))

if (occupancy not in [0, 1] or
        light not in [0, 1] or
        temperature < -50 or temperature > 100):
    print("Invalid input.")
else:
    control_room(occupancy, light, temperature)