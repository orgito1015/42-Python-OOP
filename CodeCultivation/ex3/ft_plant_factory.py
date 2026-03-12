#!/usr/bin/env python3
"""
Exercise 3: Plant Factory
Streamlining plant creation with proper initialization
"""


class Plant:
    """Plant class with constructor for initialization"""

    def __init__(self, name: str, height: int, age: int):
        """Initialize plant with starting values"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return formatted plant information"""
        return f"{self.name} ({self.height}cm, {self.age} days)"


def main() -> None:
    """Main function to demonstrate plant factory"""
    print("=== Plant Factory Output ===")

    # Create multiple plants with different characteristics
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    # Display each created plant
    for plant in plants:
        print(f"Created: {plant.get_info()}")

    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
