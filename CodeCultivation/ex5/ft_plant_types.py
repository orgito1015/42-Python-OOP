#!/usr/bin/env python3
"""
Exercise 5: Specialized Plant Types
Using inheritance to create specialized plant types
"""


class Plant:
    """Base plant class with common features"""

    def __init__(self, name: str, height: int, age: int):
        """Initialize base plant attributes"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_basic_info(self) -> str:
        """Return basic plant information"""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """Flower class inheriting from Plant"""

    def __init__(self, name: str, height: int, age: int, color: str):
        """Initialize flower with parent attributes and color"""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        """Flower-specific blooming behavior"""
        return f"{self.name} is blooming beautifully!"

    def get_info(self) -> str:
        """Return flower-specific information"""
        return (
            f"{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    """Tree class inheriting from Plant"""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Initialize tree with parent attributes and trunk diameter"""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:
        """Tree-specific shade calculation"""
        shade_area = self.trunk_diameter * 1.56
        return f"{self.name} provides {int(shade_area)} square meters of shade"

    def get_info(self) -> str:
        """Return tree-specific information"""
        return (
            f"{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """Vegetable class inheriting from Plant"""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        """Initialize vegetable with parent attributes."""
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_nutrition_info(self) -> str:
        """Vegetable-specific nutritional information"""
        return f"{self.name} is rich in {self.nutritional_value}"

    def get_info(self) -> str:
        """Return vegetable-specific information"""
        return (
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )


def main() -> None:
    """Main function to demonstrate specialized plant types"""
    print("=== Garden Plant Types ===")

    # Create flowers
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    # Create trees
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2190, 40)

    # Create vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 15, 60, "fall", "vitamin A")

    # Display flower information
    print(rose.get_info())
    print(rose.bloom())
    print(tulip.get_info())
    print(tulip.bloom())

    # Display tree information
    print(oak.get_info())
    print(oak.produce_shade())
    print(pine.get_info())
    print(pine.produce_shade())

    # Display vegetable information
    print(tomato.get_info())
    print(tomato.get_nutrition_info())
    print(carrot.get_info())
    print(carrot.get_nutrition_info())


if __name__ == "__main__":
    main()
