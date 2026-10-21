"""
File: automotive_fault_memory_logger.py
Author: Gandla Bhargavi
Brief: Automotive fault memory and diagnostic event logger
Date: 21-10-2026
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class FaultRecord:
    code: str
    description: str
    severity: Severity
    first_seen: int
    last_seen: int
    occurrences: int


@dataclass
class DiagnosticEvent:
    timestamp: int
    action: str
    fault_code: str


class DiagnosticSystem(ABC):

    @abstractmethod
    def process_data(self):
        pass


class FaultMemoryLogger(DiagnosticSystem):

    def __init__(self):
        self.active_faults = {}
        self.lifetime_counts = {}
        self.event_history = []

    def add_event(self, timestamp, action, code):
        self.event_history.append(
            DiagnosticEvent(timestamp, action, code)
        )

    def record_fault(
        self,
        code,
        description,
        severity,
        timestamp
    ):
        self.lifetime_counts[code] = (
            self.lifetime_counts.get(code, 0) + 1
        )

        if code in self.active_faults:
            fault = self.active_faults[code]

            fault.last_seen = timestamp
            fault.description = description
            fault.severity = severity
            fault.occurrences += 1

            self.add_event(timestamp, "REPEATED", code)

            print(
                f"[REPEATED] {code} | "
                f"Occurrences: {fault.occurrences}"
            )

        else:
            fault = FaultRecord(
                code=code,
                description=description,
                severity=severity,
                first_seen=timestamp,
                last_seen=timestamp,
                occurrences=self.lifetime_counts[code]
            )

            self.active_faults[code] = fault

            self.add_event(timestamp, "DETECTED", code)

            print(
                f"[DETECTED] {code} | "
                f"Severity: {severity.value}"
            )

    def clear_fault(self, code, timestamp):
        if code not in self.active_faults:
            print(f"[NOT FOUND] No active fault: {code}")
            return

        self.add_event(timestamp, "CLEARED", code)
        del self.active_faults[code]

        print(f"[CLEARED] {code} at {timestamp} s")

    def display_active_faults(self):
        print("\nACTIVE FAULT MEMORY")
        print("-" * 90)

        print(
            f"{'DTC':<12}"
            f"{'Description':<30}"
            f"{'Severity':<12}"
            f"{'Occurrences':<12}"
            f"{'First Seen':<12}"
            f"Last Seen"
        )

        print("-" * 90)

        if not self.active_faults:
            print("No active faults.")
            return

        for code in sorted(self.active_faults):
            fault = self.active_faults[code]

            print(
                f"{fault.code:<12}"
                f"{fault.description:<30}"
                f"{fault.severity.value:<12}"
                f"{fault.occurrences:<12}"
                f"{fault.first_seen:<12}"
                f"{fault.last_seen}"
            )

    def display_history(self):
        print("\nDIAGNOSTIC EVENT HISTORY")
        print("-" * 55)

        print(
            f"{'Timestamp':<15}"
            f"{'Action':<18}"
            f"DTC"
        )

        print("-" * 55)

        for event in self.event_history:
            print(
                f"{event.timestamp:<15}"
                f"{event.action:<18}"
                f"{event.fault_code}"
            )

    def display_summary(self):
        print("\nDIAGNOSTIC SUMMARY")
        print("-----------------------------")

        print(f"Active faults: {len(self.active_faults)}")
        print(f"Historical events: {len(self.event_history)}")

        print("\nLifetime fault occurrences:")

        for code in sorted(self.lifetime_counts):
            print(f"{code}: {self.lifetime_counts[code]}")

    def process_data(self):
        print("AUTOMOTIVE FAULT MEMORY LOGGER")
        print("========================================")

        self.record_fault(
            "P0128",
            "Coolant Temperature",
            Severity.WARNING,
            100
        )

        self.record_fault(
            "U0100",
            "Communication Lost",
            Severity.ERROR,
            120
        )

        self.record_fault(
            "P0128",
            "Coolant Temperature",
            Severity.WARNING,
            150
        )

        self.record_fault(
            "B1001",
            "Body Control Fault",
            Severity.INFO,
            180
        )

        self.clear_fault("U0100", 220)

        self.record_fault(
            "U0100",
            "Communication Lost",
            Severity.ERROR,
            250
        )

        self.display_active_faults()
        self.display_history()
        self.display_summary()


def main():
    logger: DiagnosticSystem = FaultMemoryLogger()
    logger.process_data()


if __name__ == "__main__":
    main()