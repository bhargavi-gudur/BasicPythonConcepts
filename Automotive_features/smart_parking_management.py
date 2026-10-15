"""
File: smart_parking_management.py
Author: Gandla Bhargavi
Brief: Smart parking management system for automobiles
Date: 15-10-2026
"""

from abc import ABC, abstractmethod


class ParkingSystem(ABC):

    @abstractmethod
    def process_data(self):
        pass


class SmartParking(ParkingSystem):

    def __init__(self, total_slots, hourly_rate):
        self.slots = [None] * total_slots
        self.parked_vehicles = {}
        self.hourly_rate = hourly_rate

    def park_vehicle(self, registration, vehicle_type, entry_hour):
        if registration in self.parked_vehicles:
            print("Vehicle is already parked.")
            return

        for index, slot in enumerate(self.slots):
            if slot is None:
                self.slots[index] = registration

                self.parked_vehicles[registration] = {
                    "vehicle_type": vehicle_type,
                    "entry_hour": entry_hour,
                    "slot": index
                }

                print(
                    f"Vehicle {registration} parked "
                    f"in slot {index + 1}."
                )
                return

        print(f"Parking is full for vehicle {registration}.")

    def exit_vehicle(self, registration, exit_hour):
        vehicle = self.parked_vehicles.get(registration)

        if vehicle is None:
            print("Vehicle not found.")
            return

        duration = exit_hour - vehicle["entry_hour"]

        if duration < 0:
            print("Invalid exit time.")
            return

        billable_hours = max(1, duration)
        fee = billable_hours * self.hourly_rate

        print(f"\nVehicle: {registration}")
        print(f"Parking duration: {duration} hour(s)")
        print(f"Parking fee: Rs. {fee:.2f}")

        self.slots[vehicle["slot"]] = None
        del self.parked_vehicles[registration]

    def display_status(self):
        occupied = len(self.parked_vehicles)
        available = len(self.slots) - occupied

        print("\nParking Status")
        print("--------------")
        print(f"Total slots: {len(self.slots)}")
        print(f"Occupied slots: {occupied}")
        print(f"Available slots: {available}")

    def process_data(self):
        self.display_status()


def main():
    parking = SmartParking(total_slots=3, hourly_rate=50.0)

    parking.park_vehicle("AP01AB1234", "Car", 9)
    parking.park_vehicle("AP02CD5678", "SUV", 10)
    parking.park_vehicle("AP03EF9012", "Car", 11)

    parking.process_data()

    print("\n--- Vehicle Exit ---")
    parking.exit_vehicle("AP01AB1234", 12)

    parking.process_data()


if __name__ == "__main__":
    main()