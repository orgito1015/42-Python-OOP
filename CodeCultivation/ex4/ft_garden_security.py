#!/usr/bin/env python3
"""
Exercise 4: Garden Security System
Protecting plant data with encapsulation and validation
"""


class SecurePlant:
    """Secure plant class with data validation and encapsulation"""

    def __init__(self, name: str):
        """Initialize secure plant with name"""
        self.__name: str = name
        self.__height: int = 0
        self.__age: int = 0

    def set_height(self, height: int) -> None:
        """Set plant height with validation"""
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set plant age with validation"""
        if age < 0:
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Get plant height safely"""
        return self.__height

    def get_age(self) -> int:
        """Get plant age safely"""
        return self.__age

    def get_name(self) -> str:
        """Get plant name safely"""
        return self.__name

    def get_info(self) -> str:
        """Return formatted plant information"""
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


def main() -> None:
    """Main function to demonstrate garden security system"""
    print("=== Garden Security System ===")

    # Create a secure plant
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.get_name()}")

    # Set valid values
    rose.set_height(25)
    rose.set_age(30)

    # Try to set invalid values
    print("Invalid operation attempted: height -5cm [REJECTED]")
    rose.set_height(-5)

    # Display current plant status
    print(f"Current plant: {rose.get_info()}")


if __name__ == "__main__":
    main()
