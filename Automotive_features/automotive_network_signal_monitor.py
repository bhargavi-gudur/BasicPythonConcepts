"""
File: automotive_network_signal_monitor.py
Author: Gandla Bhargavi
Brief: Validates automotive network signals and detects stale data.
Date: 25-10-2026
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class SignalState(Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    STALE = "STALE"


@dataclass
class SignalConfig:
    name: str
    minimum: float
    maximum: float
    timeout_ms: int


@dataclass
class SignalData:
    value: float = 0.0
    last_update_ms: int = -1
    invalid_count: int = 0
    stale_count: int = 0
    has_value: bool = False
    last_value_in_range: bool = False
    state: SignalState = SignalState.STALE


@dataclass
class SignalSample:
    name: str
    value: float
    timestamp_ms: int


class SignalMonitorInterface(ABC):
    @abstractmethod
    def process_sample(self, sample: SignalSample) -> None:
        pass

    @abstractmethod
    def evaluate_stale_signals(self, current_time_ms: int) -> None:
        pass

    @abstractmethod
    def print_report(self) -> None:
        pass


class NetworkSignalMonitor(SignalMonitorInterface):
    def __init__(self):
        self.configurations = {}
        self.signals = {}

    def add_signal(
        self,
        name: str,
        minimum: float,
        maximum: float,
        timeout_ms: int,
    ) -> None:
        if minimum > maximum or timeout_ms < 0:
            print(f"Invalid configuration for {name}")
            return

        self.configurations[name] = SignalConfig(
            name, minimum, maximum, timeout_ms
        )

        self.signals.setdefault(name, SignalData())

    def process_sample(self, sample: SignalSample) -> None:
        config = self.configurations.get(sample.name)

        if config is None:
            print(f"\nUnknown signal: {sample.name}")
            return

        data = self.signals[sample.name]

        if (
            sample.timestamp_ms < 0
            or (
                data.has_value
                and sample.timestamp_ms < data.last_update_ms
            )
        ):
            print(
                f"\nRejected out-of-order sample for {sample.name}"
            )
            return

        data.value = sample.value
        data.last_update_ms = sample.timestamp_ms
        data.has_value = True

        data.last_value_in_range = (
            config.minimum <= sample.value <= config.maximum
        )

        if data.last_value_in_range:
            data.state = SignalState.VALID
            print(
                f"\n{sample.name}: {sample.value} -> VALID"
            )
        else:
            data.state = SignalState.INVALID
            data.invalid_count += 1

            print(
                f"\n{sample.name}: {sample.value} -> INVALID "
                f"(outside range {config.minimum} to "
                f"{config.maximum})"
            )

    def evaluate_stale_signals(self, current_time_ms: int) -> None:
        if current_time_ms < 0:
            print("Invalid evaluation time.")
            return

        print(
            f"\nChecking signal freshness at "
            f"{current_time_ms} ms"
        )

        for name, data in self.signals.items():
            config = self.configurations[name]

            is_stale = (
                not data.has_value
                or current_time_ms - data.last_update_ms
                > config.timeout_ms
            )

            if is_stale:
                if data.state != SignalState.STALE:
                    data.stale_count += 1

                data.state = SignalState.STALE
                print(f"{name} -> STALE")

            elif data.last_value_in_range:
                data.state = SignalState.VALID
                print(f"{name} -> VALID")

            else:
                data.state = SignalState.INVALID
                print(f"{name} -> INVALID")

    def print_report(self) -> None:
        print("\n===== NETWORK SIGNAL REPORT =====")

        for name in sorted(self.signals):
            data = self.signals[name]
            last_value = data.value if data.has_value else "N/A"

            print(
                f"{name} | State: {data.state.value}"
                f" | Last value: {last_value}"
                f" | Invalid samples: {data.invalid_count}"
                f" | Stale events: {data.stale_count}"
            )

        print("=================================")


def main():
    monitor: SignalMonitorInterface = NetworkSignalMonitor()

    # Configure signals and their educational limits.
    concrete_monitor = monitor
    concrete_monitor.add_signal(
        "VehicleSpeed", 0.0, 250.0, 100
    )
    concrete_monitor.add_signal(
        "EngineTemperature", -40.0, 150.0, 200
    )
    concrete_monitor.add_signal(
        "SteeringAngle", -540.0, 540.0, 100
    )

    samples = [
        SignalSample("VehicleSpeed", 80.0, 0),
        SignalSample("EngineTemperature", 95.0, 0),
        SignalSample("SteeringAngle", 20.0, 0),
        SignalSample("VehicleSpeed", 280.0, 50),
        SignalSample("EngineTemperature", 100.0, 100),
    ]

    print("Automotive Network Signal Validity Monitor")

    for sample in samples:
        monitor.process_sample(sample)

    monitor.evaluate_stale_signals(150)
    monitor.evaluate_stale_signals(250)
    monitor.print_report()


if __name__ == "__main__":
    main()