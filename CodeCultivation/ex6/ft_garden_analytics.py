#!/usr/bin/env python3
"""
Exercise 6: Garden Analytics Platform
Comprehensive garden management system with nested classes,
inheritance chains, and different method types
"""


class GardenManager:
    """Garden management system with analytics capabilities"""

    # Class variable to track all gardens
    total_gardens: int = 0

    class GardenStats:
        """Nested helper class for calculating garden statistics"""

        def __init__(self):
            """Initialize statistics tracker"""
            self.plants_added: int = 0
            self.total_growth: int = 0
            self.plant_types: dict = {
                'regular': 0,
                'flowering': 0,
                'prize': 0
            }

        def record_plant_added(self, plant_type: str) -> None:
            """Record a plant addition"""
            self.plants_added += 1
            if plant_type in self.plant_types:
                self.plant_types[plant_type] += 1

        def record_growth(self, amount: int) -> None:
            """Record plant growth"""
            self.total_growth += amount

        def get_summary(self) -> str:
            """Get statistics summary"""
            return (f"Plants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant types: {self.plant_types['regular']} regular, "
                    f"{self.plant_types['flowering']} flowering, "
                    f"{self.plant_types['prize']} prize flowers")

    def __init__(self, owner: str):
        """Initialize garden manager for an owner"""
        self.owner: str = owner
        self.plants: list = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        """Add a plant to the garden"""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

        # Determine plant type
        if isinstance(plant, PrizeFlower):
            plant_type = 'prize'
        elif isinstance(plant, FloweringPlant):
            plant_type = 'flowering'
        else:
            plant_type = 'regular'

        self.stats.record_plant_added(plant_type)

    def grow_all_plants(self) -> None:
        """Help all plants in the garden grow"""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            initial_height = plant.height
            plant.grow()
            growth = plant.height - initial_height
            self.stats.record_growth(growth)
            print(f"{plant.name} grew {growth}cm")

    def get_garden_score(self) -> int:
        """Calculate total garden score based on all plants"""
        total_score = 0
        for plant in self.plants:
            total_score += plant.height
            if isinstance(plant, PrizeFlower):
                total_score += plant.prize_points
        return total_score

    def display_report(self) -> None:
        """Display comprehensive garden report"""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(self.stats.get_summary())

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        """Create multiple gardens at once (class method)"""
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens

    @staticmethod
    def is_valid_height(height: int) -> bool:
        """Validate plant height (utility function)"""
        return height >= 0 and height <= 10000

    @classmethod
    def get_total_gardens(cls) -> int:
        """Get total number of gardens managed"""
        return cls.total_gardens


class Plant:
    """Base plant class"""

    def __init__(self, name: str, height: int):
        """Initialize base plant"""
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        """Grow the plant"""
        self.height += 1

    def get_info(self) -> str:
        """Return plant information"""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Flowering plant inheriting from Plant"""

    def __init__(self, name: str, height: int, flower_color: str):
        """Initialize flowering plant"""
        super().__init__(name, height)
        self.flower_color: str = flower_color
        self.is_blooming: bool = True

    def get_info(self) -> str:
        """Return flowering plant information"""
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (
            f"{self.name}: {self.height}cm, {self.flower_color} flowers "
            f"({bloom_status})"
        )


class PrizeFlower(FloweringPlant):
    """Prize flower inheriting from FloweringPlant"""

    def __init__(self, name: str, height: int, flower_color: str,
                 prize_points: int):
        """Initialize prize flower"""
        super().__init__(name, height, flower_color)
        self.prize_points: int = prize_points

    def get_info(self) -> str:
        """Return prize flower information"""
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


def main() -> None:
    """Main function to demonstrate garden analytics platform"""
    print("=== Garden Management System Demo ===")

    # Create a garden using the constructor
    alice_garden = GardenManager("Alice")

    # Add different types of plants
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    # Grow all plants
    alice_garden.grow_all_plants()

    # Display garden report
    alice_garden.display_report()

    # Test static method
    print(f"\nHeight validation test: {GardenManager.is_valid_height(100)}")

    # Create another garden for comparison
    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Fern", 30))
    bob_garden.add_plant(FloweringPlant("Daisy", 12, "white"))
    bob_garden.grow_all_plants()

    # Compare garden scores
    print(f"\nGarden scores - Alice: {alice_garden.get_garden_score()}, "
          f"Bob: {bob_garden.get_garden_score()}")

    # Display total gardens using class method
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")


if __name__ == "__main__":
    main()
