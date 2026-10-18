"""
File: automotive_ota_update_manager.py
Author: Gandla Bhargavi
Brief: Automotive ECU OTA firmware update manager simulation
Date: 18-10-2026
"""

from abc import ABC, abstractmethod
from collections import Counter
from enum import Enum


class UpdateState(Enum):
    IDLE = "IDLE"
    DOWNLOADING = "DOWNLOADING"
    VERIFYING = "VERIFYING"
    READY_TO_INSTALL = "READY TO INSTALL"
    INSTALLING = "INSTALLING"
    COMPLETED = "COMPLETED"
    ROLLED_BACK = "ROLLED BACK"
    FAILED = "FAILED"


class OTAUpdateSystem(ABC):

    @abstractmethod
    def process_data(self):
        pass


class OTAUpdateManager(OTAUpdateSystem):

    def __init__(self, firmware):
        self.firmware = firmware
        self.state = UpdateState.IDLE

        self.event_log = []
        self.event_counts = Counter()

        self.installed_version = firmware["current_version"]

    def log_event(self, message):
        self.event_log.append(message)
        self.event_counts[message] += 1
        print(message)

    def show_summary(self):
        print("\n--- Update Summary ---")
        print(f"Final state: {self.state.value}")
        print(f"Installed version: {self.installed_version}")
        print(f"Events recorded: {len(self.event_log)}")

        print("\nEvent counts:")

        for event, count in self.event_counts.items():
            print(f"{event}: {count}")

    def process_data(self):
        firmware = self.firmware

        print("\n========================================")
        print("AUTOMOTIVE OTA UPDATE MANAGER")
        print("========================================")

        print(f"Target ECU: {firmware['target_ecu']}")
        print(f"Current version: {self.installed_version}")
        print(f"New version: {firmware['new_version']}\n")

        # Step 1: Check compatibility
        if not firmware["compatible"]:
            self.state = UpdateState.FAILED
            self.log_event(
                "[ERROR] Firmware is incompatible."
            )
            self.show_summary()
            return

        self.log_event(
            "[OK] Firmware compatibility verified."
        )

        # Step 2: Simulate download
        self.state = UpdateState.DOWNLOADING
        self.log_event("[DOWNLOAD] Firmware downloaded.")

        # Step 3: Verify signature
        self.state = UpdateState.VERIFYING
        self.log_event(
            "[VERIFY] Checking firmware signature."
        )

        if not firmware["signature_valid"]:
            self.state = UpdateState.FAILED
            self.log_event(
                "[ERROR] Firmware signature verification failed."
            )
            self.show_summary()
            return

        self.log_event(
            "[OK] Firmware signature verified."
        )

        # Step 4: Verify integrity
        self.log_event(
            "[VERIFY] Checking firmware checksum."
        )

        if not firmware["checksum_valid"]:
            self.state = UpdateState.FAILED
            self.log_event(
                "[ERROR] Firmware integrity check failed."
            )
            self.show_summary()
            return

        self.log_event(
            "[OK] Firmware integrity verified."
        )

        # Step 5: Prepare installation
        self.state = UpdateState.READY_TO_INSTALL
        self.log_event(
            "[OK] Firmware is ready to install."
        )

        # Step 6: Install firmware
        self.state = UpdateState.INSTALLING
        self.log_event(
            "[INSTALL] Starting firmware installation."
        )

        if not firmware["installation_succeeds"]:
            self.log_event(
                "[ERROR] Installation failed."
            )

            self.installed_version = firmware["current_version"]
            self.state = UpdateState.ROLLED_BACK

            self.log_event(
                "[ROLLBACK] Previous firmware restored."
            )

            self.show_summary()
            return

        # Step 7: Complete update
        self.installed_version = firmware["new_version"]
        self.state = UpdateState.COMPLETED

        self.log_event(
            "[SUCCESS] Firmware update completed."
        )

        self.show_summary()


def main():
    successful_update = {
        "target_ecu": "BodyControlECU",
        "current_version": "1.0.0",
        "new_version": "1.1.0",
        "compatible": True,
        "signature_valid": True,
        "checksum_valid": True,
        "installation_succeeds": True
    }

    failed_update = {
        "target_ecu": "GatewayECU",
        "current_version": "2.0.0",
        "new_version": "2.1.0",
        "compatible": True,
        "signature_valid": True,
        "checksum_valid": True,
        "installation_succeeds": False
    }

    update1: OTAUpdateSystem = OTAUpdateManager(
        successful_update
    )

    update2: OTAUpdateSystem = OTAUpdateManager(
        failed_update
    )

    print("SCENARIO 1: SUCCESSFUL UPDATE")
    update1.process_data()

    print("\nSCENARIO 2: FAILED UPDATE")
    update2.process_data()


if __name__ == "__main__":
    main()