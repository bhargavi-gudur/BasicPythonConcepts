"""
File: ecu_watchdog_monitor.py
Author: Gandla Bhargavi
Brief: Automotive ECU watchdog and task heartbeat monitor
Date: 16-10-2026
"""

from abc import ABC, abstractmethod


# Abstract base class
class ECUWatchdog(ABC):

    @abstractmethod
    def process_data(self):
        pass


# Derived class
class WatchdogMonitor(ECUWatchdog):

    def __init__(self):
        self.task_names = [
            "SensorTask",
            "CommunicationTask",
            "DiagnosticTask"
        ]

        # Each task stores timeout, last heartbeat,
        # fault count, and current fault state.
        self.tasks = {
            "SensorTask": {
                "timeout": 150,
                "last_heartbeat": 0,
                "fault_count": 0,
                "faulted": False
            },
            "CommunicationTask": {
                "timeout": 200,
                "last_heartbeat": 0,
                "fault_count": 0,
                "faulted": False
            },
            "DiagnosticTask": {
                "timeout": 250,
                "last_heartbeat": 0,
                "fault_count": 0,
                "faulted": False
            }
        }

        # Simulated heartbeat events.
        self.events = [
            (50, "SensorTask"),
            (100, "SensorTask"),
            (100, "CommunicationTask"),
            (150, "SensorTask"),
            (200, "SensorTask"),
            (250, "SensorTask"),
            (300, "SensorTask"),
            (400, "CommunicationTask")
        ]

    def receive_heartbeat(self, task_name, current_time):
        if task_name not in self.tasks:
            print(f"[ERROR] Unknown task: {task_name}")
            return

        task = self.tasks[task_name]

        if task["faulted"]:
            print(
                f"[RECOVERY] {task_name} responded again "
                f"at {current_time} ms"
            )

        task["last_heartbeat"] = current_time
        task["faulted"] = False

    def check_timeouts(self, current_time):
        for name in self.task_names:
            task = self.tasks[name]

            elapsed = current_time - task["last_heartbeat"]

            if elapsed > task["timeout"] and not task["faulted"]:
                task["faulted"] = True
                task["fault_count"] += 1

                print(
                    f"[TIMEOUT] {name} missed its heartbeat. "
                    f"Elapsed: {elapsed} ms, "
                    f"Limit: {task['timeout']} ms"
                )

    def display_summary(self):
        print("\nECU WATCHDOG SUMMARY")
        print("-" * 47)

        print(f"{'Task':<24}{'Status':<16}Fault Count")
        print("-" * 47)

        for name in self.task_names:
            task = self.tasks[name]

            status = "FAULT" if task["faulted"] else "ACTIVE"

            print(
                f"{name:<24}"
                f"{status:<16}"
                f"{task['fault_count']}"
            )

    def process_data(self):
        print("AUTOMOTIVE ECU WATCHDOG MONITOR")
        print("=" * 47)

        event_index = 0

        # Simulate time from 0 to 400 milliseconds.
        for current_time in range(0, 401, 50):

            # Process heartbeats scheduled for this time.
            while (
                event_index < len(self.events)
                and self.events[event_index][0] == current_time
            ):
                _, task_name = self.events[event_index]

                self.receive_heartbeat(
                    task_name,
                    current_time
                )

                event_index += 1

            self.check_timeouts(current_time)

        self.display_summary()


def main():
    watchdog: ECUWatchdog = WatchdogMonitor()
    watchdog.process_data()


if __name__ == "__main__":
    main()