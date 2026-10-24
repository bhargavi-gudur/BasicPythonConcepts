"""
File: automotive_dtc_priority_manager.py
Author: Gandla Bhargavi
Brief: Prioritizes automotive DTCs and escalates repeated faults.
Date: 24-10-2026
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import IntEnum


class Severity(IntEnum):
    INFO = 1
    WARNING = 2
    CRITICAL = 3


@dataclass
class DTCEvent:
    code: str
    description: str
    severity: Severity


@dataclass
class DTCRecord:
    code: str
    description: str
    base_severity: Severity
    current_severity: Severity
    occurrences: int = 0


class DiagnosticManager(ABC):
    @abstractmethod
    def process_event(self, event: DTCEvent) -> None:
        pass

    @abstractmethod
    def print_priority_report(self) -> None:
        pass


class DTCPriorityManager(DiagnosticManager):
    def __init__(self):
        self.records = {}

    @staticmethod
    def calculate_severity(record: DTCRecord) -> Severity:
        result = record.base_severity

        # Educational escalation rules:
        # 2 or more occurrences: at least WARNING.
        # 3 or more occurrences: CRITICAL.
        if record.occurrences >= 3:
            result = max(result, Severity.CRITICAL)
        elif record.occurrences >= 2:
            result = max(result, Severity.WARNING)

        return Severity(result)

    def process_event(self, event: DTCEvent) -> None:
        if event.code not in self.records:
            self.records[event.code] = DTCRecord(
                code=event.code,
                description=event.description,
                base_severity=event.severity,
                current_severity=event.severity,
            )

        record = self.records[event.code]

        # Keep the more severe base classification if the same
        # DTC arrives with different severity classifications.
        record.base_severity = max(
            record.base_severity,
            event.severity,
        )

        record.occurrences += 1
        record.current_severity = self.calculate_severity(record)

        print(
            f"DTC: {record.code}"
            f" | Occurrences: {record.occurrences}"
            f" | Priority: {record.current_severity.name}"
        )

    def print_priority_report(self) -> None:
        sorted_records = sorted(
            self.records.values(),
            key=lambda record: (
                -int(record.current_severity),
                -record.occurrences,
                record.code,
            ),
        )

        print("\n===== DTC PRIORITY REPORT =====")

        if not sorted_records:
            print("No diagnostic faults recorded.")

        for record in sorted_records:
            print(
                f"{record.code} | {record.description}"
                f" | Priority: {record.current_severity.name}"
                f" | Occurrences: {record.occurrences}"
            )

        print("===============================")


def main():
    manager: DiagnosticManager = DTCPriorityManager()

    events = [
        DTCEvent(
            "P0130", "Oxygen sensor circuit", Severity.WARNING
        ),
        DTCEvent(
            "C1234", "Brake system fault", Severity.CRITICAL
        ),
        DTCEvent(
            "P0130", "Oxygen sensor circuit", Severity.WARNING
        ),
        DTCEvent(
            "U0100", "ECU communication loss", Severity.WARNING
        ),
        DTCEvent(
            "P0130", "Oxygen sensor circuit", Severity.WARNING
        ),
        DTCEvent(
            "U0100", "ECU communication loss", Severity.WARNING
        ),
        DTCEvent(
            "B1010", "Cabin sensor alert", Severity.INFO
        ),
    ]

    print("Automotive DTC Priority Manager\n")

    for event in events:
        manager.process_event(event)

    manager.print_priority_report()


if __name__ == "__main__":
    main()