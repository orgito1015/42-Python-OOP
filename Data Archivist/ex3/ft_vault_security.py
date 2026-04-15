#!/usr/bin/env python3
"""Exercise 3: Vault Security - Cyber Archives."""


def read_classified_data(filename: str) -> str:
    """Read classified data using secure context manager."""
    with open(filename, 'r', encoding='utf-8') as vault:
        return vault.read()


def write_security_protocols(filename: str, content: str) -> None:
    """Write security protocols using secure context manager."""
    with open(filename, 'w', encoding='utf-8') as vault:
        vault.write(content)


def run_vault_security() -> None:
    """Execute secure vault operations with automatic sealing."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("SECURE EXTRACTION:")
    try:
        classified = read_classified_data("classified_data.txt")
    except FileNotFoundError:
        print(
            "ERROR: Classified data not found in vault. "
            "Run tools/data_generator.py first."
        )
        return
    for line in classified.strip().splitlines():
        print(line)

    print("SECURE PRESERVATION:")
    protocol = "[CLASSIFIED] New security protocols archived"
    write_security_protocols("security_protocols.txt", protocol)
    print(protocol)

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


def main() -> None:
    """Main entry point for vault security operations."""
    run_vault_security()


if __name__ == "__main__":
    main()
