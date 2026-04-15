#!/usr/bin/env python3
"""Exercise 1: Archive Creation - Cyber Archives."""


def create_archive(filename: str) -> None:
    """Create a new archive with preservation data entries."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")
    with open(filename, 'w', encoding='utf-8') as file:
        print("Storage unit created successfully...")
        print("Inscribing preservation data...")
        entries = [
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee",
        ]
        for entry in entries:
            file.write(entry + "\n")
            print(entry)
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


def main() -> None:
    """Main entry point for archive creation."""
    create_archive("new_discovery.txt")


if __name__ == "__main__":
    main()
