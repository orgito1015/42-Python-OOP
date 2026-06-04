from abc import ABC, abstractmethod

from .creature import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating creature families."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base creature of the family."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved creature of the family."""
        pass


class FlameFactory(CreatureFactory):
    """Factory for creating Flame family creatures."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for creating Aqua family creatures."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
