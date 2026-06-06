"""Exercise 0: Entering the Matrix - Virtual environment detector."""

import os
import site
import sys


def is_in_virtual_env() -> bool:
    """Return True if running inside a virtual environment."""
    in_venv = sys.prefix != sys.base_prefix
    return in_venv or os.environ.get("VIRTUAL_ENV") is not None


def get_venv_name() -> str:
    """Return the name of the active virtual environment."""
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    return os.path.basename(venv_path)


def get_venv_path() -> str:
    """Return the path of the active virtual environment."""
    return os.environ.get("VIRTUAL_ENV", sys.prefix)


def get_site_packages() -> str:
    """Return the site-packages directory for the current environment."""
    packages = site.getsitepackages()
    return packages[0] if packages else "Unknown"


def show_outside_venv() -> None:
    """Display information when running outside a virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print()
    print("Current Python:")
    print(f"  {sys.executable}")
    print()
    print("Virtual Environment:")
    print("  None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("  The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate  # On Unix")
    print(r"  matrix_env\Scripts\activate    # On Windows")
    print()
    print("Then run this program again.")


def show_inside_venv() -> None:
    """Display information when running inside a virtual environment."""
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print("Current Python:")
    print(f"  {sys.executable}")
    print()
    print("Virtual Environment:")
    print(f"  {get_venv_name()}")
    print()
    print("Environment Path:")
    print(f"  {get_venv_path()}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("  Safe to install packages without affecting")
    print("  the global system.")
    print()
    print("Package installation path:")
    print(f"  {get_site_packages()}")


def main() -> None:
    """Entry point for the construct program."""
    if is_in_virtual_env():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    main()
