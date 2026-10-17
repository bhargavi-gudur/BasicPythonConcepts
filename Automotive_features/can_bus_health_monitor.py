"""
File: can_bus_health_monitor.py
Author: Gandla Bhargavi
Brief: Automotive CAN bus communication health monitoring
Date: 17-10-2026
"""

from abc import ABC, abstractmethod


class CANMonitor(ABC):

    @abstractmethod
    def process_data(self):
        pass


class CANBusHealthMonitor(CANMonitor):

    def __init__(self, configurations, messages):
        self.configurations = {
            config["can_id"]: config
            for config in configurations
        }

        self.messages = messages

        self.message_states = {
            can_id: {
                "last_received": -1,
                "fault_count": 0,
                "timed_out": False
            }
            for can_id in self.configurations
        }

        self.unknown_id_count = 0
        self.invalid_length_count = 0

    def receive_message(self, message):
        can_id = message["can_id"]
        config = self.configurations.get(can_id)

        if config is None:
            print(
                f"[UNKNOWN ID] CAN ID 0x{can_id:X} "
                f"at {message['timestamp_ms']} ms"
            )

            self.unknown_id_count += 1
            return

        if message["payload_length"] != config["expected_length"]:
            print(
                f"[INVALID LENGTH] {config['name']} expected "
                f"{config['expected_length']} bytes, received "
                f"{message['payload_length']} bytes"
            )

            self.invalid_length_count += 1
            return

        state = self.message_states[can_id]

        if state["timed_out"]:
            print(
                f"[RECOVERED] {config['name']} received at "
                f"{message['timestamp_ms']} ms"
            )

        state["last_received"] = message["timestamp_ms"]
        state["timed_out"] = False

    def check_timeouts(self, current_time):
        for can_id, config in self.configurations.items():
            state = self.message_states[can_id]

            reference_time = state["last_received"]

            if reference_time == -1:
                reference_time = 0

            elapsed = current_time - reference_time

            if elapsed > config["timeout_ms"] and not state["timed_out"]:
                state["timed_out"] = True
                state["fault_count"] += 1

                print(
                    f"[TIMEOUT] {config['name']} "
                    f"(CAN ID 0x{can_id:X}) - "
                    f"{elapsed} ms since last valid message"
                )

    def display_summary(self):
        print("\nCAN BUS HEALTH SUMMARY")
        print("-" * 50)

        print(
            f"{'Message':<22}"
            f"{'CAN ID':<14}"
            f"{'Status':<14}"
            f"Fault Count"
        )

        print("-" * 50)

        for can_id, config in self.configurations.items():
            state = self.message_states[can_id]

            status = "TIMEOUT" if state["timed_out"] else "HEALTHY"

            print(
                f"{config['name']:<22}"
                f"0x{can_id:X}{'':<9}"
                f"{status:<14}"
                f"{state['fault_count']}"
            )

        print(f"\nUnknown CAN IDs: {self.unknown_id_count}")
        print(
            f"Invalid payload lengths: "
            f"{self.invalid_length_count}"
        )

    def process_data(self):
        print("AUTOMOTIVE CAN BUS HEALTH MONITOR")
        print("=" * 50)

        index = 0

        for current_time in range(0, 301, 50):
            while (
                index < len(self.messages)
                and self.messages[index]["timestamp_ms"] == current_time
            ):
                self.receive_message(self.messages[index])
                index += 1

            self.check_timeouts(current_time)

        self.display_summary()


def main():
    configurations = [
        {
            "name": "EngineSpeed",
            "can_id": 0x100,
            "expected_length": 8,
            "timeout_ms": 100
        },
        {
            "name": "VehicleSpeed",
            "can_id": 0x200,
            "expected_length": 8,
            "timeout_ms": 150
        },
        {
            "name": "BrakeStatus",
            "can_id": 0x300,
            "expected_length": 1,
            "timeout_ms": 100
        }
    ]

    messages = [
        {"can_id": 0x100, "timestamp_ms": 0, "payload_length": 8},
        {"can_id": 0x200, "timestamp_ms": 0, "payload_length": 8},
        {"can_id": 0x300, "timestamp_ms": 0, "payload_length": 1},

        {"can_id": 0x100, "timestamp_ms": 50, "payload_length": 8},
        {"can_id": 0x300, "timestamp_ms": 50, "payload_length": 1},

        {"can_id": 0x100, "timestamp_ms": 100, "payload_length": 8},
        {"can_id": 0x200, "timestamp_ms": 100, "payload_length": 6},

        {"can_id": 0x555, "timestamp_ms": 150, "payload_length": 8},

        {"can_id": 0x100, "timestamp_ms": 150, "payload_length": 8},
        {"can_id": 0x100, "timestamp_ms": 200, "payload_length": 8},
        {"can_id": 0x100, "timestamp_ms": 250, "payload_length": 8},
        {"can_id": 0x100, "timestamp_ms": 300, "payload_length": 8}
    ]

    monitor: CANMonitor = CANBusHealthMonitor(
        configurations,
        messages
    )

    monitor.process_data()


if __name__ == "__main__":
    main()