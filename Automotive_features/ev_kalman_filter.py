"""
File: ev_kalman_filter.py
Author: Gandla Bhargavi
Brief: EV battery temperature estimation using a Kalman filter
Date: 14-10-2026
"""

from abc import ABC, abstractmethod


# Abstract base class
class EVSensorSystem(ABC):

    @abstractmethod
    def process_data(self):
        pass


# Derived class
class BatteryTemperatureKalmanFilter(EVSensorSystem):

    def __init__(
        self,
        readings,
        initial_temperature,
        initial_uncertainty,
        process_noise,
        measurement_noise
    ):
        self.sensor_readings = readings

        self.estimated_temperature = initial_temperature
        self.estimation_uncertainty = initial_uncertainty

        self.process_noise = process_noise
        self.measurement_noise = measurement_noise

    def process_data(self):
        print("EV Battery Temperature Kalman Filter")
        print("-------------------------------------")

        print(
            f"{'Sample':<10}"
            f"{'Sensor Temp':<18}"
            f"{'Kalman Gain':<18}"
            f"{'Estimated Temp':<20}"
        )

        print("-" * 66)

        for index, measured_temperature in enumerate(
            self.sensor_readings, start=1
        ):
            # Step 1: Predict the temperature
            predicted_temperature = self.estimated_temperature

            # Step 2: Predict uncertainty
            predicted_uncertainty = (
                self.estimation_uncertainty
                + self.process_noise
            )

            # Step 3: Calculate Kalman gain
            kalman_gain = (
                predicted_uncertainty
                / (
                    predicted_uncertainty
                    + self.measurement_noise
                )
            )

            # Step 4: Update temperature estimate
            self.estimated_temperature = (
                predicted_temperature
                + kalman_gain
                * (
                    measured_temperature
                    - predicted_temperature
                )
            )

            # Step 5: Update uncertainty
            self.estimation_uncertainty = (
                (1 - kalman_gain)
                * predicted_uncertainty
            )

            print(
                f"{index:<10}"
                f"{measured_temperature:<18.2f}"
                f"{kalman_gain:<18.2f}"
                f"{self.estimated_temperature:<20.2f}"
            )

        print(
            f"\nFinal Estimated Temperature: "
            f"{self.estimated_temperature:.2f} C"
        )

        print(
            f"Final Estimation Uncertainty: "
            f"{self.estimation_uncertainty:.2f}"
        )


def main():
    # Simulated sensor readings
    temperature_readings = [
        26.0, 26.5, 27.2, 29.0
    ]

    sensor: EVSensorSystem = BatteryTemperatureKalmanFilter(
        readings=temperature_readings,
        initial_temperature=25.0,
        initial_uncertainty=1.0,
        process_noise=0.1,
        measurement_noise=4.0
    )

    sensor.process_data()


if __name__ == "__main__":
    main()