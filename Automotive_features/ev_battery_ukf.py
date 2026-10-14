"""
File: ev_battery_ukf.py
Author: Gandla Bhargavi
Brief: EV battery SoC estimation using an Unscented Kalman Filter
Date: 15-10-2026
"""

from abc import ABC, abstractmethod
from math import sqrt


class EVSensorSystem(ABC):

    @abstractmethod
    def process_data(self):
        pass


class BatteryUKF(EVSensorSystem):

    def __init__(
        self,
        samples,
        initial_soc,
        initial_covariance,
        process_noise,
        measurement_noise,
        capacity_ah,
        resistance
    ):
        self.samples = samples
        self.soc = initial_soc
        self.covariance = initial_covariance

        self.process_noise = process_noise
        self.measurement_noise = measurement_noise
        self.capacity_ah = capacity_ah
        self.resistance = resistance

    def open_circuit_voltage(self, state):
        return 3.0 + 1.2 * state - 0.1 * state * state

    def process_data(self):
        alpha = 0.5
        beta = 2.0
        kappa = 0.0
        n = 1.0

        lam = alpha**2 * (n + kappa) - n

        wm0 = lam / (n + lam)
        wc0 = wm0 + (1 - alpha**2 + beta)
        wi = 1 / (2 * (n + lam))

        print("EV Battery UKF - SoC Estimation")
        print("-----------------------------------------------")

        print(
            f"{'Sample':<8}"
            f"{'Voltage':<12}"
            f"{'SoC':<12}"
            f"{'Covariance':<14}"
        )

        print("-" * 46)

        for index, sample in enumerate(self.samples, start=1):
            current = sample["current"]
            voltage = sample["voltage"]
            dt = sample["delta_time"]

            # 1. Predict SoC using coulomb counting.
            predicted_soc = (
                self.soc
                - current * dt / (self.capacity_ah * 3600)
            )

            # 2. Predict covariance.
            predicted_covariance = (
                self.covariance + self.process_noise
            )

            # 3. Generate sigma points.
            spread = sqrt(
                (n + lam) * predicted_covariance
            )

            sigma0 = predicted_soc
            sigma1 = predicted_soc + spread
            sigma2 = predicted_soc - spread

            # 4. Propagate sigma points through voltage model.
            z0 = (
                self.open_circuit_voltage(sigma0)
                - current * self.resistance
            )

            z1 = (
                self.open_circuit_voltage(sigma1)
                - current * self.resistance
            )

            z2 = (
                self.open_circuit_voltage(sigma2)
                - current * self.resistance
            )

            # 5. Predict terminal voltage.
            predicted_voltage = (
                wm0 * z0 + wi * z1 + wi * z2
            )

            dz0 = z0 - predicted_voltage
            dz1 = z1 - predicted_voltage
            dz2 = z2 - predicted_voltage

            innovation_covariance = (
                wc0 * dz0**2
                + wi * dz1**2
                + wi * dz2**2
                + self.measurement_noise
            )

            dx0 = sigma0 - predicted_soc
            dx1 = sigma1 - predicted_soc
            dx2 = sigma2 - predicted_soc

            cross_covariance = (
                wc0 * dx0 * dz0
                + wi * dx1 * dz1
                + wi * dx2 * dz2
            )

            # 6. Calculate UKF gain.
            gain = (
                cross_covariance / innovation_covariance
            )

            # 7. Correct SoC estimate.
            self.soc = (
                predicted_soc
                + gain * (voltage - predicted_voltage)
            )

            self.soc = max(0.0, min(1.0, self.soc))

            # 8. Update covariance.
            self.covariance = (
                predicted_covariance
                - gain * innovation_covariance * gain
            )

            self.covariance = max(self.covariance, 1e-12)

            print(
                f"{index:<8}"
                f"{voltage:<12.4f}"
                f"{self.soc:<12.4f}"
                f"{self.covariance:<14.6f}"
            )

        print(f"\nEstimated Battery SoC: {self.soc * 100:.2f}%")


def main():
    readings = [
        {"current": 20.0, "voltage": 3.80, "delta_time": 10.0},
        {"current": 20.0, "voltage": 3.79, "delta_time": 10.0},
        {"current": 20.0, "voltage": 3.78, "delta_time": 10.0},
        {"current": 20.0, "voltage": 3.77, "delta_time": 10.0}
    ]

    system: EVSensorSystem = BatteryUKF(
        samples=readings,
        initial_soc=0.80,
        initial_covariance=0.01,
        process_noise=0.0001,
        measurement_noise=0.0004,
        capacity_ah=60.0,
        resistance=0.005
    )

    system.process_data()


if __name__ == "__main__":
    main()