"""
File: ecu_sleep_wakeup_manager.py
Author: Gandla Bhargavi
Brief: Automotive ECU sleep and wake-up state manager
Date: 19-10-2026
"""

from abc import ABC, abstractmethod
from collections import Counter
from enum import Enum


class ECUState(Enum):
    ACTIVE = "ACTIVE"
    SLEEP_PENDING = "SLEEP_PENDING"
    SLEEP = "SLEEP"
    WAKING_UP = "WAKING_UP"


class ECUManager(ABC):

    @abstractmethod
    def process_data(self):
        pass


class ECUSleepWakeupManager(ECUManager):

    def __init__(self, events, inactivity_timeout):
        self.state = ECUState.ACTIVE

        self.events = sorted(
            events,
            key=lambda event: event["time_seconds"]
        )

        self.event_counts = Counter()

        self.inactivity_timeout = inactivity_timeout
        self.last_activity = 0
        self.wakeup_complete_at = 0

        self.ignition_on = False
        self.sleep_entries = 0
        self.wakeup_count = 0

    def change_state(self, new_state, current_time):
        if self.state == new_state:
            return

        print(
            f"[STATE] {self.state.value} -> "
            f"{new_state.value} at {current_time} s"
        )

        self.state = new_state

        if self.state == ECUState.SLEEP:
            self.sleep_entries += 1

    def start_wakeup(self, current_time):
        if self.state == ECUState.SLEEP:
            self.change_state(
                ECUState.WAKING_UP,
                current_time
            )

            self.wakeup_complete_at = current_time + 1
            self.wakeup_count += 1

    def handle_event(self, event, current_time):
        event_type = event["event_type"]

        print(f"[EVENT] {event_type} at {current_time} s")

        self.event_counts[event_type] += 1

        if event_type == "IGNITION_ON":
            self.ignition_on = True
            self.last_activity = current_time

            if self.state == ECUState.SLEEP:
                self.start_wakeup(current_time)

            elif self.state == ECUState.SLEEP_PENDING:
                self.change_state(
                    ECUState.ACTIVE,
                    current_time
                )

        elif event_type == "IGNITION_OFF":
            self.ignition_on = False
            self.last_activity = current_time

            if self.state == ECUState.ACTIVE:
                self.change_state(
                    ECUState.SLEEP_PENDING,
                    current_time
                )

        elif event_type == "DOOR_OPEN":
            self.last_activity = current_time

            if self.state == ECUState.SLEEP:
                self.start_wakeup(current_time)

        elif event_type == "NETWORK_WAKEUP":
            self.last_activity = current_time

            if self.state == ECUState.SLEEP:
                self.start_wakeup(current_time)

        else:
            print("[WARNING] Unknown event ignored.")

    def process_data(self):
        print("AUTOMOTIVE ECU SLEEP/WAKE-UP MANAGER")
        print("====================================")

        event_index = 0

        for current_time in range(26):
            # Process events scheduled for this second.
            while (
                event_index < len(self.events)
                and self.events[event_index]["time_seconds"]
                == current_time
            ):
                self.handle_event(
                    self.events[event_index],
                    current_time
                )

                event_index += 1

            # Complete wake-up.
            if (
                self.state == ECUState.WAKING_UP
                and current_time >= self.wakeup_complete_at
            ):
                if self.ignition_on:
                    self.change_state(
                        ECUState.ACTIVE,
                        current_time
                    )
                else:
                    self.change_state(
                        ECUState.SLEEP_PENDING,
                        current_time
                    )

            # Enter sleep after inactivity.
            if (
                self.state == ECUState.SLEEP_PENDING
                and not self.ignition_on
                and current_time - self.last_activity
                >= self.inactivity_timeout
            ):
                self.change_state(
                    ECUState.SLEEP,
                    current_time
                )

        self.display_summary()

    def display_summary(self):
        print("\nECU POWER MANAGEMENT SUMMARY")
        print("-----------------------------")

        print(f"Final state: {self.state.value}")

        ignition = "ON" if self.ignition_on else "OFF"
        print(f"Ignition: {ignition}")

        print(f"Sleep entries: {self.sleep_entries}")
        print(f"Wake-up sequences: {self.wakeup_count}")

        print("\nEvent counts:")

        for event_type, count in sorted(
            self.event_counts.items()
        ):
            print(f"{event_type}: {count}")


def main():
    events = [
        {"time_seconds": 0, "event_type": "IGNITION_ON"},
        {"time_seconds": 3, "event_type": "IGNITION_OFF"},
        {"time_seconds": 10, "event_type": "NETWORK_WAKEUP"},
        {"time_seconds": 17, "event_type": "DOOR_OPEN"}
    ]

    manager: ECUManager = ECUSleepWakeupManager(
        events,
        inactivity_timeout=5
    )

    manager.process_data()


if __name__ == "__main__":
    main()