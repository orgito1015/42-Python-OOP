#!/usr/bin/env python3
"""
Exercise 2: Plant Growth Simulator
Adding behavior to plants through methods
"""


class Plant:
    """Plant class with growth and aging behaviors"""

    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        """Increase plant height by 1cm"""
        self.height += 1

    def age_plant(self) -> None:
        """Increase plant age by 1 day"""
        self.age += 1

    def get_info(self) -> str:
        """Return formatted plant information"""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """Main function to simulate plant growth"""
    # Create a plant
    rose = Plant("Rose", 25, 30)

    # Display initial state
    print("=== Day 1 ===")
    print(rose.get_info())

    # Record initial height
    initial_height = rose.height

    # Simulate a week of growth
    for day in range(7):
        rose.grow()
        rose.age_plant()

    # Display final state
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")


if __name__ == "__main__":
    main()
