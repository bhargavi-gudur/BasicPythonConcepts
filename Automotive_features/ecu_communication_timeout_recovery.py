"""
File: ecu_communication_timeout_recovery.py
Author: Gandla Bhargavi
Brief: Simulates ECU communication timeout detection and recovery.
Date: 23-10-2026
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class CommunicationState(Enum):
    ONLINE = "ONLINE"
    RETRYING = "RETRYING"
    OFFLINE = "OFFLINE"


@dataclass
class ECU:
    name: str
    timeout_limit_ms: int
    retry_count: int = 0
    failure_count: int = 0
    state: CommunicationState = CommunicationState.ONLINE


@dataclass
class CommunicationEvent:
    ecu_name: str
    response_time_ms: int
    response_received: bool


class CommunicationManager(ABC):
    @abstractmethod
    def process_event(self, event: CommunicationEvent) -> None:
        pass

    @abstractmethod
    def print_report(self) -> None:
        pass


class ECURecoveryManager(CommunicationManager):
    def __init__(self):
        self.ecus = {}
        self.max_retries = 2

    def add_ecu(self, name: str, timeout_limit_ms: int) -> None:
        self.ecus[name] = ECU(name, timeout_limit_ms)

    def process_event(self, event: CommunicationEvent) -> None:
        ecu = self.ecus.get(event.ecu_name)

        if ecu is None:
            print(f"\nUnknown ECU: {event.ecu_name}")
            return

        print(f"\nECU: {ecu.name}")

        if ecu.state == CommunicationState.OFFLINE:
            print("ECU is OFFLINE. Recovery is required.")
            return

        timed_out = (
            not event.response_received
            or event.response_time_ms > ecu.timeout_limit_ms
        )

        if not timed_out:
            if ecu.state == CommunicationState.RETRYING:
                print("Communication recovered after retry.")
            else:
                print("Response received within timeout.")

            ecu.state = CommunicationState.ONLINE
            ecu.retry_count = 0

        else:
            ecu.failure_count += 1
            print("Communication timeout detected.")

            if ecu.retry_count < self.max_retries:
                ecu.retry_count += 1
                ecu.state = CommunicationState.RETRYING

                print(
                    f"Retry attempt: {ecu.retry_count}"
                    f"/{self.max_retries}"
                )
            else:
                ecu.state = CommunicationState.OFFLINE
                print("Maximum retries exceeded.")
                print("ECU marked OFFLINE.")

        print(f"Current state: {ecu.state.value}")

    def print_report(self) -> None:
        print("\n===== ECU COMMUNICATION REPORT =====")

        for name in sorted(self.ecus):
            ecu = self.ecus[name]

            print(
                f"ECU: {ecu.name} | State: {ecu.state.value}"
                f" | Retries: {ecu.retry_count}"
                f" | Failures: {ecu.failure_count}"
            )

        print("====================================")


def main():
    manager: CommunicationManager = ECURecoveryManager()

    # Configure the simulated ECUs.
    manager.add_ecu("EngineECU", 100)
    manager.add_ecu("TransmissionECU", 100)
    manager.add_ecu("BrakingECU", 100)

    events = [
        CommunicationEvent("EngineECU", 40, True),

        CommunicationEvent("TransmissionECU", 150, True),
        CommunicationEvent("TransmissionECU", 60, True),

        CommunicationEvent("BrakingECU", 150, False),
        CommunicationEvent("BrakingECU", 170, False),
        CommunicationEvent("BrakingECU", 180, False),
    ]

    print("ECU Communication Timeout Recovery Manager")

    for event in events:
        manager.process_event(event)

    manager.print_report()


if __name__ == "__main__":
    main()