"""
File: vehicle_gateway_router.py
Author: Gandla Bhargavi
Brief: Automotive vehicle gateway message router simulation
Date: 20-10-2026
"""

from abc import ABC, abstractmethod
from collections import Counter


# Abstract base class
class GatewaySystem(ABC):

    @abstractmethod
    def process_data(self):
        pass


# Derived class
class VehicleGatewayRouter(GatewaySystem):

    def __init__(self, networks, routing_rules, messages):
        self.networks = set(networks)
        self.routing_rules = routing_rules
        self.messages = messages
        self.statistics = Counter()

    def find_route(self, source, destination):
        for rule in self.routing_rules:
            if (
                rule["source"] == source
                and rule["destination"] == destination
            ):
                return rule

        return None

    def route_message(self, message):
        can_id = message["message_id"]

        print(f"\nMessage ID: 0x{can_id:X}")
        print(f"Source: {message['source']}")
        print(f"Destination: {message['destination']}")

        # Validate source network
        if message["source"] not in self.networks:
            print("[BLOCKED] Unknown source network.")
            self.statistics["UnknownSource"] += 1
            self.statistics["Blocked"] += 1
            return

        # Validate destination network
        if message["destination"] not in self.networks:
            print("[BLOCKED] Unknown destination network.")
            self.statistics["UnknownDestination"] += 1
            self.statistics["Blocked"] += 1
            return

        # Classic CAN supports up to 8 payload bytes.
        if len(message["payload"]) > 8:
            print(
                "[BLOCKED] Invalid classic CAN payload length."
            )
            self.statistics["InvalidPayload"] += 1
            self.statistics["Blocked"] += 1
            return

        # Find the route
        rule = self.find_route(
            message["source"],
            message["destination"]
        )

        if rule is None:
            print("[BLOCKED] No routing rule configured.")
            self.statistics["NoRoute"] += 1
            self.statistics["Blocked"] += 1
            return

        # Validate message ID
        if can_id not in rule["allowed_ids"]:
            print("[BLOCKED] Message ID is not authorized.")
            self.statistics["Unauthorized"] += 1
            self.statistics["Blocked"] += 1
            return

        print("[FORWARDED] Message routed successfully.")
        self.statistics["Forwarded"] += 1

    def display_summary(self):
        print("\n\nGATEWAY ROUTING SUMMARY")
        print("=" * 40)

        print(f"{'Total messages':<24}{len(self.messages)}")
        print(f"{'Forwarded':<24}{self.statistics['Forwarded']}")
        print(f"{'Blocked':<24}{self.statistics['Blocked']}")

        print("\nBlock reasons:")

        print(
            f"{'Unauthorized ID':<24}"
            f"{self.statistics['Unauthorized']}"
        )

        print(
            f"{'No routing rule':<24}"
            f"{self.statistics['NoRoute']}"
        )

        print(
            f"{'Invalid payload':<24}"
            f"{self.statistics['InvalidPayload']}"
        )

        print(
            f"{'Unknown source':<24}"
            f"{self.statistics['UnknownSource']}"
        )

        print(
            f"{'Unknown destination':<24}"
            f"{self.statistics['UnknownDestination']}"
        )

    def process_data(self):
        print("AUTOMOTIVE VEHICLE GATEWAY ROUTER")
        print("=" * 40)

        print(f"Configured networks: {len(self.networks)}")
        print(f"Routing rules: {len(self.routing_rules)}")
        print("\nProcessing messages...")

        for message in self.messages:
            self.route_message(message)

        self.display_summary()


def main():
    networks = [
        "BodyCAN",
        "InfotainmentCAN",
        "PowertrainCAN",
        "GatewayCAN",
        "DiagnosticCAN"
    ]

    routing_rules = [
        {
            "source": "BodyCAN",
            "destination": "InfotainmentCAN",
            "allowed_ids": {0x120, 0x121}
        },
        {
            "source": "PowertrainCAN",
            "destination": "GatewayCAN",
            "allowed_ids": {0x201}
        },
        {
            "source": "DiagnosticCAN",
            "destination": "GatewayCAN",
            "allowed_ids": {0x700}
        }
    ]

    messages = [
        {
            "source": "BodyCAN",
            "destination": "InfotainmentCAN",
            "message_id": 0x120,
            "payload": [0x10, 0x20, 0x30, 0x40]
        },
        {
            "source": "PowertrainCAN",
            "destination": "GatewayCAN",
            "message_id": 0x201,
            "payload": [0x01, 0x02, 0x03]
        },
        {
            "source": "DiagnosticCAN",
            "destination": "GatewayCAN",
            "message_id": 0x700,
            "payload": [0xAA, 0xBB]
        },
        {
            "source": "BodyCAN",
            "destination": "InfotainmentCAN",
            "message_id": 0x555,
            "payload": [0x01, 0x02]
        },
        {
            "source": "BodyCAN",
            "destination": "DiagnosticCAN",
            "message_id": 0x120,
            "payload": [0x01]
        },
        {
            "source": "BodyCAN",
            "destination": "InfotainmentCAN",
            "message_id": 0x120,
            "payload": [0, 1, 2, 3, 4, 5, 6, 7, 8]
        },
        {
            "source": "BodyCAN",
            "destination": "UnknownCAN",
            "message_id": 0x120,
            "payload": [0x01]
        }
    ]

    gateway: GatewaySystem = VehicleGatewayRouter(
        networks,
        routing_rules,
        messages
    )

    gateway.process_data()


if __name__ == "__main__":
    main()