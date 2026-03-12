#!/usr/bin/env python3
"""
Exercise 1: Garden Data Organizer
Creating a Plant class to manage plant data efficiently
"""


class Plant:
    """Blueprint for representing a plant with its attributes"""

    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


def main() -> None:
    """Main function to demonstrate plant data organization"""
    # Create multiple plants
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    # Display plant registry
    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")


if __name__ == "__main__":
    main()
