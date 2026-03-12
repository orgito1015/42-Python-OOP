#!/usr/bin/env python3
"""
Exercise 0: Planting Your First Seed
Introduction to Python program structure and execution
"""


def main() -> None:
    """Main function to display plant information"""
    # Plant information stored in variables
    plant_name: str = "Rose"
    plant_height: str = "25cm"
    plant_age: str = "30 days"

    # Display the plant information
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name}")
    print(f"Height: {plant_height}")
    print(f"Age: {plant_age}")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
