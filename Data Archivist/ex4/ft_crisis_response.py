#!/usr/bin/env python3
"""Exercise 4: Crisis Response - Cyber Archives."""

import os


def setup_crisis_scenarios() -> None:
    """Create test files needed for crisis response demonstrations."""
    vault_file = "classified_vault.txt"
    try:
        with open(vault_file, 'w', encoding='utf-8') as f:
            f.write("[CLASSIFIED] TOP SECRET - VAULT ACCESS RESTRICTED")
        os.chmod(vault_file, 0o000)
    except OSError:
        # Silent failure is acceptable: if setup fails the access_archive
        # call below will still demonstrate FileNotFoundError handling.
        pass


def access_archive(filename: str, crisis_mode: bool = True) -> None:
    """Access an archive with comprehensive crisis handling.

    Args:
        filename: Path to the archive file to access.
        crisis_mode: If True, prefix output with CRISIS ALERT.
                     If False, prefix with ROUTINE ACCESS.
    """
    prefix = "CRISIS ALERT" if crisis_mode else "ROUTINE ACCESS"
    print(f"{prefix}: Attempting access to '{filename}'...")
    try:
        with open(filename, 'r', encoding='utf-8') as vault:
            content = vault.read()
        print(f'SUCCESS: Archive recovered - "{content.strip()}"')
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {e}")
        print("STATUS: Crisis contained, damage assessed")


def run_crisis_response() -> None:
    """Execute the full crisis response protocol."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    setup_crisis_scenarios()

    access_archive("lost_archive.txt", crisis_mode=True)
    access_archive("classified_vault.txt", crisis_mode=True)
    access_archive("standard_archive.txt", crisis_mode=False)

    print("All crisis scenarios handled successfully. Archives secure.")


def main() -> None:
    """Main entry point for crisis response operations."""
    run_crisis_response()


if __name__ == "__main__":
    main()
