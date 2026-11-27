"""
File: automotive_ecu_event_scheduler.py
Author: Gandla Bhargavi
Brief: Simulates priority-based periodic ECU task scheduling.
Date: 26-11-2026
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
import heapq


@dataclass
class ECUTask:
    name: str
    priority: int
    period_ms: int
    execution_time_ms: int
    next_release_ms: int
    deadline_ms: int
    execution_count: int = 0
    missed_deadlines: int = 0


@dataclass
class ScheduledTask:
    name: str
    priority: int
    release_time_ms: int
    deadline_ms: int
    execution_time_ms: int


class SchedulerInterface(ABC):

    @abstractmethod
    def register_task(self, task):
        pass

    @abstractmethod
    def run_until(self, end_time_ms):
        pass

    @abstractmethod
    def print_statistics(self):
        pass


class ECUEventScheduler(SchedulerInterface):

    def __init__(self):
        self.tasks = {}
        self.ready_queue = []
        self.execution_log = []
        self.current_time_ms = 0
        self.sequence = 0

    def register_task(self, task):
        if (
            not task.name
            or task.priority < 0
            or task.period_ms <= 0
            or task.execution_time_ms <= 0
            or task.deadline_ms < task.next_release_ms
            or task.execution_time_ms
            > task.deadline_ms - task.next_release_ms
            or task.name in self.tasks
        ):
            print(f"Task registration rejected: {task.name}")
            return

        self.tasks[task.name] = task

        print(
            f"Task registered: {task.name}"
            f" | Priority: {task.priority}"
            f" | Period: {task.period_ms} ms"
        )

    def release_due_tasks(self):
        for task in self.tasks.values():
            while task.next_release_ms <= self.current_time_ms:
                scheduled = ScheduledTask(
                    task.name,
                    task.priority,
                    task.next_release_ms,
                    task.deadline_ms,
                    task.execution_time_ms,
                )

                # Lower heap key means higher scheduling priority.
                heapq.heappush(
                    self.ready_queue,
                    (
                        -scheduled.priority,
                        scheduled.deadline_ms,
                        self.sequence,
                        scheduled,
                    ),
                )

                self.sequence += 1
                task.next_release_ms += task.period_ms
                task.deadline_ms += task.period_ms

    def run_until(self, end_time_ms):
        if end_time_ms < self.current_time_ms:
            print("Invalid scheduler end time.")
            return

        print("\nStarting ECU scheduler...")

        while True:
            self.release_due_tasks()

            if not self.ready_queue:
                next_release = min(
                    (
                        task.next_release_ms
                        for task in self.tasks.values()
                    ),
                    default=end_time_ms + 1,
                )

                if next_release > end_time_ms:
                    break

                self.current_time_ms = next_release
                continue

            _, _, _, scheduled = heapq.heappop(
                self.ready_queue
            )

            task = self.tasks[scheduled.name]

            finish_time = (
                self.current_time_ms
                + scheduled.execution_time_ms
            )

            if finish_time > end_time_ms:
                heapq.heappush(
                    self.ready_queue,
                    (
                        -scheduled.priority,
                        scheduled.deadline_ms,
                        self.sequence,
                        scheduled,
                    ),
                )
                self.sequence += 1
                break

            if finish_time > scheduled.deadline_ms:
                task.missed_deadlines += 1

                print(
                    f"Deadline missed: {scheduled.name}"
                    f" | Deadline: {scheduled.deadline_ms} ms"
                    f" | Finish: {finish_time} ms"
                )

                self.execution_log.append(
                    f"{scheduled.name} - DEADLINE MISSED"
                )
            else:
                print(
                    f"Executed: {scheduled.name}"
                    f" | Priority: {scheduled.priority}"
                    f" | Time: {self.current_time_ms}"
                    f" to {finish_time} ms"
                )

                self.execution_log.append(
                    f"{scheduled.name} - EXECUTED"
                )

            task.execution_count += 1
            self.current_time_ms = finish_time

        print(
            f"\nScheduler stopped at "
            f"{self.current_time_ms} ms"
        )

    def print_statistics(self):
        print("\n===== ECU TASK STATISTICS =====")

        for name in sorted(self.tasks):
            task = self.tasks[name]

            print(
                f"{task.name}"
                f" | Executions: {task.execution_count}"
                f" | Missed deadlines: {task.missed_deadlines}"
            )

        print("\nExecution history:")

        for item in self.execution_log:
            print(f"- {item}")

        print("================================")


def main():
    scheduler: SchedulerInterface = ECUEventScheduler()

    print("Automotive ECU Event Scheduler\n")

    scheduler.register_task(
        ECUTask("BrakeMonitor", 5, 20, 5, 0, 20)
    )

    scheduler.register_task(
        ECUTask("SensorAcquisition", 4, 30, 8, 0, 30)
    )

    scheduler.register_task(
        ECUTask("DashboardUpdate", 2, 50, 10, 0, 50)
    )

    scheduler.register_task(
        ECUTask("BackgroundLogger", 1, 100, 15, 0, 100)
    )

    scheduler.run_until(100)
    scheduler.print_statistics()


if __name__ == "__main__":
    main()