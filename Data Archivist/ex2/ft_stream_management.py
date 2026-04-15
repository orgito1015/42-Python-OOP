#!/usr/bin/env python3
"""Exercise 2: Stream Management - Cyber Archives."""

import sys


def run_communication_system() -> None:
    """Run the three-channel communication system."""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    sys.stdout.write("Input Stream active.\tEnter archivist ID: ")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().strip()
    sys.stdout.write("Input Stream active.\tEnter status report: ")
    sys.stdout.flush()
    status_report = sys.stdin.readline().strip()

    sys.stdout.write(
        f"[STANDARD] Archive status from {archivist_id}: "
        f"{status_report}\n"
    )
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


def main() -> None:
    """Main entry point for stream management."""
    run_communication_system()


if __name__ == "__main__":
    main()
