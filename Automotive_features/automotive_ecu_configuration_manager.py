"""
File: automotive_ecu_configuration_manager.py
Author: Gandla Bhargavi
Brief: Manages ECU configuration parameters, validation, and history.
Date: 26-10-2026
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


@dataclass
class ConfigurationParameter:
    name: str
    value: float
    minimum: float
    maximum: float


@dataclass
class ConfigurationChange:
    parameter_name: str
    old_value: float
    new_value: float
    accepted: bool
    message: str
    version: int


class ConfigurationManager(ABC):
    @abstractmethod
    def update_parameter(self, name: str, new_value: float) -> bool:
        pass

    @abstractmethod
    def print_configuration(self) -> None:
        pass

    @abstractmethod
    def print_history(self) -> None:
        pass


class ECUConfigurationManager(ConfigurationManager):
    def __init__(self):
        self.parameters = {}
        self.history = []
        self.configuration_version = 1

    def add_parameter(
        self,
        name: str,
        initial_value: float,
        minimum: float,
        maximum: float,
    ) -> bool:
        values = (initial_value, minimum, maximum)

        if (
            not name
            or not all(math.isfinite(value) for value in values)
            or minimum > maximum
            or not minimum <= initial_value <= maximum
            or name in self.parameters
        ):
            print(
                f"Configuration rejected for {name}: "
                "invalid definition."
            )
            return False

        self.parameters[name] = ConfigurationParameter(
            name, initial_value, minimum, maximum
        )

        print(f"Parameter registered: {name} = {initial_value}")
        return True

    def update_parameter(self, name: str, new_value: float) -> bool:
        parameter = self.parameters.get(name)

        if parameter is None:
            self.history.append(
                ConfigurationChange(
                    name,
                    0.0,
                    new_value,
                    False,
                    "Unknown parameter",
                    self.configuration_version,
                )
            )

            print(f"Update rejected: unknown parameter {name}")
            return False

        old_value = parameter.value

        if (
            not math.isfinite(new_value)
            or not parameter.minimum <= new_value <= parameter.maximum
        ):
            self.history.append(
                ConfigurationChange(
                    name,
                    old_value,
                    new_value,
                    False,
                    "Value outside permitted range",
                    self.configuration_version,
                )
            )

            print(
                f"Update rejected: {name} value is "
                "outside permitted range."
            )
            return False

        if new_value == old_value:
            self.history.append(
                ConfigurationChange(
                    name,
                    old_value,
                    new_value,
                    True,
                    "No change required",
                    self.configuration_version,
                )
            )

            print(f"No change: {name} is already {old_value}")
            return True

        parameter.value = new_value
        self.configuration_version += 1

        self.history.append(
            ConfigurationChange(
                name,
                old_value,
                new_value,
                True,
                "Configuration updated",
                self.configuration_version,
            )
        )

        print(
            f"Update accepted: {name} changed from "
            f"{old_value} to {new_value} | "
            f"Version: {self.configuration_version}"
        )

        return True

    def print_configuration(self) -> None:
        print("\n===== ECU CONFIGURATION =====")
        print(f"Configuration version: {self.configuration_version}")

        for name in sorted(self.parameters):
            parameter = self.parameters[name]

            print(
                f"{parameter.name} = {parameter.value} "
                f"(Range: {parameter.minimum} "
                f"to {parameter.maximum})"
            )

        print("=============================")

    def print_history(self) -> None:
        print("\n===== CONFIGURATION HISTORY =====")

        if not self.history:
            print("No configuration changes recorded.")

        for change in self.history:
            status = "ACCEPTED" if change.accepted else "REJECTED"

            print(
                f"{change.parameter_name} | {status} | "
                f"{change.message} | Version: {change.version}"
            )

        print("=================================")


def main():
    manager: ConfigurationManager = ECUConfigurationManager()

    print("Automotive ECU Configuration Manager\n")

    # Register initial configuration parameters.
    manager.add_parameter("IdleSpeedRPM", 800, 600, 1200)
    manager.add_parameter("FanOnTempC", 95, 80, 110)
    manager.add_parameter("CabinTargetTempC", 22, 16, 30)

    print("\nApplying configuration updates...\n")

    manager.update_parameter("IdleSpeedRPM", 900)
    manager.update_parameter("FanOnTempC", 120)
    manager.update_parameter("CabinTargetTempC", 24)
    manager.update_parameter("UnknownParameter", 10)

    manager.print_configuration()
    manager.print_history()


if __name__ == "__main__":
    main()