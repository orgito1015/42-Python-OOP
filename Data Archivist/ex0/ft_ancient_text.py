#!/usr/bin/env python3
"""Exercise 0: Ancient Text Recovery - Cyber Archives."""


def recover_ancient_text(filename: str) -> None:
    """Recover and display data from an ancient archive file."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")
    with open(filename, 'r', encoding='utf-8') as file:
        print("Connection established...")
        print("RECOVERED DATA:")
        content = file.read()
        print(content.strip())
    print("Data recovery complete.")
    print("Storage unit disconnected.")


def main() -> None:
    """Main entry point for ancient text recovery."""
    filename = "ancient_fragment.txt"
    try:
        recover_ancient_text(filename)
    except FileNotFoundError:
        print(
            "ERROR: Storage vault not found. Run data generator first."
        )


if __name__ == "__main__":
    main()
