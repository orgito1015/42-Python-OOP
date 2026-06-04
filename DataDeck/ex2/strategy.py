from abc import ABC, abstractmethod
from typing import cast

from ex0 import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleStrategy(ABC):
    """Abstract base class for battle strategies."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True if this strategy is valid for the given creature."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        """Execute the strategy and return a list of action messages."""
        pass


class NormalStrategy(BattleStrategy):
    """Strategy suitable for any creature: simply attacks."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    """Strategy for transform-capable creatures: transform, attack, revert."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        tc = cast(TransformCapability, creature)
        return [tc.transform(), creature.attack(), tc.revert()]


class DefensiveStrategy(BattleStrategy):
    """Strategy for heal-capable creatures: attack then heal."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        hc = cast(HealCapability, creature)
        return [creature.attack(), hc.heal()]
