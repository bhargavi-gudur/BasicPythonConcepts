"""
File: automotive_functional_safety_monitor.py
Author: Gandla Bhargavi
Brief: Simulates automotive fault handling and safety-state transitions.
Date: 22-10-2026
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class SafetyState(Enum):
    NORMAL = "NORMAL"
    DEGRADED = "DEGRADED"
    SAFE_STATE = "SAFE_STATE"


@dataclass
class FaultEvent:
    fault_name: str
    severity: Severity


class FaultHandler(ABC):
    @abstractmethod
    def process_fault(self, event: FaultEvent) -> None:
        pass

    @abstractmethod
    def print_status(self) -> None:
        pass


class SafetyMonitor(FaultHandler):
    def __init__(self):
        self.state = SafetyState.NORMAL
        self.fault_counts = {}

    def process_fault(self, event: FaultEvent) -> None:
        name = event.fault_name
        severity = event.severity

        self.fault_counts[name] = (
            self.fault_counts.get(name, 0) + 1
        )

        print(
            f"\nFault detected: {name} "
            f"| Severity: {severity.value}"
        )

        # Keep SAFE_STATE latched in this simulation.
        if self.state == SafetyState.SAFE_STATE:
            print("Safety state remains SAFE_STATE.")
            return

        if severity == Severity.INFO:
            print("Informational event recorded.")

        elif severity == Severity.WARNING:
            self.state = SafetyState.DEGRADED
            print("Warning response activated.")

        elif severity == Severity.CRITICAL:
            self.state = SafetyState.SAFE_STATE
            print("Critical fault! Entering safe state.")

        print(f"Current safety state: {self.state.value}")

    def print_status(self) -> None:
        print("\n===== SAFETY MONITOR REPORT =====")
        print(f"Safety state: {self.state.value}")
        print("Fault occurrence counts:")

        if not self.fault_counts:
            print("No faults recorded.")
        else:
            for name, count in sorted(self.fault_counts.items()):
                print(f"  {name}: {count}")

        print("=================================")


def main():
    monitor: FaultHandler = SafetyMonitor()

    events = [
        FaultEvent(
            "SteeringSensorTimeout", Severity.WARNING
        ),
        FaultEvent(
            "CommunicationDelay", Severity.WARNING
        ),
        FaultEvent(
            "BrakeControllerFailure", Severity.CRITICAL
        ),
        FaultEvent(
            "SecondarySensorWarning", Severity.WARNING
        ),
        FaultEvent(
            "SystemInformation", Severity.INFO
        ),
    ]

    print("Automotive Functional Safety Monitor")

    for event in events:
        monitor.process_fault(event)

    monitor.print_status()


if __name__ == "__main__":
    main()