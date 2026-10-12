"""
File: ev_complementary_filter.py
Author: Gandla Bhargavi
Brief: EV sensor fusion using a complementary filter
Date: 13-10-2026
"""

from abc import ABC, abstractmethod


# Abstract base class
class EVSensorSystem(ABC):

    @abstractmethod
    def process_data(self):
        pass


# Derived class
class ComplementaryFilter(EVSensorSystem):

    def __init__(self, sensor_data, alpha):
        self.sensor_data = sensor_data
        self.alpha = alpha
        self.estimated_angle = 0.0

    def process_data(self):
        print("EV Complementary Filter Sensor Fusion")
        print("--------------------------------------")
        print(f"Alpha: {self.alpha}\n")

        print(
            f"{'Sample':<10}"
            f"{'Accel Angle':<18}"
            f"{'Gyro Rate':<18}"
            f"{'Fused Angle':<18}"
        )

        print("-" * 64)

        for index, sample in enumerate(self.sensor_data, start=1):
            accel_angle = sample["accelerometer_angle"]
            gyro_rate = sample["gyroscope_rate"]
            delta_time = sample["delta_time"]

            # Predict angle using gyroscope
            gyro_angle = (
                self.estimated_angle
                + gyro_rate * delta_time
            )

            # Correct estimate using accelerometer
            self.estimated_angle = (
                self.alpha * gyro_angle
                + (1 - self.alpha) * accel_angle
            )

            print(
                f"{index:<10}"
                f"{accel_angle:<18.2f}"
                f"{gyro_rate:<18.2f}"
                f"{self.estimated_angle:<18.2f}"
            )

        print(
            f"\nFinal Estimated Angle: "
            f"{self.estimated_angle:.2f} degrees"
        )


def main():
    # Simulated sensor readings
    readings = [
        {
            "accelerometer_angle": 2.0,
            "gyroscope_rate": 3.0,
            "delta_time": 0.1
        },
        {
            "accelerometer_angle": 2.5,
            "gyroscope_rate": 4.0,
            "delta_time": 0.1
        },
        {
            "accelerometer_angle": 3.2,
            "gyroscope_rate": 2.0,
            "delta_time": 0.1
        },
        {
            "accelerometer_angle": 3.5,
            "gyroscope_rate": 1.0,
            "delta_time": 0.1
        }
    ]

    # Polymorphism through the base-class reference
    sensor: EVSensorSystem = ComplementaryFilter(
        readings, 0.98
    )

    sensor.process_data()


if __name__ == "__main__":
    main()